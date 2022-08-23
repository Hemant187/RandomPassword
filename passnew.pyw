from tkinter import *

def passgen(event):
    import random
    from string import ascii_letters

    letters = ''
    for i in ascii_letters:
        letters += i

    num = '0123456789'
    spl = '!@#$%^&*()_'

    total = num + spl + letters
    res = ''
    try:
        passvar.get() == int
        pass_len = int(passvar.get())

        for i in range(pass_len):
            res += random.choice(total)
        resultvar.set(res)

    except Exception :
        resultvar.set("Enter integer!")


def savepass(event):
    from csv import writer
    with open('password.csv', 'a') as file:
        obj = writer(file)
        obj.writerow([appvar.get(), resultvar.get()])


root = Tk()
root.geometry('443x350')
root.title('Password Generator')

Label(text="Password Length", font='lucida 10 bold').grid(row=0, column=1)

passvar = StringVar()
passval = Entry(root, textvariable=passvar, font='lucida 15')
passval.grid(row=0, column=2)


b = Button(text='Generate Password')
b.grid(row=1, column=2, pady=10)
b.bind("<Button-1>", passgen)


Label(text="Generated Password", font='lucida 10 bold').grid(row=5, column=1)

resultvar = StringVar()
resultval = Entry(root, textvariable=resultvar, font='lucida 15 bold')
resultval.grid(row=5, column=2)

Label(text="Want to add app name", font='lucida 10 bold').grid(
    row=6, column=1, pady=50)

appvar = StringVar()
appval = Entry(root, textvariable=appvar, font='lucida 15 bold')
appval.grid(row=6, column=2)


b2 = Button(text='Save Password')
b2.grid(row=7, column=2, pady=10)
b2.bind("<Button-1>", savepass)


root.mainloop()
