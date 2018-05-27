restmenu = {}

print "Please enter your menu for today."
while True:
    dish = raw_input("Enter the name of the dish: ")
    price = raw_input("Enter the price of the dish: ")
    restmenu[dish] = price
    new = raw_input("Would you like to enter another dish? ")
    if new == ("no" or "N" or "n"):
        break

menufile = open("menu.txt", "w+")
menufile.write("Today's menu:\n")
for key, value in restmenu.items():
    print key + " - " + value
    menufile.write(key + " - " + value + "\n")
menufile.close()
