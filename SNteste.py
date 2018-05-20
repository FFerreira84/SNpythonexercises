def findchars(char1, char2):
    strlist = ["Lucky", "Taco", "Cena"]
    return((char1 and char2) in str(strlist))



c = "Y"
while c == "Y" or "yes":
    a = raw_input("Insert the first letter: ")
    b = raw_input("Insert the second letter: ")
    print(findchars(a,b))
    c = raw_input("Try again? (Y/N): ")