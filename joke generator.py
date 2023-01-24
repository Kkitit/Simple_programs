from tkinter import *
import pyjokes
from googletrans import Translator


def generate():
    joke = pyjokes.get_joke()
    a = transl.translate(joke)
    t.delete('1.0', END)
    t.insert('1.0', a.text)


root = Tk()
root.title('Joke-Joke')
root.geometry('500x300')
root.resizable(width=False, height=False)
transl = Translator()

btn = Button(root, text='Give a joke', font='Arial 16 bold', command=generate)
btn.pack(pady=10)

t = Text(root, font='Arial 16 bold', pady=10, padx=10, wrap=WORD)

t.pack()

root.mainloop()
