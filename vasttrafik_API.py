import requests
import datetime
import time

# Redbergsplatsen   9021014005460000
# Olskrokstorget    9021014005160000
# Östra sjukhuset   9021014007880000
# Brunnsparken      9021014001760000

class API_VT:
    """ Class for accessing Västtrafiks API
    """
    def __init__(self):
        self.token = ''
        self.expires_in = 0
        # Needed for the first comparison
        self.expires_time = datetime.datetime.now()-datetime.timedelta(seconds = 5)

    def retrieve_token(self):
        """ Method for retreiving a token

        Checks when token expires and only requests a new if the old one has expired
        """
        if self.expires_time < datetime.datetime.now():
            _url = 'https://api.vasttrafik.se:443/token'
            _payload = {'Content-Type': r'application/x-www-form-urlencoded',
                       'grant_type': r'client_credentials',
                       'Authorization': r'Basic VVpoNThiSnBzZkd6WVRUYm1lNzRLT21Lak1BYTpNTGszcjRPTm5CVGVsMHE2VTN5cVJrb0R5dGNh',
                       'client_id': r'UZh58bJpsfGzYTTbme74KOmKjMA',
                       'client_secret': r'MLk3r4ONnBTel0q6U3yqRkoDytc'}
            try:
                _req_token = requests.post(_url, _payload)
            except requests.exceptions.RequestException as ex:
                time.sleep(5)
                _req_token = requests.post(_url, _payload)
                
            _json_response = _req_token.json()
            self.token = _json_response['access_token']
            self.expires_in = _json_response['expires_in']
            self.expires_time = datetime.datetime.now()+datetime.timedelta(seconds = self.expires_in)
            return self.token
        else:
            return self.token

    def get_diff_minutes(self, tram_time):
        """ Method for retreiving how many minutes away a tram is to departure

        Takes time for departure for tram and returns in how many minutes
        that departure is. Assumes that the current time and tram time is  on the
        same day. Problems may occure close to midnight.
        """
        # Get current time
        self._datetime_now = datetime.datetime.now()
        # Get current date
        self._date_now = self._datetime_now.strftime('%Y-%m-%d')
        # Set tram time to occure on current day
        self._tr_time = datetime.datetime.strptime(self._date_now + " " +
                                                   tram_time, "%Y-%m-%d %H:%M")
        # Calculate time difference in minutes
        minutes_diff = round((self._tr_time -
                              self._datetime_now).total_seconds() / 60.0)
        # Return only int
        return int(minutes_diff)
    

    def retrieve_trams(self, token, departure_ID, arrival_ID, time_offset, nbr_of_deps):
        """ Method for accessing departures

        Returns departures from a certain stopID to another stopID, given a token and
        how much of a time offest that should be added
        """
        self._now_time = datetime.datetime.now()
        # Current time plus offset
        self._tram_datetime = (datetime.datetime.now() +
                               datetime.timedelta(minutes = time_offset))
        self._tram_date = self._tram_datetime.strftime('%Y-%m-%d')
        self._tram_time = self._tram_datetime.strftime('%H:%M')
        # Create request information
        self._url_short = r'https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard?id=' + departure_ID
        self._payload = {'date': self._tram_date,
               'time': self._tram_time,
               'timeSpan': '30',               # Maximum timespan
               'maxDeparturesPerLine': '2',    # Maximum departures per line
               'needJourneyDetail': '0',
               'direction': arrival_ID,
               'format': 'json',}
        self._header = {'Authorization': 'Bearer ' + token}
        # Get request
        self._r = requests.get(url = self._url_short, headers = self._header, params = self._payload)
        self._tram_data = self._r.json()
        #print(self._tram_data)
        
        trams = []
        # Store desired information in list
        for i in range(len(self._tram_data['DepartureBoard']['Departure'])):
            try:
                trams.append({'number': self._tram_data['DepartureBoard']['Departure'][i]['sname'],
                              'direction': self._tram_data['DepartureBoard']['Departure'][i]['direction'],
                              'time': self.get_diff_minutes(self._tram_data['DepartureBoard']['Departure'][i]['rtTime']),
                              'color': self._tram_data['DepartureBoard']['Departure'][i]['fgColor']})
            except KeyError as ex: # For some reason 'rtTime' does not alwas exist
                trams.append({'number': self._tram_data['DepartureBoard']['Departure'][i]['sname'],
                              'direction': self._tram_data['DepartureBoard']['Departure'][i]['direction'],
                              'time': self.get_diff_minutes(self._tram_data['DepartureBoard']['Departure'][i]['time']),
                              'color': self._tram_data['DepartureBoard']['Departure'][i]['fgColor']})




        # Sort list after departure time
        n = len(trams) - 1
        for j in range(n, 0, -1):
            for i in range(j):
                if trams[i]['time'] > trams[i+1]['time']:
                    trams[i], trams[i+1] = trams[i+1], trams[i]
                n = n - 1

        # Select only a certain number of departures to return
        return trams[:nbr_of_deps]



if __name__ == "__main__":
    # Creates API
    api = API_VT()
    # Retrieves auth token for future use
    token = api.retrieve_token()
    # From station
    from_station = '9021014004490000'
    # To station. Can be leaved blank if all departures are wanted
    to_station = '9021014004945000'
    # Disregards departures less then time_offset minutes away
    time_offset = 7
    # Decides how many (max) departures that are returned
    number_departs = 5
    # Retrieves departures
    trams = api.retrieve_trams(token, from_station, to_station, time_offset, number_departs)

    # Print information about departures
    for i in range(len(trams)):
        print(trams[i]['number'] + '\t' +
              trams[i]['direction'] + '\t' +
              str(trams[i]['time']) + '\t' +
              trams[i]['color'])




