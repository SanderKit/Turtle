from tkinter import *
import time

#akna seaded
aken = Tk()
aken.title('Taani lipp')
aken.iconbitmap('favicon.ico')
aken.geometry("1000x1000")

#Lõuendi loomine
canvas = Canvas(aken, width=1000, height=1000, bg="white")
canvas.pack(pady=20)

#Kujundi loomine
canvas.create_rectangle(0, 170, 200, 20, fill='red')
canvas.create_line(0, 100, 300, 100, fill="white", width=25)
canvas.create_line(100, 0, 100, 200, fill="white", width=25)

#Pilt
#pildi lisamine
minu_pilt = PhotoImage(file='pastry1.png')
canvas.create_image(0, 300, anchor=NW, image=minu_pilt)

aken.mainloop()
canvas.mainloop()