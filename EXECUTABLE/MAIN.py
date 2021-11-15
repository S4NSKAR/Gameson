from tkinter import *
from tkinter import messagebox
import os

def dev():
    messagebox.showinfo('Creators : ', 'Developed by : \nSanskar \nRishabh \nGourav \nDevanshu')

def egg_game():
    os.startfile("dist\\Egg-Catcher\\Egg-Catcher.exe")

def caterpillar_game():
    os.startfile("dist\\Caterpillar\\Caterpillar.exe")

top = Tk()
top.geometry("730x450")
top.title('GAMESON')
c = Canvas(top, height = 600, width = 800, bg='black', bd=0)
c.create_text(180,5, text='WELCOME TO GAMESON!',  font=('Megrim', 24, 'bold'), fill='yellow',activefill="light blue", anchor=NW)
img = PhotoImage(file  = "Media\\bg.png")
c.create_image(0, 50, image=img, anchor=NW)
Button(text="Egg Catcher", command=egg_game, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=18, y = 120)
Button(text="Caterpillar", command=caterpillar_game, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=18, y = 220)
Button(text="Developers", command=dev, activebackground='green', highlightcolor='yellow', bd=6, bg='black', fg='white', font=('Roboto', 14, 'bold'), relief='raised',height=1, width=15).place(x=500, y = 380)
c.pack()
top.mainloop()