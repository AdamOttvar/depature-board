UPPER_DEPATURE = "Redbergsplatsen"
UPPER_ARRIVAL = "Östra Sjukhuset"
LOWER_DEPATURE = "Olskrokstorget"
LOWER_ARRIVAL = "Svingeln"


import datetime
from tkinter import *

from tram_GUI import *


root = Tk()
root.title("Departure Board")

# Upper Title
upperTitleFrame = Frame(root, bg = "black")
upperTitleFrame.pack(side="top", fill="both")
upperTitleRow = TitleRow(upperTitleFrame, UPPER_DEPATURE, UPPER_ARRIVAL)

# Upper Content
upperContentFrame = Frame(root, bg = "black")
upperContentFrame.pack(side="top", fill="both", expand=True)
upperContentRow1 = TramRow(upperContentFrame, "1", "Östra sjukhuset", "12:34")
upperContentRow2 = TramRow(upperContentFrame, "1", "Östra sjukhuset", "12:34")

# Lower Title
lowerTitleFrame = Frame(root, bg = "black")
lowerTitleFrame.pack(side="top", fill="both")
lowerTitleLabel = TitleRow(lowerTitleFrame, LOWER_DEPATURE, LOWER_ARRIVAL)

# Lower Content
lowerContentFrame = Frame(root, bg = "black")
lowerContentFrame.pack(side="top", fill="both", expand=True)
lowerContentRow1 = TramRow(lowerContentFrame, "8", "Frölunda", "13:37")
lowerContentRow2 = TramRow(lowerContentFrame, "8", "Frölunda", "13:37")


def update_time():
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
    root.after(2000, update_time)

root.after(0, update_time)
root.mainloop()


