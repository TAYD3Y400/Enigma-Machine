import time
from email import message
from logging import root
import tkinter
from tkinter import *
from back import *
from functools import partial
from typing import List


root1 = Tk()
root= Tk()

message = ""



r1Label = Label(root1, text="R1")
r2Label = Label(root1, text="R2")
r3Label = Label(root1, text="R3")

r1Label.grid(row=1, column=1)
r2Label.grid(row=1, column=2)
r3Label.grid(row=1, column=3)

entryMessage1 = Entry(root1, width=1, bg="white", fg="black")
entryMessage2 = Entry(root1, width=1, bg="white", fg="black")
entryMessage3 = Entry(root1, width=1, bg="white", fg="black")

entryMessage1.grid(row=2, column=1)
entryMessage2.grid(row=2, column=2)
entryMessage3.grid(row=2, column=3)


def main():
    rotors = []
rr = tkinter.Button(root1, text="Ok", bg="green", command= lambda: rotorsReady ([entryMessage1.get(),entryMessage2.get(), entryMessage3.get()])).grid(row=2, column=4)
 

def rotorsReady(rotors):  
    if (rotors[0]!=NONE) and (rotors[1]!=NONE) and (rotors[2]!=NONE):
        fitRotors(rotors)
        keyboard()
        light_panel()
        root1.destroy()
        

def fitRotors(rotors):

    r1Label = Label(root, text="R1")
    r2Label = Label(root, text="R2")
    r3Label = Label(root, text="R3")

    r1Label.grid(row=1, column=1)
    r2Label.grid(row=1, column=2)
    r3Label.grid(row=1, column=3)

    rotor1Label = Label(root, text=rotors[0])
    rotor2Label = Label(root, text=rotors[1])
    rotor3Label = Label(root, text=rotors[2])

    rotor1Label.grid(row=2, column=1)
    rotor2Label.grid(row=2, column=2)
    rotor3Label.grid(row=2, column=3)


def light_panel():
    bQ = tkinter.Button(root, text="Q", bg="#494949").grid(row=4, column=1)
    bW = tkinter.Button(root, text="W", bg="#494949").grid(row=4, column=2)
    bE = tkinter.Button(root, text="E", bg="#494949").grid(row=4, column=3)
    bR = tkinter.Button(root, text="R", bg="#494949").grid(row=4, column=4)
    bT = tkinter.Button(root, text="T", bg="#494949").grid(row=4, column=5)
    bY = tkinter.Button(root, text="Y", bg="#494949").grid(row=4, column=6)
    bU = tkinter.Button(root, text="U", bg="#494949").grid(row=4, column=7)
    bI = tkinter.Button(root, text="I", bg="#494949").grid(row=4, column=8)
    bO = tkinter.Button(root, text="O", bg="#494949").grid(row=4, column=9)
    bP = tkinter.Button(root, text="P", bg="#494949").grid(row=4, column=10)

    bA = tkinter.Button(root, text="A", bg="#494949").grid(row=5, column=1)
    bS = tkinter.Button(root, text="S", bg="#494949").grid(row=5, column=2)
    bD = tkinter.Button(root, text="D", bg="#494949").grid(row=5, column=3)
    bF = tkinter.Button(root, text="F", bg="#494949").grid(row=5, column=4)
    bG = tkinter.Button(root, text="G", bg="#494949").grid(row=5, column=5)
    bH = tkinter.Button(root, text="H", bg="#494949").grid(row=5, column=6)
    bJ = tkinter.Button(root, text="J", bg="#494949").grid(row=5, column=7)
    bK = tkinter.Button(root, text="K", bg="#494949").grid(row=5, column=8)
    bL = tkinter.Button(root, text='L', bg="#494949").grid(row=5, column=9)

    bZ = tkinter.Button(root, text='Z', bg="#494949").grid(row=6, column=1)
    bX = tkinter.Button(root, text='X', bg="#494949").grid(row=6, column=2)
    bC = tkinter.Button(root, text='C', bg="#494949").grid(row=6, column=3)
    bV = tkinter.Button(root, text='V', bg="#494949").grid(row=6, column=4)
    bB = tkinter.Button(root, text='B', bg="#494949").grid(row=6, column=5)
    bN = tkinter.Button(root, text='N', bg="#494949").grid(row=6, column=6)
    bM = tkinter.Button(root, text='M', bg="#494949").grid(row=6, column=7)

def keyboard():

    label = Label(root).grid(row=7)
    bQ = tkinter.Button(root, text="Q", command=partial(keyboard_letter, "Q", 4, 1)).grid(row=8, column=1)
    bW = tkinter.Button(root, text="W", command=partial(keyboard_letter, "W", 4, 2)).grid(row=8, column=2)
    bE = tkinter.Button(root, text="E", command=partial(keyboard_letter, "E", 4, 3)).grid(row=8, column=3)
    bR = tkinter.Button(root, text="R", command=partial(keyboard_letter, "R", 4, 4)).grid(row=8, column=4)
    bT = tkinter.Button(root, text="T", command=partial(keyboard_letter, "T", 4, 5)).grid(row=8, column=5)
    bY = tkinter.Button(root, text="Y", command=partial(keyboard_letter, "Y", 4, 6)).grid(row=8, column=6)
    bU = tkinter.Button(root, text="U", command=partial(keyboard_letter, "U", 4, 7)).grid(row=8, column=7)
    bI = tkinter.Button(root, text="I", command=partial(keyboard_letter, "I", 4, 8)).grid(row=8, column=8)
    bO = tkinter.Button(root, text="O", command=partial(keyboard_letter, "O", 4, 9)).grid(row=8, column=9)
    bP = tkinter.Button(root, text="P", command=partial(keyboard_letter, "P", 4, 10)).grid(row=8, column=10)

    bA = tkinter.Button(root, text="A", command=partial(keyboard_letter, "A", 5, 1)).grid(row=9, column=1)
    bS = tkinter.Button(root, text="S", command=partial(keyboard_letter, "S", 5, 2)).grid(row=9, column=2)
    bD = tkinter.Button(root, text="D", command=partial(keyboard_letter, "D", 5, 3)).grid(row=9, column=3)
    bF = tkinter.Button(root, text="F", command=partial(keyboard_letter, "F", 5, 4)).grid(row=9, column=4)
    bG = tkinter.Button(root, text="G", command=partial(keyboard_letter, "G", 5, 5)).grid(row=9, column=5)
    bH = tkinter.Button(root, text="H", command=partial(keyboard_letter, "H", 5, 6)).grid(row=9, column=6)
    bJ = tkinter.Button(root, text="J", command=partial(keyboard_letter, "J", 5, 7)).grid(row=9, column=7)
    bK = tkinter.Button(root, text="K", command=partial(keyboard_letter, "K", 5, 8)).grid(row=9, column=8)
    bL = tkinter.Button(root, text='L', command=partial(keyboard_letter, "L", 5, 9)).grid(row=9, column=9)

    noneButton = tkinter.Button(root, text="  ").grid(row=9, column=10)

    bZ = tkinter.Button(root, text='Z', command=partial(keyboard_letter, "Z", 6, 1)).grid(row=10, column=1)
    bX = tkinter.Button(root, text='X', command=partial(keyboard_letter, "X", 6, 2)).grid(row=10, column=2)
    bC = tkinter.Button(root, text='C', command=partial(keyboard_letter, "C", 6, 3)).grid(row=10, column=3)
    bV = tkinter.Button(root, text='V', command=partial(keyboard_letter, "V", 6, 4)).grid(row=10, column=4)
    bB = tkinter.Button(root, text='B', command=partial(keyboard_letter, "B", 6, 5)).grid(row=10, column=5)
    bN = tkinter.Button(root, text='N', command=partial(keyboard_letter, "N", 6, 6)).grid(row=10, column=6)
    bM = tkinter.Button(root, text='M', command=partial(keyboard_letter, "M", 6, 7)).grid(row=10, column=7)

    noneButton = tkinter.Button(root,text="  ").grid(row=10, column=8)
    noneButton = tkinter.Button(root, text="  ").grid(row=10, column=9)

    tkinter.Button(root, text="OK", bg="#17B919", command=partial(keyboard_letter, "OK")).grid(row=10, column=10)

def bright_letter(letter, row, column):
    bright_letter = Label(root, text=letter, bg="yellow")
    bright_letter.grid(row=row, column=column)
    root.after(2000, bright_letter_off, letter, row, column)


def bright_letter_off(letter, row, column):
    bright_letter = Label(root, text=letter, bg="#494949")
    bright_letter.grid(row=row, column=column)



def keyboard_letter(letter, row, column):
    letter_encrypted= encryptLetter(letter, #rotors) # falta encriptar

    global message
    message=message+(letter_encrypted)
    print("letra ingresada:" + letter + "encriptada es:" + letter_encrypted)
    fitMessage(message)
    bright_letter(letter_encrypted, row, column)




def fitMessage(message):
    message = Label(root, text=message)

    message.grid(row=2, column=0)


def encrypt(rotors):
    print(entryMessage.get())

    # abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    rotors = addRotors(rotors)
    writeFile('rotors.txt', rotors)
    fitRotors(rotors)

    return rotors


main()

root.mainloop()
