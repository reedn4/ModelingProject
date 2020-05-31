from SudokuStruct import Sudoku
from tkinter import *
from math import floor, ceil

# Easy Puzzle
row1 = ['_', 6, '_', '_', 8, 1, 4, 2, '_']
row2 = ['_', 1, 5, '_', 6, '_', 3, 7, 8]
row3 = ['_', '_', '_', 4, '_', 3, '_', 6, '_']
row4 = [1, '_', '_', 6, '_', 4, 8, 3, '_']
row5 = [3, '_', 6, '_', 1, '_', 7, '_', 5]
row6 = [2, 8, '_', 3, 5, '_', '_', '_', 6]
row7 = [8, 3, '_', 9, 4, '_', '_', '_', '_']
row8 = ['_', 7, 2, 1, 3, '_', 9, '_', '_']
row9 = ['_', '_', 9, '_', 2, '_', 6, 1, '_']
easy = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

# Medium Puzzle
row1 = ['_', 6, '_', '_', '_', 4, 7, '_', '_']
row2 = [1, '_', '_', '_', '_', '_', '_', '_', '_']
row3 = [3, 7, '_', 8, 2, '_', '_', 5, '_']
row4 = ['_', 9, 6, '_', '_', '_', '_', 8, 2]
row5 = ['_', 1, 8, '_', '_', '_', '_', 7, '_']
row6 = ['_', '_', '_', 4, 8, 2, '_', '_', 6]
row7 = [5, '_', 1, 2, '_', 6, '_', 9, 4]
row8 = [6, '_', 9, 1, '_', '_', '_', '_', '_']
row9 = ['_', '_', '_', 9, '_', 5, '_', '_', 3]
medium = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

# Hard Puzzle
row1 = ['_', '_', '_', '_', '_', '_', 1, '_', '_']
row2 = ['_', '_', 2, '_', 9, '_', '_', '_', '_']
row3 = [4, 7, 9, 1, '_', 2, '_', '_', '_']
row4 = ['_', '_', '_', 8, '_', '_', 2, 6, 9]
row5 = ['_', 2, '_', '_', '_', 9, '_', '_', 8]
row6 = ['_', 9, '_', 2, '_', '_', 7, 3, '_']
row7 = [9, '_', '_', '_', '_', 7, '_', '_', 5]
row8 = [6, '_', '_', 9, 1, '_', '_', '_', '_']
row9 = [2, '_', 4, 6, 8, '_', '_', 7, 1]
hard = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

# Expert Puzzle
row1 = [8, '_', '_', '_', '_', '_', 3, '_', 4]
row2 = ['_', 4, '_', '_', '_', 1, 7, '_', '_']
row3 = [2, '_', '_', 4, 7, '_', '_', '_', '_']
row4 = [4, 2, '_', '_', '_', '_', '_', '_', '_']
row5 = ['_', 1, '_', '_', '_', 2, '_', 7, '_']
row6 = ['_', '_', 3, '_', 9, '_', '_', '_', 5]
row7 = ['_', '_', '_', 6, 8, 5, '_', '_', '_']
row8 = ['_', '_', 8, '_', '_', '_', 1, 2, '_']
row9 = ['_', '_', '_', '_', '_', 9, '_', '_', 3]
expert = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

row1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
row2 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
row3 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
row4 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
row5 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
row6 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
row7 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
row8 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
row9 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
blank = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

# Choose your puzzle: easy, medium, hard, expert, blank
sud = Sudoku(hard)

sVal = 0
root = Tk()
root.title("Sudoku")
manual = True

def addNum(r, c):
    global sVal, sButtons, manual
    if manual and sVal > 0:
        if sVal in sud.guess[r][c]:
            sud.fillCell(r, c, sVal)

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
    global nButtons, oFrame
    nButtons += [Button(oFrame, text=str(c + 1), command=lambda: setNum(c+1), height=3, width=6)]
    nButtons[-1].grid(row=0, column=c, padx=3, pady=3)

def createGL(r, c):
    global gLabels, topFrame
    temp = sud.guess[r][c]
    strT = ''
    if isinstance(temp, list):
        for n in range(1, 10):
            strT += '  '
            if n in temp:
                strT += str(n)
            else:
                strT += '  '
            if n%3 == 0 and n < 9:
                strT +=' \n'
        gLabels[r] += [Label(topFrame, text=strT, bd=2, relief='solid', bg='gray80', height=4, width=8)]
        gLabels[r][c].grid(row=r, column=c)
    else:
        gLabels[r] += [Label(topFrame, text=strT, bd=2, relief='solid', bg='gray25', height=4, width=8)]
        gLabels[r][c].grid(row=r, column=c)


def showGuess():
    global topFrame, gLabels
    top = Toplevel()
    topFrame = LabelFrame(top, text="Guesses", padx=10, pady=10)
    topFrame.pack()
    gLabels = [[], [], [], [], [], [], [], [], []]
    for r in range(9):
        for c in range(9):
            createGL(r, c)
    sud.gLabels = gLabels

def manO():
    global manual
    manual = True
    manualS.config(state=DISABLED)
    compS.config(state=ACTIVE)
    tFrame.grid_forget()
    oFrame.grid(row=4, column=0, columnspan=3)

def compO():
    global manual
    manual = False
    manualS.config(state=ACTIVE)
    compS.config(state=DISABLED)
    oFrame.grid_forget()
    tFrame.grid(row=4, column=0, columnspan=3)


# Create frame for sudoku board
mainFrame = LabelFrame(root, text="Sudoku", bd=5, padx=5, pady=5, labelanchor='n')
mainFrame.pack(padx=40, pady=20)

optFr = LabelFrame(mainFrame, text="Options", padx=5, pady=5)
optFr.grid(row=0, column=0, columnspan=3)
manualS = Button(optFr, text="Manual", command=manO, height=2, width=18, bd=5, state=DISABLED)
manualS.grid(row=0, column=0, padx=5, pady=5)
compS = Button(optFr, text="Computer", command=compO, height=2, width=18, bd=5)
compS.grid(row=0, column=1, padx=5, pady=5)
sGuess = Button(optFr, text="Show Guesses", command=showGuess, height=2, width=18, bd=5)
sGuess.grid(row=0, column=2, padx=5, pady=5)

# Create Sudoku grid
sudFrame = Frame(mainFrame)
sudFrame.grid(row=1, column=0, rowspan=3, columnspan=3, padx=5, pady=5)
sFrame = []
sButtons = [[], [], [], [], [], [], [], [], []]
for m in range(3):
    sFrame += [[]]
    for n in range(3):
        sFrame[m] += [Frame(sudFrame, bd=1, bg='Black')]
        sFrame[m][n].grid(row=m+1, column=n)
        for r in range(3):
            for c in range(3):
                createB(r+m*3, c+n*3)
sud.buttons = sButtons

# Create frame for number guesses
oFrame = LabelFrame(mainFrame, text="Numbers", padx=10, pady=10)
# oFrame.grid(row=4, column=0, columnspan=3)
# Create number buttons
nButtons = []
for c in range(9):
    createOB(c)

pBor = 5
# Create frame for techniques
tFrame = LabelFrame(mainFrame, text="Solution Techniques", padx=5, pady=5)
# tFrame.grid(row=4, column=0, columnspan=3)
# Naked Singles
nakS = Button(tFrame, text="Naked Singles", command=sud.nSing, height=2, width=12, bd=pBor)
nakS.grid(row=0, column=0, padx=2, pady=2)
# Hidden Singles
hidS = Button(tFrame, text="Hidden Singles", command=sud.hSing, height=2, width=12, bd=pBor)
hidS.grid(row=0, column=1, padx=2, pady=2)
# Naked Pairs
nakP = Button(tFrame, text="Naked Pairs", command=sud.nPair, height=2, width=12, bd=pBor)
nakP.grid(row=0, column=2, padx=2, pady=2)
# Pointing Pairs
nakS = Button(tFrame, text="Pointing Pairs", command=sud.pointPair, height=2, width=12, bd=pBor)
nakS.grid(row=0, column=3, padx=2, pady=2)
# Claiming Pairs
nakS = Button(tFrame, text="Claiming Pairs", command=sud.claimPair, height=2, width=12, bd=pBor)
nakS.grid(row=0, column=4, padx=2, pady=2)
# Naked Triples
nakS = Button(tFrame, text="Naked Triples", command=sud.nTriple, height=2, width=12, bd=pBor)
nakS.grid(row=1, column=0, padx=2, pady=2)
# X-Wing
nakS = Button(tFrame, text="X-Wing", command=sud.xWing, height=2, width=12, bd=pBor, state=DISABLED)
nakS.grid(row=1, column=1, padx=2, pady=2)
# Hidden Pairs
nakS = Button(tFrame, text="Hidden Pairs", command=sud.hPair, height=2, width=12, bd=pBor, state=DISABLED)
nakS.grid(row=1, column=2, padx=2, pady=2)
# Naked Quad
nakS = Button(tFrame, text="Naked Quads", command=sud.nQuad, height=2, width=12, bd=pBor, state=DISABLED)
nakS.grid(row=1, column=3, padx=2, pady=2)

if manual:
    oFrame.grid(row=4, column=0, columnspan=3)
else:
    tFrame.grid(row=4, column=0, columnspan=3)

root.mainloop()