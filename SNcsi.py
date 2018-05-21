haircolor = {"Black": "CCAGCAATCGC", "Brown": "GCCAGTGCCG", "Blonde": "TTAGCTATCGC"}
faceshape = {"Square": "GCCACGG", "Round": "ACCACAA", "Oval": "AGGCCTCA"}
eyecolor = {"Blue": "TTGTGGTGGC", "Green": "GGGAGGTGGC", "Brown": "AAGTAGTGAC"}
gender = {"Female": "TGAAGGACCTTC", "Male": "TGCAGGAACTTC"}
race = {"White": "AAAACCTCA", "Black": "CGACTACAG", "Asian": "CGCGGGCCG"}
thief = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
eva = {"Gender": "Female", "Race": "White", "Hair Color": "Blonde", "Eye Color": "Blue", "Face Shape": "Oval"}
larisa = {"Gender": "Female", "Race": "White", "Hair Color": "Brown", "Eye Color": "Brown", "Face Shape": "Oval"}
matej = {"Gender": "Male", "Race": "White", "Hair Color": "Black", "Eye Color": "Blue", "Face Shape": "Oval"}
miha = {"Gender": "Male", "Race": "White", "Hair Color": "Brown", "Eye Color": "Green", "Face Shape": "Square"}
suspect = {}
a = 0
b = True
guilty = False

print("DNA Test")
while True:
    a = input("Please choose your suspect\n1. Eva\n2. Larisa\n3. Matej\n4. Miha\n5. Enter your suspect's information\n")
    if a == 1:
        suspect = eva
    elif a == 2:
        suspect = larisa
    elif a == 3:
        suspect = matej
    elif a == 4:
        suspect = miha
    elif a == 5:
        print "Please enter your information."
        suspect["Gender"] = raw_input("Gender: ")
        suspect["Race"] = raw_input("Race: ")
        suspect["Hair Color"] = raw_input("Hair Color: ")
        suspect["Eye Color"] = raw_input("Eye Color: ")
        suspect["Face Shape"] = raw_input("Face Shape: ")

    for key, value in haircolor.items():
        if (key in suspect.values()) and (value in thief):
            for key, value in faceshape.items():
                if (key in suspect.values()) and (value in thief):
                    for key, value in eyecolor.items():
                        if (key in suspect.values()) and (value in thief):
                            for key, value in gender.items():
                                if (key in suspect.values()) and (value in thief):
                                    for key, value in race.items():
                                        if (key in suspect.values()) and (value in thief):
                                            guilty = True


    if guilty == True:
        print "The suspect is guilty!"
        break
    else:
        b = raw_input("The suspect is innocent!\nTry again? (Y/N): ")
        if b == ("N"):
            break