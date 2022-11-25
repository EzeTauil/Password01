from tkinter import *
import random
import string

def generatePass():
    lst=[]
    for i in range(1,13):
        alphabet_lower=list(string.ascii_lowercase)
        alphabet_upper=list(string.ascii_uppercase)
        alphabet_symbols=list(string.punctuation)
        str=alphabet_lower+alphabet_upper+alphabet_symbols
        character=random.choice(str)
        lst.append(character)
    a="".join(lst)
    print(a) 
    label.config(text=a)


root = Tk()

root.title("Generador de contraseña")
root.geometry("500x500") #ancho por alto 
root.resizable(0,0)

my_button = Button(root,text="Generar",font="arial 15 bold",command=generatePass).pack()
my_label = Label(root,text="").pack()
exit_button = Button(root,text="cerrar",font="arial 15 bold", command=root.destroy).pack()
label=Label(root,text="",font="arial 15 bold")
label.pack()
root.mainloop()
