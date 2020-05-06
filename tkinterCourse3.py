from tkinter import *

root = Tk()

def myClick():
    myLabel=Label(root,text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root,text="Click Me!",command=myClick)
#,fg='blue',bg='red',padx=50,pady=50,state=DISABLED)
#can use hex color codes

myButton.pack()

root.mainloop()
