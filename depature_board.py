UPPER_DEPATURE = "Redbergsplatsen"
UPPER_DEPATURE_ID = "9021014005460000"

UPPER_ARRIVAL = "Östra Sjukhuset"
UPPER_ARRIVAL_ID = "9021014007880000"

LOWER_DEPATURE = "Olskrokstorget"
LOWER_DEPATURE_ID = "9021014005160000"

LOWER_ARRIVAL = "Brunnsparken"
LOWER_ARRIVAL_ID = "9021014001760000"

TIME_OFFSET = 6


import datetime
from tkinter import *

from tram_GUI import *
from vasttrafik_API import *


root = Tk()
root.title("Departure Board")

api = API_VT()
token = api.retrieve_token()
upperTrams = api.retrieve_trams(token, UPPER_DEPATURE_ID, UPPER_ARRIVAL_ID, TIME_OFFSET)
lowerTrams = api.retrieve_trams(token, LOWER_DEPATURE_ID, LOWER_ARRIVAL_ID, TIME_OFFSET)

#print(upperTrams)
#print(lowerTrams)

# Upper Title
upperTitleFrame = Frame(root, bg = "black")
upperTitleFrame.pack(side="top", fill="both")
upperTitleRow = TitleRow(upperTitleFrame, UPPER_DEPATURE, UPPER_ARRIVAL)

# Upper Content
upperContentFrame = Frame(root, bg = "black")
upperContentFrame.pack(side="top", fill="both", expand=True)
upperContentRow1 = TramRow(upperContentFrame, upperTrams[0]['number'], upperTrams[0]['direction'], upperTrams[0]['time'])
upperContentRow2 = TramRow(upperContentFrame, upperTrams[1]['number'], upperTrams[1]['direction'], upperTrams[1]['time'])

# Lower Title
lowerTitleFrame = Frame(root, bg = "black")
lowerTitleFrame.pack(side="top", fill="both")
lowerTitleLabel = TitleRow(lowerTitleFrame, LOWER_DEPATURE, LOWER_ARRIVAL)

# Lower Content
lowerContentFrame = Frame(root, bg = "black")
lowerContentFrame.pack(side="top", fill="both", expand=True)
lowerContentRow1 = TramRow(lowerContentFrame, lowerTrams[0]['number'], lowerTrams[0]['direction'], lowerTrams[0]['time'])
lowerContentRow2 = TramRow(lowerContentFrame, lowerTrams[1]['number'], lowerTrams[1]['direction'], lowerTrams[1]['time'])


def update_time():
    """
    _tram_datetime = datetime.datetime.now()+datetime.timedelta(minutes = 0)
    _tram_time = _tram_datetime.strftime('%H:%M')
    upperContentRow1.depTime.set(_tram_time)
    _tram_datetime = datetime.datetime.now()+datetime.timedelta(minutes = 1)
    _tram_time = _tram_datetime.strftime('%H:%M')
    upperContentRow2.depTime.set(_tram_time)
    _tram_datetime = datetime.datetime.now()+datetime.timedelta(minutes = 2)
    _tram_time = _tram_datetime.strftime('%H:%M')
    lowerContentRow1.depTime.set(_tram_time)
    _tram_datetime = datetime.datetime.now()+datetime.timedelta(minutes = 3)
    _tram_time = _tram_datetime.strftime('%H:%M')
    lowerContentRow2.depTime.set(_tram_time)
    """
    root.after(2000, update_time)


root.after(0, update_time)
root.mainloop()


