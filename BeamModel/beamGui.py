from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from singStruct import Sig, SigCol
import numpy as np

root = Tk()
root.title("Beam Model")

sUnit = "N"
mUnit = "Nm"
dUnit = "m"
lst = []
# m1 = Sig(0,-2,-160)
# r1 = Sig(0,-1,80)
# uS1 = Sig(3,0,-20)
# uS2 = Sig(7,0,20)
# m2 = Sig(10,-2,-240)
# lst = [m1, r1, uS1, uS2, m2]
# t = np.linspace(0, 10, 1000)
uCol = SigCol(lst)
inOpt = ["Force", "Moment", "Uniform Load"]
unitOpt = ["N", "Nm"]
disOpt = ["m", "ft"]

def update():
    global t, uCol
    figure = plt.Figure(figsize=(7, 7), dpi=100)
    shear = figure.add_subplot(211)
    shear.plot(t, list(map(uCol.integF, t)))
    shear.set_xlabel("Location (" + dUnit + ")")
    shear.set_ylabel("Shear ("+sUnit+")")
    moment = figure.add_subplot(212)
    moment.plot(t, list(map(uCol.integS, t)))
    moment.set_xlabel("Location (" + dUnit + ")")
    moment.set_ylabel("Moment (" + mUnit+")")
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().grid(row=1, column=0)

def addInput():
    global inOpt, unitOpt, disOpt, topFrame
    top = Toplevel()
    top.title("Add Input")
    topFrame = LabelFrame(top, text="Add Input", padx=5, pady=5)
    topFrame.pack(padx=10, pady=10)
    itype = StringVar()
    itype.set("Select Input Type")
    drop = OptionMenu(topFrame, itype, *inOpt)
    drop.grid(row=0, column=0, columnspan=2)
    label = Label(topFrame, text="Value:")
    label.grid(row=1, column=0, columnspan=2)
    val = Entry(topFrame)
    val.grid(row=2, column=0)
    utype = StringVar()
    utype.set("Unit")
    drop = OptionMenu(topFrame, utype, *unitOpt)
    drop.grid(row=2, column=1)
    label2 = Label(topFrame, text="Location:")
    label2.grid(row=3, column=0, columnspan=2)
    disV = Entry(topFrame)
    disV.grid(row=4, column=0)
    dtype = StringVar()
    dtype.set("Unit")
    drop = OptionMenu(topFrame, dtype, *disOpt)
    drop.grid(row=4, column=1)
    btn = Button(top, text="Submit", command=lambda:[addSig(itype.get(),int(val.get()),list(map(int,disV.get().split('-')))), top.destroy()])
    btn.pack()

def addSig(strI, valI, disI):
    if strI == inOpt[0]:
        temp = [Sig(disI[0], -1, valI)]
    elif strI == inOpt[1]:
        temp = [Sig(disI[0], -2, valI)]
    elif strI == inOpt[2]:
        temp = [Sig(disI[0], 0, valI), Sig(disI[1], 0, -1 * valI)]
    else:
        print('invalid input type')
        return
    uCol.addSig(temp)

frame = LabelFrame(root, text="Simulation Inputs",padx=5, pady=5)
frame.grid(row=0,column=0)

add_btn = Button(frame, text="Add", command=addInput)
add_btn.grid(row = 0, column = 0)

update_btn = Button(frame, text="Update", command=update)
update_btn.grid(row = 0, column = 1)

figure = plt.Figure(figsize=(7, 7), dpi=100)
shear = figure.add_subplot(211)
shear.set_xlabel("Location (" + dUnit + ")")
shear.set_ylabel("Shear ("+sUnit+")")
moment = figure.add_subplot(212)
moment.set_xlabel("Location (" + dUnit + ")")
moment.set_ylabel("Moment (" + mUnit+")")
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=1, column=0)

root.mainloop()