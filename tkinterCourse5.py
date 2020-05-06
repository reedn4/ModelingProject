from tkinter import *
import math

root = Tk()
root.title('Calculator')

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

calTemp = 0

def button_click(number):
    global calTemp
    if isinstance(number,int):
        current = e.get()
        e.delete(0,END)
        e.insert(0, str(current)+str(number))
    elif number == 'c':
        e.delete(0,END)
        calTemp = 0
    else:
        calTemp += int(e.get())
        if number == '+':
            e.delete(0,END)
        else:
            e.delete(0,END)
            e.insert(0,str(calTemp))
            calTemp = 0
        
        
    
    return

temp = Button(root,text='0',padx=40,pady=20,command=lambda: button_click(0))
temp.grid(row=4,column=0)
temp = Button(root,text='1',padx=40,pady=20,command=lambda: button_click(1))
temp.grid(row=1,column=0)
temp = Button(root,text='2',padx=40,pady=20,command=lambda: button_click(2))
temp.grid(row=1,column=1)
temp = Button(root,text='3',padx=40,pady=20,command=lambda: button_click(3))
temp.grid(row=1,column=2)
temp = Button(root,text='4',padx=40,pady=20,command=lambda: button_click(4))
temp.grid(row=2,column=0)
temp = Button(root,text='5',padx=40,pady=20,command=lambda: button_click(5))
temp.grid(row=2,column=1)
temp = Button(root,text='6',padx=40,pady=20,command=lambda: button_click(6))
temp.grid(row=2,column=2)
temp = Button(root,text='7',padx=40,pady=20,command=lambda: button_click(7))
temp.grid(row=3,column=0)
temp = Button(root,text='8',padx=40,pady=20,command=lambda: button_click(8))
temp.grid(row=3,column=1)
temp = Button(root,text='9',padx=40,pady=20,command=lambda: button_click(9))
temp.grid(row=3,column=2)
temp = Button(root,text='+',padx=39,pady=20,command=lambda: button_click('+'))
temp.grid(row=5,column=0)
temp = Button(root,text='clear',padx=80,pady=20,command=lambda: button_click('c'))
temp.grid(row=4,column=1,columnspan=2)
temp = Button(root,text='=',padx=89,pady=20,command=lambda: button_click('='))
temp.grid(row=5,column=1,columnspan=2)


#Button1 = Button(root,text="1",padx=20,pady=20,command=myClick)
#,fg='blue',bg='red',padx=50,pady=50,state=DISABLED)
#can use hex color codes

#myButton.pack()

root.mainloop()
