# for use tkinter module
from tkinter import *

# Create a function for generate random password
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

# save appname and password in a csv file
def savepass(event):
    from csv import writer
    with open('password.csv', 'a') as file:
        obj = writer(file)
        obj.writerow([appvar.get(), resultvar.get()])


root = Tk()
# give gui width and height
root.geometry('443x350')
# for gui title
root.title('Password Generator')

# print Password Length in gui
Label(text="Password Length", font='lucida 10 bold').grid(row=0, column=1)

# create a string variable
passvar = StringVar()
# create a entry box for password lenght
passval = Entry(root, textvariable=passvar, font='lucida 15')
passval.grid(row=0, column=2)


# create a button for generate password
b = Button(text='Generate Password')
b.grid(row=1, column=2, pady=10)
b.bind("<Button-1>", passgen)


# print Generated password in gui
Label(text="Generated Password", font='lucida 10 bold').grid(row=5, column=1)

# create a stringvariable named resultvar
resultvar = StringVar()
# create a box where generated password will appear 
resultval = Entry(root, textvariable=resultvar, font='lucida 15 bold')
resultval.grid(row=5, column=2)

# print want to add app name option on gui
Label(text="Want to add app name", font='lucida 10 bold').grid(
    row=6, column=1, pady=50)

# create a new variable named appvar
appvar = StringVar()
#create a entry box to app name 
appval = Entry(root, textvariable=appvar, font='lucida 15 bold')
appval.grid(row=6, column=2)


# create a button to save app name andpassword in csv file
b2 = Button(text='Save Password')
b2.grid(row=7, column=2, pady=10)
b2.bind("<Button-1>", savepass)


# make loop for gui 
root.mainloop()
