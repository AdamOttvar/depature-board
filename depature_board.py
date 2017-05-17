UPPER_DEPATURE = "Redbergsplatsen"
UPPER_DEPATURE_ID = "9021014005460000"

UPPER_ARRIVAL = "Östra Sjukhuset"
UPPER_ARRIVAL_ID = "9021014007880000"

LOWER_DEPATURE = "Olskrokstorget"
LOWER_DEPATURE_ID = "9021014005160000"

#LOWER_ARRIVAL = "Brunnsparken"
#LOWER_ARRIVAL_ID = "9021014001760000"

LOWER_ARRIVAL = "Svingeln"
LOWER_ARRIVAL_ID = "9021014006480000"

NBR_DEPARTURES = 4
TIME_OFFSET = 6
CLOCK_SIZE = 50

import datetime
from tkinter import *

from tram_GUI import *
from vasttrafik_API import *

class DEPARTURE_BOARD:
    """ Class for creating a departure board

    """
    def __init__(self, api, nbrOfDepartures):
        self.api = api
        self.nbrOfDep = nbrOfDepartures
        self.root = Tk()
        self.root.title("Departure Board")
        # Clock Frame
        self.clockTime = datetime.datetime.now()
        self.clock = StringVar()
        self.clock.set(self.clockTime.strftime('%H:%M'))
        self.clockFrame = Frame(self.root, bg = "black")
        self.clockFrame.pack(side="top", fill="both")
        self.clockLabel = Label(self.clockFrame,
                                textvariable=self.clock,
                                font=("default",50),
                                bg = "black",
                                fg="white")
        self.clockLabel.pack(side="top", fill="both", expand=True, pady=10)

        # So that fullscreen can be toggled
        self.root.bind("<F11>", self.fullscreen_toggle)
        self.root.bind("<Escape>", self.fullscreen_cancel)
        
        # Upper Title
        self.upperTitleFrame = Frame(self.root, bg = "black")
        self.upperTitleFrame.pack(side="top", fill="both")
        self.upperTitleRow = TitleRow(self.upperTitleFrame, UPPER_DEPATURE, UPPER_ARRIVAL)

        # Upper Content
        self.upperContentFrame = Frame(self.root, bg = "black")
        self.upperContentFrame.pack(side="top", fill="both", expand=True)

        # Lower Title
        self.lowerTitleFrame = Frame(self.root, bg = "black")
        self.lowerTitleFrame.pack(side="top", fill="both")
        self.lowerTitleRow = TitleRow(self.lowerTitleFrame, LOWER_DEPATURE, LOWER_ARRIVAL)

        # Lower Content
        self.lowerContentFrame = Frame(self.root, bg = "black")
        self.lowerContentFrame.pack(side="top", fill="both", expand=True)

    def fullscreen_toggle(self, event="none"):
        self.root.focus_set()
        self.root.attributes("-fullscreen", True)
        self.root.wm_attributes("-topmost", 1)

    def fullscreen_cancel(self, event="none"):
        self.root.attributes("-fullscreen", False)
        self.root.wm_attributes("-topmost", 0)
        self.centerWindow()

    def centerWindow(self):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        w = sw*0.7
        h = sh*0.7
        x = (sw-w)/2
        y = (sh-h)/2
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

    def update_clock(self):
        self.clockTime = datetime.datetime.now()
        self.clock.set(self.clockTime.strftime('%H:%M'))
        # Update clock every second
        self.root.after(1000, self.update_clock)

    def create_board(self):
        self.token = self.api.retrieve_token()
        self.upperTrams = self.api.retrieve_trams(self.token, UPPER_DEPATURE_ID, UPPER_ARRIVAL_ID, TIME_OFFSET)
        self.lowerTrams = self.api.retrieve_trams(self.token, LOWER_DEPATURE_ID, LOWER_ARRIVAL_ID, TIME_OFFSET)

        for i in range(self.nbrOfDep):
            TramRow(self.upperContentFrame,
                    self.upperTrams[i]['number'],
                    self.upperTrams[i]['direction'],
                    self.upperTrams[i]['time'])

            TramRow(self.lowerContentFrame,
                    self.lowerTrams[i]['number'],
                    self.lowerTrams[i]['direction'],
                    self.lowerTrams[i]['time'])

        self.fullscreen_toggle()
        # Start updating the clock
        self.update_clock()
        # Update trams every 30 seconds
        self.root.after(30000, self.update_board)

    def update_board(self):
        # Clear frames
        for child in self.upperContentFrame.winfo_children():
            child.destroy()
                
        for child in self.lowerContentFrame.winfo_children():
            child.destroy()

        self.create_board()       


# Create connection to Västtrafik API
api = API_VT()
# Create the board
board = DEPARTURE_BOARD(api,NBR_DEPARTURES)
board.create_board()
# Start infinite loop
board.root.mainloop()


