from tkinter import *

root = Tk()

e = Entry(root)
          #,borderwidth = 10, width=50, bg='blue', fg='white')
e.pack()
e.insert(0, 'Enter Your Name')

def myClick():
    hello = 'Hello ' + e.get()
    myLabel=Label(root,text=hello)
    myLabel.pack()

myButton = Button(root,text="Submit",command=myClick)
#,fg='blue',bg='red',padx=50,pady=50,state=DISABLED)
#can use hex color codes

myButton.pack()

root.mainloop()
