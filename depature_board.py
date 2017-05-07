from tkinter import *
UPPER_DEPATURE = "Redbergsplatsen"
UPPER_ARRIVAL = "Östra Sjukhuset"
LOWER_DEPATURE = "Olskrokstorget"
LOWER_ARRIVAL = "Svingeln"


root = Tk()
root.title("Departure Board")

UpperTitleFrame = Frame(root, bg = "black")
UpperTitleFrame.pack(side="top", fill="both")
UpperTitleLabel = Label(UpperTitleFrame, text=UPPER_DEPATURE + " mot " + UPPER_ARRIVAL,
                        font=("default",30), bg = "black", fg="white")
UpperTitleLabel.pack(side="top", fill="both", expand=True)

UpperContentFrame = Frame(root, bg = "black")
UpperContentFrame.pack(side="top", fill="both")
UpperContentNumber = Label(UpperContentFrame, text="1", font=("default",30), bg = "black", fg="white")
UpperContentNumber.pack(side="left", fill="y")
UpperContentDescr = Label(UpperContentFrame, text="Östra Sjukhuset", font=("default",30), bg = "black", fg="white")
UpperContentDescr.pack(side="left", fill="both")
UpperContentTime = Label(UpperContentFrame, text="12:34", font=("default",30), bg = "black", fg="white")
UpperContentTime.pack(side="right", fill="y")

LowerTitleFrame = Frame(root, bg = "black")
LowerTitleFrame.pack(side="top", fill="both")
LowerTitleLabel = Label(LowerTitleFrame, text=LOWER_DEPATURE + " mot " + LOWER_ARRIVAL,
                        font=("default",30), bg = "black", fg="white")
LowerTitleLabel.pack(side="top", fill="both", expand=True)

LowerContentFrame = Frame(root, bg = "black")
LowerContentFrame.pack(side="top", fill="both")
LowerContentNumber = Label(LowerContentFrame, text="8", font=("default",30), bg = "black", fg="white")
LowerContentNumber.pack(side="left", fill="y")
LowerContentDescr = Label(LowerContentFrame, text="Frölunda", font=("default",30), bg = "black", fg="white")
LowerContentDescr.pack(side="left", fill="both")
LowerContentTime = Label(LowerContentFrame, text="13:37", font=("default",30), bg = "black", fg="white")
LowerContentTime.pack(side="right", fill="y")

root.mainloop()
