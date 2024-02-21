'''from tkinter import *
from tkinter import messagebox
from tkinter import ttk
top=Tk()
top.geometry('1000x600')

l=Label(top,text='Welcome',bg='green',fg='white',font=('Arial 30 bold'))
l.place(x=400,y=20)

top.config(bg='green')
top.mainloop()'''

#Date 17/01/24
#Radio button
'''from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import wallpaper
from PIL import ImageTk,Image

top=Tk()
top.geometry('1000x600')


def show():
    top.destroy()
    import dd

b4=Button(top,text='Login',bg='yellow',fg='white',font=('Arial 30 bold'),command=show)
b4.place(x=400,y=300)

r=Radiobutton(top,text='male',value=1)
r.place(x=200,y=100)

r2=Radiobutton(top,text='female',value=2)
r2.place(x=200,y=150)

r3=Radiobutton(top,text='other',value=3)
r3.place(x=200,y=200)


top.mainloop()'''



from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import wallpaper
from PIL import ImageTk,Image

top=Tk()
top.geometry('1000x600')

def show():
    top.destroy()
    import carssf
path="D:/thanks2.webp"
img=ImageTk.PhotoImage(Image.open(path))

l7=Label(top,image=img)
l7.pack()

l=Label(top,text='Payment Successfully',bg='purple',fg='white',font=('Arial 20 bold'))
l.place(x=350,y=80)


#l1=Label(top,text='Goto Homepage',bg='grey',fg='white',font=('Arial 30 bold'))
#l1.place(x=350,y=200)

l2=Label(top,text='Thanks for visit',bg='Brown',fg='white',font=('Arial 20 bold'))
l2.place(x=400,y=300)

b4=Button(top,text='Goto Homepage',bg='grey',fg='white',font=('Arial 20 bold'),command=show)
b4.place(x=380,y=200)


top.config(bg='green')
top.mainloop()