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

# eva = ["Female", "White", "Blonde", "Blue", "Oval"]
# larisa = ["Female", "White", "Brown", "Brown", "Oval"]
# matej = ["Male", "White", "Black", "Blue", "Oval"]
# miha = ["Male", "White", "Brown", "Green", "Square"]

a = "string"

for key, value in eva.items():
    result = a.find(value)
    print result
