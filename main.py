import tkinter
from tkinter import *
from back import *

root= Tk()

entryMessage = Entry(root, width=20, bg="gray", fg="black")
entryMessage.grid(row= 1, column= 0)

def main():
    rotors = eval(readFile('rotors.txt'))

    fitRotors(rotors)
    light_panel()
    keyborad()


def fitRotors(rotors):

    r1Label = Label(root, text="R1")
    r2Label = Label(root, text="R2")
    r3Label = Label(root, text="R3")

    r1Label.grid(row= 1, column= 1)
    r2Label.grid(row= 1, column= 2)
    r3Label.grid(row= 1, column= 3)
    
    rotor1Label = Label(root, text=rotors[0])
    rotor2Label = Label(root, text=rotors[1])
    rotor3Label = Label(root, text=rotors[2])

    rotor1Label.grid(row= 2, column= 1)
    rotor2Label.grid(row= 2, column= 2)
    rotor3Label.grid(row= 2, column= 3)

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



def keyborad():
    label = Label(root).grid(row=7)
    bQ = tkinter.Button(root, text="Q").grid(row=8, column=1)
    bW = tkinter.Button(root, text="W").grid(row=8, column=2)
    bE = tkinter.Button(root, text="E").grid(row=8, column=3)
    bR = tkinter.Button(root, text="R").grid(row=8, column=4)
    bT = tkinter.Button(root, text="T").grid(row=8, column=5)
    bY = tkinter.Button(root, text="Y").grid(row=8, column=6)
    bU = tkinter.Button(root, text="U").grid(row=8, column=7)
    bI = tkinter.Button(root, text="I").grid(row=8, column=8)
    bO = tkinter.Button(root, text="O").grid(row=8, column=9)
    bP = tkinter.Button(root, text="P").grid(row=8, column=10)

    bA = tkinter.Button(root, text="A").grid(row=9, column=1)
    bS = tkinter.Button(root, text="S").grid(row=9, column=2)
    bD = tkinter.Button(root, text="D").grid(row=9, column=3)
    bF = tkinter.Button(root, text="F").grid(row=9, column=4)
    bG = tkinter.Button(root, text="G").grid(row=9, column=5)
    bH = tkinter.Button(root, text="H").grid(row=9, column=6)
    bJ = tkinter.Button(root, text="J").grid(row=9, column=7)
    bK = tkinter.Button(root, text="K").grid(row=9, column=8)
    bL = tkinter.Button(root, text='L').grid(row=9, column=9)

    bZ = tkinter.Button(root, text='Z').grid(row=10, column=1)
    bX = tkinter.Button(root, text='X').grid(row=10, column=2)
    bC = tkinter.Button(root, text='C').grid(row=10, column=3)
    bV = tkinter.Button(root, text='V').grid(row=10, column=4)
    bB = tkinter.Button(root, text='B').grid(row=10, column=5)
    bN = tkinter.Button(root, text='N').grid(row=10, column=6)
    bM = tkinter.Button(root, text='M').grid(row=10, column=7)


def fitMessage(message):

    message = Label(root, text=message)
    
    message.grid(row= 2, column= 0)


def encrypt(rotors):

    print(entryMessage.get())

    #abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    rotors = addRotors(rotors)
    writeFile('rotors.txt', rotors)
    fitRotors(rotors)

    return rotors

main()

root.mainloop() 