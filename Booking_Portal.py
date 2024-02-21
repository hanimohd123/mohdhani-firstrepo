from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
top=Tk()
top.geometry("1000x600")
def show():
    top.destroy()
    import dd

def insert():
    k1=cb.get()
    k2=cb1.get()
    k3=cb2.get()
    k4=cb3.get()
    k5=cb5.get()
    k6=int(cb4.get())
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='india123',db='cars')
    cur=db.cursor()
    s="insert into bmw value('%s','%s','%s','%s','%s','%s')"%(k1,k2,k3,k4,k5,k6)
    res=s.fetchall()
    result=cur.execute(s)
    if(result>0):
        messagebox.showinfo("result","your record insert successfully")
    else:
        messagebox.showinfo("result", "your record not insert successfully")
    db.commit()
    res.close()
    db.close()

    res=[result[0] for res in result]
path="D:/audoi.jpg"
img=ImageTk.PhotoImage(Image.open(path))

l7=Label(top,image=img,)
l7.pack()

l=Label(top,text='Welcome to audi showroom',bg='dark red',fg='black',font=("Arial 20 bold"))
l.place(x=300,y=0)

l1=Label(top,text='Book Your Car',bg='brown',fg='black',font=("Arial 20 bold"))
l1.place(x=380,y=80)

l2=Label(top,text='New_Brand',bg='brown',fg='black',font=("Arial 15 bold"))
l2.place(x=300,y=150)

l2=Label(top,text='Budget',bg='brown',fg='black',font=("Arial 15 bold"))
l2.place(x=300,y=200)

e1=('select','Audi A4','Audi A6','Q8 e-tron','Q3')
cb=ttk.Combobox(top,value=e1,font=("Arial 15 bold"))
cb.place(x=410,y=150)
cb.current(0)

e2=('select','10000000','<15999990','<2000000')
cb1=ttk.Combobox(top,value=e2,font=("Arial 15 bold"))
cb1.place(x=410,y=200)
cb1.current(0)

l3=Label(top,text='Ownership',bg='brown',fg='black',font=("Arial 15 bold"))
l3.place(x=300,y=250)

e3=('select','First Owner','Second Owner')
cb2=ttk.Combobox(top,value=e3,font=("Arial 15 bold"))
cb2.place(x=410,y=250)
cb2.current(0)

l3=Label(top,text='Fuel_Type',bg='brown',fg='black',font=("Arial 15 bold"))
l3.place(x=300,y=300)

e4=('select','Petrol','Diesel','CNG')
cb3=ttk.Combobox(top,value=e4,font=("Arial 15 bold"))
cb3.place(x=410,y=300)
cb3.current(0)

l4=Label(top,text='Colours',bg='brown',fg='black',font=("Arial 15 bold"))
l4.place(x=300,y=350)

e5=('select','Red','Green','Yellow','Black','White')

cb5=ttk.Combobox(top,value=e5,font=("Arial 15 bold"))
cb5.place(x=410,y=350)
cb5.current(0)

l4=Label(top,text='Valid DL',bg='brown',fg='black',font=("Arial 15 bold"))
l4.place(x=300,y=400)

e6=('select','Yes','No')
cb4=ttk.Combobox(top,value=e6,font=("Arial 15 bold"))
cb4.place(x=410,y=400)
cb4.current(0)

'''b4=Button(top,text='Submit',bg='white',fg='black',font=('Arial 30 bold'),command=show)
b4.place(x=400,y=450)'''


b5=Button(top,text='Login',bg='white',fg='black',font=('Arial 30 bold'),command=insert)
b5.place(x=400,y=450)

top.config(bg='green')
top.mainloop()