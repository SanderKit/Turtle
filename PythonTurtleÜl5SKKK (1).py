#Sander Kulma
#Ülesanne 05
#18.01.2021

from tkinter import *

#akna seaded
aken = Tk()
aken.title('KM Kalkulaator')
aken.iconbitmap('favicon.ico')
aken.geometry("400x200")

kmta = Label(aken, text="Hind k2ibemaksuta: ")
kmta.grid(row=0, column=0)

sisestus = Entry(aken)
sisestus.grid(row=0,column=1,sticky=W)

def naita_valikut():
    var.get()
    print(var.get())

kmm = Label(aken, text="K2ibemaksumäär: ")
kmm.grid(row=1, column=0, sticky=W)

var = IntVar()

valikukast = Radiobutton(aken,text="9%", variable=var, value=9, command=naita_valikut)
valikukast.grid(column=1, row=1,sticky=W)
valikukast1 = Radiobutton(aken,text="20%", variable=var, value=20, command=naita_valikut)
valikukast1.grid(row=2, column=1,sticky=W)

aaaaaa=Label(aken,text=" ")
aaaaaa.grid(row=3)

km = Label(aken, text="Käibemaks: ")
km.grid(row=4,column=0, sticky=W)

kmga = Label(aken, text="Hind käibemaksuga: ")
kmga.grid(row=5,column=0, sticky=W)

def arvutus():
    km= int(sisestus.get())
    lp = int(var.get()) / 100
    km1 = km * lp
    km2 = km1 + km
    vastus.config(text=km1)
    vastus1.config(text=km2)
    
vastus = Label(aken, text="€")
vastus.grid(row=4,column=1)

vastus1 = Label(aken, text="€")
vastus1.grid(row=5,column=1)

nupp1 = Button(aken, text="OK", width=10, command=arvutus)
nupp1.grid(row=6,column=1, sticky=E)

aken.mainloop()
