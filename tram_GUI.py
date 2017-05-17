# Module for creating tram GUI
FONT_SIZE_TITLE = 40
FONT_SIZE_TRAM = 30
PADDING_X = 10
PADDING_Y = 10

from tkinter import *


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
    the tram number, tram direction and tram departure time.
    Prepared for function that could update labels with StringVar
    """
    def __init__(self, tram_frame, tram_number, tram_direction, tram_dep_time):
        """ Initiates the strings as StringVar in order to be easy to update.
        """
        self.frame = Frame(tram_frame, bg = "black")
        self.number = StringVar()
        self.direction = StringVar()
        self.depTime = StringVar()

        self.number.set(tram_number)
        self.direction.set(tram_direction)
        self.depTime.set(tram_dep_time)
        self.numberLabel = Label(self.frame, textvariable=self.number, font=("default",FONT_SIZE_TRAM), bg = "black", fg="white")
        self.numberLabel.pack(side="left", fill="y", padx=PADDING_X)
        self.descrLabel = Label(self.frame, textvariable=self.direction, font=("default",FONT_SIZE_TRAM), bg = "black", fg="white")
        self.descrLabel.pack(side="left", fill="both")
        self.timeLabel = Label(self.frame, textvariable=self.depTime, font=("default",FONT_SIZE_TRAM), bg = "black", fg="white")
        self.timeLabel.pack(side="right", fill="y", padx=PADDING_X)

        self.frame.pack(side="top", fill="both", pady=PADDING_Y)
