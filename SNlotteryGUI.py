import random
import Tkinter
import tkMessageBox

window = Tkinter.Tk()
# Greeting text
greeting = Tkinter.Label(window, text="How many lottery numbers would you like to generate?")
greeting.pack()
# Number of digits to generate
digits = Tkinter.Entry(window)
digits.pack()


# Generate digits
def lotterygame():
    lottery = []
    numbers = int(digits.get())
    while len(lottery) < numbers:
        a = random.randint(1, 50)
        if a not in lottery:
            lottery.append(a)
    result = str(sorted(lottery))

    tkMessageBox.showinfo("Result", result)


# submit button
submit = Tkinter.Button(window, text="Submit", command=lotterygame)  # lotterygame, not lotterygame()
submit.pack()

window.mainloop()
