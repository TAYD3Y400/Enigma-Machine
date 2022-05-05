from tkinter import *
from back import *

root= Tk()

def main():
    rotors = eval(readFile('rotors.txt'))

    fitRotors(rotors)

    encryptButton = Button (root, text="Encrypt", command=lambda: encrypt(rotors))
    encryptButton.grid(row= 0, column= 1)

def fitRotors(rotors):
    
    rotor1Label = Label(root, text=rotors[0])
    rotor2Label = Label(root, text=rotors[1])
    rotor3Label = Label(root, text=rotors[2])

    rotor1Label.grid(row= 1, column= 0)
    rotor2Label.grid(row= 1, column= 1)
    rotor3Label.grid(row= 1, column= 2)

def encrypt(rotors):

    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    rotors=addRotors(rotors)
    writeFile('rotors.txt',rotors)

    fitRotors(rotors)

    return rotors

main()
                
root.mainloop() 