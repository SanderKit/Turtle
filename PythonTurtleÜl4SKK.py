#Sander Kulma
#18.01.2021
#IT20

from tkinter import *

#akna seaded
aken = Tk()
aken.title('Sander Kulma')
aken.configure(background='black')
aken.iconbitmap('favicon.ico')
aken.resizable(0, 0)

#tekst
lorem = 'Sander Kulma\nIT20\n2021'
tekst = Label(aken, text=lorem, justify=CENTER, foreground="red", background="black", font="Tahoma 16 bold italic")
tekst.pack(pady=30, padx=30)
aken.pack()
aken.mainloop()




