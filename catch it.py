from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk


def two():
    messagebox.showinfo(' ', 'Ha-ha-ha')
    quit()


def motionMouse(event):
    p.place(x=random.randint(0,500), y=random.randint(0,500))


root = Tk()
root.geometry('600x600')
root.title('catch me')
root.resizable(width=False,height=False)
root['bg'] = 'white'

image = ImageTk.PhotoImage(file="img/fu.png")
p = Button(root, image=image)
p.place(x=170, y=100)
p.bind('<Enter>', motionMouse)
btn2 = Button(root, text='Сдаюсь!',font='Arial 20 bold', command=two)
btn2.place(x=350,y=100)


root.mainloop()