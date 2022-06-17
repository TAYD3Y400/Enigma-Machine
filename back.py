# Rewrite a file content
def writeFile(name, strValue):
    file = open(name, 'w')
    file.write(str(strValue))
    file.close()


# Read and return a file content
def readFile(name):
    file = open(name, "r")
    variable = file.read()
    file.close()
    return variable


# Sort the alphabet using the position of the rotor
def sortABC(abc, pos):
    abcAux = []

    for i in range(0, pos - 1):
        abcAux = abcAux + [abc[0]]
        abc = abc[1:]

    abc = abc + abcAux

    return abc


# Sort the alphabet using the position of the rotor
def encryptLetter(letter, rotors):
    letter=letter.lower()
    print("---"+letter)
    print(rotors)
    
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rotor1 = sortABC(abc, rotors[2])
    rotor2 = sortABC(abc, rotors[1])
    rotor3 = sortABC(abc, rotors[0])

    shuffle1 = ['z', 'w', 'q', 'k', 'e', 'x', 'n', 'd', 'r', 'h', 'm', 'g',
                'u', 'o', 't', 'j', 'v', 'l', 'p', 'y', 's', 'i', 'f', 'c', 'b', 'a']
    shuffle1 = sortABC(shuffle1, rotors[2])

    shuffle2 = ['j', 'l', 'f', 'd', 'b', 'a', 'w', 's', 'o', 'k', 'g', 'c',
                'y', 'u', 'q', 'm', 'i', 'e', 't', 'r', 'p', 'z', 'x', 'v', 'n', 'h']
    shuffle2 = sortABC(shuffle2, rotors[1])

    
    shuffle3 = ['q', 'k', 'e', 'n', 'v', 'j', 'b', 'm', 'p', 'h', 'z', 'y',
                'g', 't', 's', 'd', 'a', 'c', 'f', 'i', 'l', 'o', 'r', 'u', 'x', 'w']
    shuffle3 = sortABC(shuffle3, rotors[0])

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

    for pos in range(len(shuffle3)):
        if shuffle3[pos] == rotor3_letter:
            rotor3_letter_pos = pos
            break
        else:
            continue

    rotor2_letter = rotor2[rotor3_letter_pos]

    for pos in range(len(shuffle2)):
        if shuffle2[pos] == rotor2_letter:
            rotor2_letter_pos = pos
            break
        else:
            continue

    rotor1_letter = rotor1[rotor2_letter_pos]

    for pos in range(len(shuffle1)):
        if shuffle1[pos] == rotor1_letter:
            rotor1_letter_pos = pos
            break
        else:
            continue

    encrypted_letter = abc[rotor1_letter_pos]
    print("---"+encrypted_letter+"/n")
    return encrypted_letter



print(encryptLetter("m", [13, 22, 3]))


# Move the rotors position
def addRotors(rotors):
    rotors[0] += 1

    if (rotors[0] > 26):

        rotors[0] = 1
        rotors[1] += 1

        if (rotors[1] > 26):

            rotors[1] = 1
            rotors[2] += 1

            if (rotors[2] > 26):
                rotors[2] = 1

    return rotors