from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from tkinter import filedialog, messagebox
from dataFram import dataFram
from math import floor, ceil

root = Tk()
root.title("Data Visualization")
dataFiles = []
fileNames = []
plotLst = []
noFileE = 0
ptVar = IntVar()
lnVar = IntVar()
plotR = 0
labLst = []

def load():
    global dataFiles, fileNames, noFileE
    root.filename = filedialog.askopenfilename(title="Select A File", filetype=(("EXCEL files", "*.xlsx"), ("CSV files", "*.csv"), ("TEXT files", "*.txt")))
    response = messagebox.askyesno("", "Does your file contain headers?")
    dataFiles += [dataFram(root.filename, response)]
    fileNames += [str(root.filename).split('/')[-1]]
    loadLab = Label(mainFrame, text=str(len(dataFiles))+" File(s) Loaded", bg='gray90', width=30)
    loadLab.grid(row=2, column=0, columnspan=2, pady=2)
    temp = ''
    for name in fileNames:
        temp += name
        temp += '\n'
    fileLab = Label(mainFrame, text=temp)
    fileLab.grid(row=3, column=0, columnspan=2)
    if noFileE != 0:
        noFileE.pack_forget()
        noFileE = 0

def varSelect(datF, fram, var):
    tIn = fileNames.index(datF.get())
    varL = Label(fram, text="Variable:")
    varL.grid(row=1, column=0, padx=5, pady=5)
    var = OptionMenu(fram, var, *dataFiles[tIn].colNames())
    var.grid(row=1, column=1, padx=5, pady=5)

def delButton(plotIn):
    plotLst.pop(plotIn)
    labLst[plotIn][0].grid_forget()
    labLst[plotIn][1].grid_forget()
    labLst.pop(plotIn)

def addDelBut(frame, plotIn):
    labLst[-1] += [Button(frame, text="Remove", command=lambda: delButton(plotIn))]
    labLst[-1][1].grid(row=plotR, column=1)

def addPlot(title, xVar, yVar):
    global plotLst, top, plotR, labLst
    plotLst += [[title, xVar, yVar, [lnVar.get(), ptVar.get()]]]
    top.destroy()
    temp = "Plot #" + str(len(plotLst)) + ":\nIndependent Variable: " + xVar[1] + " [" + xVar[0].file + "]\nDependent Variable: " + yVar[1] + " [" + yVar[0].file + "]"
    labLst += [[Label(messFrame, text=temp)]]
    labLst[-1][0].grid(row=plotR, column=0)
    addDelBut(messFrame, len(plotLst)-1)
    plotR += 1

def addGraph():
    global noFileE, top
    if len(dataFiles) < 1 and noFileE == 0:
        noFileE = Label(messFrame, text="No data available")
        noFileE.pack()
    elif len(dataFiles) >= 1:
        global ptVar, lnVar
        top = Toplevel()
        top.title("Add Graph")
        topFrame = LabelFrame(top, text="Add Graph", padx=5, pady=5)
        topFrame.pack(padx=10, pady=10)
        titleFram = Frame(topFrame)
        titleFram.grid(row=0, column=0, columnspan=2)
        labelT = Label(titleFram, text="Graph Title: ")
        labelT.grid(row=0, column=0)
        graphT = Entry(titleFram)
        graphT.grid(row=0, column=1)
        # Define independent variable
        xVarF = LabelFrame(topFrame, text="Independent Variable")
        xVarF.grid(row=1, column=0, padx=10, pady=10)
        # Select Data file for independent variable
        datXL = Label(xVarF, text="Data File:")
        datXL.grid(row=0, column=0, padx=5, pady=5)
        datX = StringVar()
        datX.set("Select")
        varX = StringVar()
        varX.set("Select")
        datXS = OptionMenu(xVarF, datX, *fileNames, command=lambda x: [varSelect(datX, xVarF, varX)])
        datXS.grid(row=0, column=1, padx=5, pady=5)
        # Define dependent variable
        yVarF = LabelFrame(topFrame, text="Dependent Variable")
        yVarF.grid(row=1, column=1, padx=10, pady=10)
        # Select Data file for dependent variable
        datYL = Label(yVarF, text="Data File:")
        datYL.grid(row=0, column=0, padx=5, pady=5)
        datY = StringVar()
        datY.set("Select")
        varY = StringVar()
        varY.set("Select")
        datYS = OptionMenu(yVarF, datY, *fileNames, command=lambda x: varSelect(datY, yVarF, varY))
        datYS.grid(row=0, column=1, padx=5, pady=5)
        ptVar.set(0)
        ptC = Checkbutton(topFrame, text='Points', variable=ptVar)
        ptC.grid(row=2, column=0, columnspan=2)
        lnVar.set(0)
        lnC = Checkbutton(topFrame, text='Lines', variable=lnVar)
        lnC.grid(row=3, column=0, columnspan=2)
        # Button to add graph
        addGr = Button(topFrame, text="Add", command=lambda: addPlot(graphT.get(), [dataFiles[fileNames.index(datX.get())], varX.get()], [dataFiles[fileNames.index(datY.get())], varY.get()]))
        addGr.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

def plotWind():
    top = Toplevel()
    top.title("Add Input")
    figure = plt.Figure()
    r = 1
    c = 1
    if len(plotLst) > 1:
        r = 2
        c = ceil(len(plotLst)/2)
    for n in range(len(plotLst)):
        temp = figure.add_subplot(r, c, n+1)
        if bool(plotLst[n][3][0]):
            temp.plot(plotLst[n][1][0].data[plotLst[n][1][1]], plotLst[n][2][0].data[plotLst[n][2][1]])
        if bool(plotLst[n][3][1]):
            temp.scatter(plotLst[n][1][0].data[plotLst[n][1][1]], plotLst[n][2][0].data[plotLst[n][2][1]])
        temp.set_xlabel(plotLst[n][1][1])
        temp.set_ylabel(plotLst[n][2][1])
        temp.set_title(plotLst[n][0])
    canvas = FigureCanvasTkAgg(figure, top)
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, top)
    toolbar.update()
    canvas.get_tk_widget().pack()

mainFrame = Frame(root, padx=10, pady=10, bd=2, relief='solid')
mainFrame.pack(padx=10, pady=10)

title = Label(mainFrame, text="Data Visualization with Python", height=2, width=40, font=40, bg='gray80')
title.grid(row=0, column=0, columnspan=2, pady=10)

typeLab = Label(mainFrame, text="Accepted File types: .csv, .txt, .xlsx")
typeLab.grid(row=1, column=1)
fileBut = Button(mainFrame, text="Add Data File", command=load)
fileBut.grid(row=1, column=0, pady=10)
addG = Button(mainFrame, text="Add Graph", command=addGraph, width=35)
addG.grid(row=4, column=0, columnspan=2)
messFrame = Frame(mainFrame)
messFrame.grid(row=5, column=0, columnspan=2)

createP = Button(root, text="Plot", command=plotWind, height=1, width=8, bd=2)
createP.pack(padx=5, pady=5)

root.mainloop()