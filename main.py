from tkinter import *
from back import *

root= Tk()

rotors = eval(readFile('rotors.txt'))

def encrypt():
    global rotors

    rotor1Label = Label(root, text=rotors[0])
    rotor2Label = Label(root, text=rotors[1])
    rotor3Label = Label(root, text=rotors[2])

    rotor1Label.grid(row= 1, column= 0)
    rotor2Label.grid(row= 1, column= 1)
    rotor3Label.grid(row= 1, column= 2)

    rotors=addRotors(rotors)

encryptButton = Button (root, text="Encrypt", command= encrypt)
encryptButton.grid(row= 0, column= 1)
                
root.mainloop()