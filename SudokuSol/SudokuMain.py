from SudokuStruct import Sudoku
from tkinter import *
from math import floor, ceil

row1 = [1, 5, '_', '_', 4, 2, '_', '_', 6]
row2 = [2, 7, 4, 5, 6, '_', '_', 1, '_']
row3 = ['_', '_', 6, '_', '_', 7, 4, '_', 2]
row4 = ['_', 1, '_', '_', '_', '_', '_', 4, '_']
row5 = ['_', '_', '_', '_', 5, '_', '_', '_', '_']
row6 = ['_', 6, '_', 4, '_', 3, 1, 9, '_']
row7 = ['_', 2, '_', 6, '_', 5, 9, '_', '_']
row8 = [9, 8, 5, '_', 3, '_', '_', 6, '_']
row9 = ['_', 4, '_', 2, 1, 9, 8, 3, '_']
lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

row1 = ['_', '_', '_', '_', '_', '_', '_', 8, '_']
row2 = [6, 8, '_', 4, 7, '_', '_', 2, '_']
row3 = ['_', 1, 9, 5, '_', 8, 6, 4, 7]
row4 = ['_', 6, '_', 9, '_', '_', '_', '_', 4]
row5 = [3, 4, 2, 6, 8, '_', '_', '_', '_']
row6 = [1, 9, '_', '_', 5, '_', 8, 3, '_']
row7 = ['_', '_', '_', 7, 2, '_', 4, '_', 3]
row8 = ['_', '_', 6, '_', '_', 5, '_', 1, '_']
row9 = ['_', '_', 3, 8, 9, 1, 5, '_', '_']
lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

row1 = ['_', 8, '_', 9, '_', '_', '_', 5, '_']
row2 = [4, '_', '_', 6, 5, '_', 9, 1, 3]
row3 = ['_', '_', 5, 4, '_', '_', '_', '_', '_']
row4 = [1, '_', 2, '_', 6, 5, '_', '_', '_']
row5 = [7, '_', 4, '_', '_', '_', 5, '_', 8]
row6 = ['_', '_', '_', '_', '_', '_', '_', '_', 2]
row7 = [3, '_', '_', '_', '_', 1, '_', '_', 6]
row8 = [8, 7, '_', '_', '_', '_', '_', 4, '_']
row9 = ['_', 5, '_', '_', 4, '_', 8, '_', 1]
lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

row1 = ['_', '_', '_', '_', '_', '_', 8, '_', '_']
row2 = ['_', '_', '_', '_', '_', 2, '_', 7, 4]
row3 = ['_', '_', 7, '_', '_', 8, '_', 2, '_']
row4 = ['_', '_', 8, 3, 4, 5, '_', 9, '_']
row5 = ['_', '_', 3, '_', '_', 6, '_', '_', 1]
row6 = [6, '_', '_', 8, '_', '_', '_', '_', '_']
row7 = ['_', 2, 4, 9, '_', 3, 6, '_', 8]
row8 = ['_', 1, 9, '_', '_', '_', '_', '_', '_']
row9 = ['_', '_', '_', '_', 5, 4, 9, '_', '_']
lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
#
# row1 = ['_', 4, 8, 3, 5, 1, '_', '_', 7]
# row2 = ['_', '_', 1, 6, 9, 7, '_', '_', '_']
# row3 = ['_', 7, '_', '_', 2, '_', 1, 3, '_']
# row4 = ['_', '_', 2, '_', '_', 3, '_', '_', '_']
# row5 = [7, '_', '_', 2, '_', '_', '_', 8, 3]
# row6 = [8, '_', 3, 9, 7, '_', 4, 1, 2]
# row7 = ['_', '_', 6, 5, 4, 2, '_', 7, 9]
# row8 = ['_', 2, '_', '_', '_', '_', 5, '_', '_']
# row9 = [5, '_', '_', '_', '_', 9, '_', '_', 1]
# lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
# row1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# row2 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# row3 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# row4 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# row5 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# row6 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# row7 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# row8 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# row9 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
# lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

sud = Sudoku(lst)
# print(sud.display())
# print(sud.displayG())
# sud.nTriple()
# print(sud.displayG())
sVal = 0

root = Tk()
root.title("Sudoku")
manual = True

def addNum(r, c):
    global sVal, sButtons, manual
    if manual:
        if sVal in sud.guess[r][c]:
            sud.fillCell(r, c, sVal)
            # sButtons[r][c].config(text = str(sVal))

def setNum(num):
    global sVal
    sVal = num

def createB(r, c):
    global sButtons, sFrame
    if isinstance(sud.known[r][c], int):
        sButtons[r] += [Button(sFrame[floor(r/3)][floor(c/3)], text=str(sud.known[r][c]), cursor='hand2', height=3, width=6)]
    else:
        sButtons[r] += [
            Button(sFrame[floor(r / 3)][floor(c / 3)], text="", command=lambda: addNum(r, c), cursor='hand2', height=3, width=6)]
    sButtons[r][c].grid(row=r, column=c)

def createOB(c):
    global nButtons
    nButtons += [Button(oFrame, text=str(c + 1), command=lambda: setNum(c+1), height=3, width=6)]
    nButtons[-1].grid(row=0, column=c)

def showGuess():
    return

# Create frame for sudoku board
mainFrame = LabelFrame(root, text="Sudoku", bd=5, padx=10, pady=10, labelanchor='n')
mainFrame.pack()

optFr = LabelFrame(mainFrame, text="Options", padx=10, pady=10)
optFr.grid(row=0, column=0, columnspan=3)
sGuess = Button(optFr, text="Show Guesses", command=showGuess, height=2, width=18, bd=5)
sGuess.grid(row=0, column=0)
sGuess = Button(optFr, text="Show Guesses", command=showGuess, height=2, width=18, bd=5)
sGuess.grid(row=0, column=1)
sGuess = Button(optFr, text="Show Guesses", command=showGuess, height=2, width=18, bd=5)
sGuess.grid(row=0, column=2)

# Create Sudoku grid
sFrame = []
sButtons = [[], [], [], [], [], [], [], [], []]
for m in range(3):
    sFrame += [[]]
    for n in range(3):
        sFrame[m] += [Frame(mainFrame, bd=1, bg='Black')]
        sFrame[m][n].grid(row=m+1, column=n)
        for r in range(3):
            for c in range(3):
                createB(r+m*3, c+n*3)
sud.buttons = sButtons

# Create frame for number guesses
oFrame = LabelFrame(mainFrame, text="Numbers", padx=5, pady=5)
# oFrame.grid(row=4, column=0, columnspan=3)
# Create number buttons
nButtons = []
for c in range(9):
    createOB(c)

pBor = 5
# Create frame for techniques
tFrame = LabelFrame(mainFrame, text="Solution Techniques", padx=5, pady=5)
tFrame.grid(row=4, column=0, columnspan=3)
# Naked Singles
nakS = Button(tFrame, text="Naked Singles", command=sud.nSing, height=2, width=18, bd=pBor)
nakS.grid(row=0, column=0)
# Hidden Singles
hidS = Button(tFrame, text="Hidden Singles", command=sud.hSing, height=2, width=18, bd=pBor)
hidS.grid(row=0, column=1)
# Naked Pairs
nakP = Button(tFrame, text="Naked Pairs", command=sud.nPair, height=2, width=18, bd=pBor)
nakP.grid(row=0, column=2)
# Pointing Pairs
nakS = Button(tFrame, text="Pointing Pairs", command=sud.pointPair, height=2, width=18, bd=pBor)
nakS.grid(row=1, column=0)
# Claiming Pairs
nakS = Button(tFrame, text="Claiming Pairs", command=sud.claimPair, height=2, width=18, bd=pBor)
nakS.grid(row=1, column=1)
# Naked Triples
nakS = Button(tFrame, text="Naked Triples", command=sud.nTriple, height=2, width=18, bd=pBor)
nakS.grid(row=1, column=2)
# X-Wing
nakS = Button(tFrame, text="X-Wing", command=sud.xWing, height=2, width=18, bd=pBor, state=DISABLED)
nakS.grid(row=2, column=0)
# Hidden Pairs
nakS = Button(tFrame, text="Hidden Pairs", command=sud.hPair, height=2, width=18, bd=pBor, state=DISABLED)
nakS.grid(row=2, column=1)
# Naked Quad
nakS = Button(tFrame, text="Naked Quads", command=sud.nQuad, height=2, width=18, bd=pBor, state=DISABLED)
nakS.grid(row=2, column=2)


root.mainloop()