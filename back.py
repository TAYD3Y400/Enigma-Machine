#Rewrite a file content
def writeFile (name, strValue):
    file = open(name, 'w')
    file.write (strValue)
    file.close()

#Read and return a file content
def readFile(name):

    file = open(name, "r")
    variable = file.read()
    file.close()
    return variable

#Move the rotors position
def addRotors(rotors):

    rotors[2]+=1

    if (rotors[2]>26):

        rotors[2]=0
        rotors[1]+=1

        if (rotors[1]>26):

            rotors[1]=0
            rotors[0]+=1

            if (rotors[0]>26):

                rotors[0]=0
    
    return rotors