from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image

top=Tk()
top.geometry('1000x600')

def show():
    top.destroy()
    import weel

path="D:/d1c2a1cb08c54d0bdf7a1a67970dbf23.png"
img=ImageTk.PhotoImage(Image.open(path))

l7=Label(top,image=img,)
l7.pack()


l=Label(top,text='Payment Method!',bg='Light Grey',fg='white',font=('Arial 30 bold'))
l.place(x=350,y=20)

r=Radiobutton(top,text='Credit Card(Visa,Master Card)',value=1,font=("Arial 13 bold"))
r.place(x=150,y=100)

e1=Entry(top,font=("Arial 16 bold"))
e1.place(x=420,y=100)

l1=Label(top,text='Expire Date',bg='grey',fg='white',font=('Arial 9 bold'))
l1.place(x=690,y=100)

k=('select','jan/2030','feb/2030','mar/2030','apr/2030','may/2030','june/2030','july/2030','aug/2030','sep/2030','oct/2030','nov/2030','dec/2030')

cb=ttk.Combobox(top,value=k,font=("Arial 7 bold"))
cb.place(x=665,y=120)
cb.current(0)

l2=Label(top,text='CVV',bg='grey',fg='white',font=('Arial 9 bold'))
l2.place(x=840,y=100)

e2=Entry(top,font=("Arial 7 bold"))
e2.place(x=800,y=120)




r=Radiobutton(top,text='Debit Card(Visa,Master Card)',value=1,font=("Arial 13 bold"))
r.place(x=150,y=150)

e3=Entry(top,font=("Arial 16 bold"))
e3.place(x=420,y=150)

l3=Label(top,text='Expire Date',bg='grey',fg='white',font=('Arial 9 bold'))
l3.place(x=690,y=150)

k=('select','jan/2030','feb/2030','mar/2030','apr/2030','may/2030','june/2030','july/2030','aug/2030','sep/2030','oct/2030','nov/2030','dec/2030')

cb=ttk.Combobox(top,value=k,font=("Arial 7 bold"))
cb.place(x=665,y=170)
cb.current(0)

l4=Label(top,text='CVV',bg='grey',fg='white',font=('Arial 9 bold'))
l4.place(x=840,y=150)

e4=Entry(top,font=("Arial 7 bold"))
e4.place(x=800,y=170)


r=Radiobutton(top,text='UPI(Paytm,GPay,PhonePe)',value=2,font=("Arial 13 bold"))
r.place(x=150,y=220)

c1=Checkbutton(top,text='Paytm',font=("Arial 13 bold"))
c1.place(x=400,y=220)

c2=Checkbutton(top,text='GPay',font=("Arial 13 bold"))
c2.place(x=500,y=220)

c3=Checkbutton(top,text='PhonePe',font=("Arial 13 bold"))
c3.place(x=600,y=220)

b4=Button(top,text='Proceed',bg='grey',fg='white',font=('Arial 15 bold'),command=show)
b4.place(x=450,y=300)
top.config(bg='grey')
top.mainloop()