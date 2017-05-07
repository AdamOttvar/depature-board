import datetime
from tkinter import *

UPPER_DEPATURE = "Redbergsplatsen"
UPPER_ARRIVAL = "Östra Sjukhuset"
LOWER_DEPATURE = "Olskrokstorget"
LOWER_ARRIVAL = "Svingeln"
FONT_SIZE_TITLE = 40
FONT_SIZE_TRAM = 30

class TitleRow:
    """Class for creating a row with the title och the frame

    The title is "the departure station" + "mot" + "the arrival station"
    """
    def __init__(self, title_frame, dep_station, arr_station):
        self.frame = title_frame
        self.departure = dep_station
        self.arrival = arr_station

        self.titleLabel = Label(self.frame, text=self.departure + " mot " + self.arrival,
                        font=("default",30), bg = "black", fg="white")
        self.titleLabel.pack(side="top", fill="both", expand=True, pady=10)


class TramRow:
    """Class for creating a row with tram information

    Tram information is stored in a frame with three labels that store
    the tram number, tram description and tram departure time.
    """
    def __init__(self, tram_frame, tram_number, tram_description, tram_dep_time):
        self.frame = Frame(tram_frame, bg = "black")
        self.number = StringVar()
        self.descr = StringVar()
        self.depTime = StringVar()


        self.number.set(tram_number)
        self.descr.set(tram_description)
        self.depTime.set(tram_dep_time)
        self.numberLabel = Label(self.frame, textvariable=self.number, font=("default",FONT_SIZE_TRAM), bg = "black", fg="white")
        self.numberLabel.pack(side="left", fill="y", padx=10)
        self.descrLabel = Label(self.frame, textvariable=self.descr, font=("default",FONT_SIZE_TRAM), bg = "black", fg="white")
        self.descrLabel.pack(side="left", fill="both")
        self.timeLabel = Label(self.frame, textvariable=self.depTime, font=("default",FONT_SIZE_TRAM), bg = "black", fg="white")
        self.timeLabel.pack(side="right", fill="y", padx=10)

        self.frame.pack(side="top", fill="both", pady=10)
        

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


