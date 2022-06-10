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

#Sort the alphabet using the position of the rotor
def sortABC(abc, pos):

    abcAux=[]

    for i in range(0, pos-1):
        abcAux = abcAux + [abc[0]]
        abc=abc[1:]
    
    abc=abc+abcAux

    return abc

#Sort the alphabet using the position of the rotor
def encryptLetter(letter, rotors):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
    rotor3 = sortABC(abc, rotors[2])
    rotor2 = sortABC(abc, rotors[1])
    rotor1 = sortABC(abc, rotors[0])
    print(rotor3)

    rotor3_letter = ""
    rotor2_letter = ""
    rotor1_letter = ""

    rotor3_letter_pos = 0
    rotor2_letter_pos = 0
    rotor1_letter_pos = 0

    # Third rotor
    for pos in range(len(abc)):
        if abc[pos] == letter:
            rotor3_letter_pos = pos
            break
        else:
            continue
    rotor3_letter = rotor3[rotor3_letter_pos]

    # Second rotor
    for pos in range(len(abc)):
        if abc[pos] == rotor3_letter:
            rotor2_letter_pos = pos
            break
        else:
            continue
    rotor2_letter = rotor2[rotor2_letter_pos]


    # First rotor
    for pos in range(len(abc)):
        if abc[pos] == rotor2_letter:
            rotor1_letter_pos = pos
            break
        else:
            continue
    rotor1_letter = rotor1[rotor1_letter_pos]
    return rotor1_letter

    # reflector_pos = 0
    # for pos in range(len(abc)):
    #     if abc[pos] == rotor1_letter:
    #         reflector_pos = 25 - pos


    # # Reflection
    # reflected_letter = abc[reflector_pos]

    # # First rotor again with reflected letter
    # for pos in range(len(abc)):
    #     if abc[pos] == reflected_letter:
    #         rotor1_letter_pos = pos
    #         break
    #     else:
    #         continue
    # rotor1_letter = rotor1[rotor1_letter_pos]

    # # Second rotor with reflected letter
    # for pos in range(len(abc)):
    #     if abc[pos] == rotor1_letter:
    #         rotor2_letter_pos = pos
    #         break
    #     else:
    #         continue
    # rotor2_letter = rotor2[rotor2_letter_pos]

    # for pos in range(len(abc)):
    #     if abc[pos] == rotor2_letter:
    #         rotor3_letter_pos = pos
    #         break
    #     else:
    #         continue

    # return_letter = rotor3[rotor3_letter_pos]


    # return return_letter//


print(encryptLetter("b", [23,1,6]))


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