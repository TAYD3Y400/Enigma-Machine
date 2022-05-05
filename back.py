#Rewrite a file content
def writeFile (name, strValue):
    file = open(name, 'w')
    file.write (str(strValue))
    file.close()

#Read and return a file content
def readFile(name):

    file = open(name, "r")
    variable = file.read()
    file.close()
    return variable

#Sort the alphabetic using the position of the rotor
def sortABC(abc, pos):

    abcAux=[]

    for i in range(0, pos-1):
        abcAux = abcAux + [abc[0]]
        abc=abc[1:]
        print (abc[0])
    
    abc=abc+abcAux

    return abc


#Move the rotors position
def addRotors(rotors):

    rotors[2]+=1

    if (rotors[2]>26):

        rotors[2]=1
        rotors[1]+=1

        if (rotors[1]>26):

            rotors[1]=1
            rotors[0]+=1

            if (rotors[0]>26):

                rotors[0]=1
    
    return rotors