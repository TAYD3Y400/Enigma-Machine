from tkinter import *
from back import *

root= Tk()

entryMessage = Entry(root, width=20, bg="gray", fg="black")
entryMessage.grid(row= 1, column= 0)

def main():
    rotors = eval(readFile('rotors.txt'))

    fitRotors(rotors)


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

def fitMessage(message):

    message = Label(root, text=message)
    
    message.grid(row= 2, column= 0)


def encrypt(rotors):

    print(entryMessage.get())

    #abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    rotors=addRotors(rotors)
    writeFile('rotors.txt',rotors)
    fitRotors(rotors)

    return rotors

main()
                
root.mainloop() 