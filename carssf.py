from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
top=Tk()
top.geometry("1000x600")


path="D:/car1.jpg"
img=ImageTk.PhotoImage(Image.open(path))

l7=Label(top,image=img)
l7.pack()

def insert():
    k=e1.get()
    k2=e2.get()
    k3=e3.get()
    k4=e4.get()
    k5=e5.get()
    k6=int(e6.get())
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='india123',db='car')
    cur=db.cursor()
    s="insert into audi value('%s','%s','%s','%s','%s','%s')"%(k,k2,k3,k4,k5,k6)
    result=cur.execute(s)
    if(result>0):
        messagebox.showinfo("Result","your record insert successfully")
    else:
        messagebox.showinfo("Result", "your record not insert successfully")
    db.commit()

def login():
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='india123',db='car')
    cur=db.cursor()
    cur.execute("select * from audi where Name=%s and Password=%s",(e1.get(),e6.get()))
    row=cur.fetchone()

    if row==None:
        messagebox.showerror("Error","Invalid username and password")
    else:
        top.destroy()
        import Booking_Portal

l=Label(top,text='Car Booking',bg='teal',fg='black',font=("Arial 30 bold"))
l.place(x=400,y=120)

l2=Label(top,text='Name',bg='teal',fg='black',font=("Arial 20 bold"))
l2.place(x=200,y=200)

e1=Entry(top,font=("Arial 20 bold"))
e1.place(x=400,y=200)

l3=Label(top,text='Age',bg='teal',fg='black',font=("Arial 20 bold"))
l3.place(x=200,y=250)

e2=Entry(top,font=("Arial 20 bold"))
e2.place(x=400,y=250)

l4=Label(top,text='Gender',bg='teal',fg='black',font=("Arial 20 bold"))
l4.place(x=200,y=300)

e3=Entry(top,font=("Arial 20 bold"))
e3.place(x=400,y=300)

l5=Label(top,text='Location',bg='teal',fg='black',font=("Arial 20 bold"))
l5.place(x=200,y=350)

e4=Entry(top,font=("Arial 20 bold"))
e4.place(x=400,y=350)

l6=Label(top,text='Phone_N0',bg='teal',fg='black',font=("Arial 20 bold"))
l6.place(x=200,y=400)

e5=Entry(top,font=("Arial 20 bold"))
e5.place(x=400,y=400)

l7=Label(top,text='Password',bg='teal',fg='black',font=("Arial 20 bold"))
l7.place(x=200,y=450)

e6=Entry(top,font=("Arial 20 bold"))
e6.place(x=400,y=450)

b1=Button(top,text='Submit',font=('Arial 14 bold'),command=insert)
b1.place(x=400,y=500)

'''b2=Button(top,text='Delete',font=('Arial 14 bold'),command=delete)
b2.place(x=485,y=450)'''

b2=Button(top,text='login',font=('Arial 14 bold'),command=login)
b2.place(x=500,y=500)



top.config(bg='grey')
top.mainloop()