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
                       'client_id': r'UZh58bJpsfGzYTTbme74KOmKjMAa',
                       'client_secret': r'MLk3r4ONnBTel0q6U3yqRkoDytca'}
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

    def retrieve_trams(self, token, departure_ID, arrival_ID, time_offset):
        """ Method for accessing departures

        Returns departures from a certain stopID to another stopID, given a token and
        how much of a time offest that should be added
        """
        self._tram_datetime = datetime.datetime.now()+datetime.timedelta(minutes = time_offset)
        self._tram_date = self._tram_datetime.strftime('%Y-%m-%d')
        self._tram_time = self._tram_datetime.strftime('%H:%M')
        self._url_short = r'https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard?id=' + departure_ID
        self._payload = {'date': self._tram_date,
               'time': self._tram_time,
               'timeSpan': '30',
               'maxDeparturesPerLine': '2',
               'needJourneyDetail': '0',
               'direction': arrival_ID,
               'format': 'json',}
        self._header = {'Authorization': 'Bearer ' + token}
        self._r = requests.get(url = self._url_short, headers = self._header, params = self._payload)
        self._tram_data = self._r.json()

        trams = []
        for i in range(len(self._tram_data['DepartureBoard']['Departure'])):
            trams.append({'number': self._tram_data['DepartureBoard']['Departure'][i]['sname'],
                                'direction': self._tram_data['DepartureBoard']['Departure'][i]['direction'],
                                'time': self._tram_data['DepartureBoard']['Departure'][i]['rtTime']})
        return trams



if __name__ == "__main__":
    api = API_VT()
    token = api.retrieve_token()
    trams = api.retrieve_trams(token, '9021014005460000', '9021014007880000', 8)
    print(trams)




