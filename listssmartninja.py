print "Welcome to the TODO task management program."

lista = []


while True:
    lista2 = []
    task = raw_input("Please enter a TODO task: ")
    print "Your task is: " + task
    lista.append(task)

    new = raw_input("Would you like to enter new task? (yes/no) ")

    if new == "no":
        break

print "All tasks: %s" % lista
print "END"