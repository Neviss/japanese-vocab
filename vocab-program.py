import pandas as pd
import random as rd
from tkinter import *
import tkinter.font as tkFont

# Display the total number of cards left in cardList
def displayTotal(total):
    # Print total cards left
    totalCardsLeft = Label(totalFrame, text=total, font=totalFont)
    totalCardsLeft.pack()

#Display the current card information
def displayCardInformation(line):
    # Print card information
    blank = Label(frame, text="", font=topFont)
    kana = Label(frame, text=str(line[0]), font=topFont)
    kanji = Label(bottomFrame, text=str(line[1]), font=bottomFont)
    definition = Label(bottomFrame, text=str(line[2]), font=bottomFont)

    blank.pack()
    kana.pack()
    definition.pack(side=BOTTOM)
    kanji.pack(side=BOTTOM)

# Generate a new card
def generateNewCard():
    if total > 0:
        global currentIndex
        currentIndex = rd.randrange(0, total)
        line = cardList[currentIndex]
        displayCardInformation(line)
    elif total == 0:
        line = cardList[0]
        displayCardInformation(line)

# Clear frame
def clearFrame():
    for child in frame.winfo_children():
        child.destroy()

    for child in bottomFrame.winfo_children():
        child.destroy()

    for child in totalFrame.winfo_children():
        child.destroy()

# Event on '<Return' key press
def enterKey(event):
    #print("Enter pressed")
    
    # User knows
    # Clear frame, remove from list, update total, generate new card
    clearFrame()

    global total
    if total > 0:
        del cardList[currentIndex]
        total -= 1

        displayTotal(total)
        generateNewCard()
    else:
        print("No other cards left!")
        Label(frame, text="No other cards left!", font=topFont).pack()

# Event on '<space>' key press
def spaceKey(event):
    #print("Spaecebar pressed")

    # User doesn't know
    # Clear frame and generate new card
    clearFrame()
    generateNewCard()


# Read sheet
df = pd.read_excel('Vocabulary.xlsx', sheet_name='N5 Vocab')

# Create card list and current position
cardList = []
currentIndex = 0

# Make flashcards
for index, row in df.iterrows():
    cardList.append([row["Kana"], row["Kanji"], row["Definition/s"]])

# Calculate total length
total = len(cardList)

#-----------------------------------------------------------------------------
# Tkinter Things

# Create window
master = Tk()
master.title("Japanese Vocabulary Flashcards")

# Frame setup
frame = Frame(master)
frame.pack()
totalFrame = Frame(master)
totalFrame.place(x=0, y=0)
bottomFrame = Frame(master)
bottomFrame.pack(side=BOTTOM)

# Font setup
topFont = tkFont.Font(family="Helvetica", size=128, weight="bold")
totalFont = tkFont.Font(family="Helvetica", size=64, weight="bold")
bottomFont = tkFont.Font(family="Helvetica", size=16, weight="bold")

# Get screen display size
width = master.winfo_screenwidth()
height = master.winfo_screenheight()

# Set geometry size
master.geometry("%dx%d" % (width, height-100))

# Keybinds
master.bind("<Return>", enterKey)
master.bind("<space>", spaceKey)

# Widgets go here
displayTotal(total)
generateNewCard()

# Execute tkinter
master.mainloop()