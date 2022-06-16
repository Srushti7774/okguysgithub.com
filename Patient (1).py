from tkinter import *
from functools import partial
import warnings

def checkPassword(password, cpassword):
    s1 = password.get()
    s2 = cpassword.get()
    if s1 == s2:
        warnings.warn('Match')
    if s1 != s2:
        warnings.warn('Not Match')
def showData(FirstName,LastName,username,mail,password,cpassword,line,city,state,pincode):
    print("FirstName :", FirstName.get())
    print("LastName  :", LastName.get())
    print("username  :", username.get())
    print("Mail  :", mail.get())
    print("password  :", password.get())
    print("Confirm password:", cpassword.get())
    print("line      :", line.get())
    print("city      :", city.get())
    print("state     :", state.get())
    print("pincode   :", pincode.get())
    return

#window
tkWindow = Tk()
tkWindow.geometry('250x300')
tkWindow.title('Patient')



#password label and password entry box
FirstNameLabel = Label(tkWindow,text="FirstName").grid(row=0, column=0)
FirstName = StringVar()
FirstNameEntry = Entry(tkWindow, textvariable=FirstName).grid(row=1, column=1)

#username label and text entry box
LastNameLabel = Label(tkWindow, text="LastName").grid(row=1, column=0)
LastName = StringVar()
LastNameEntry = Entry(tkWindow, textvariable=LastName).grid(row=0, column=1)


usernameLabel = Label(tkWindow, text="User Name").grid(row=2, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=2, column=1)

mailLabel = Label(tkWindow, text="Email Id").grid(row=3, column=0)
mail = StringVar()
mailLabelEntry = Entry(tkWindow, textvariable=mail).grid(row=3, column=1)
#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=4, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=4, column=1)

cpasswordLabel = Label(tkWindow,text="Confirm Password").grid(row=5, column=0)
cpassword = StringVar()
cpasswordEntry = Entry(tkWindow, textvariable=cpassword, show='*').grid(row=5, column=1)
checkPassword = partial(checkPassword, password, cpassword)

addLabel = Label(tkWindow,text="Address").grid(row=7, column=0)

line = StringVar()
lineLabel = Label(tkWindow,text="Line").grid(row=8, column=0)
lineEntry= Entry(tkWindow, textvariable=line,).grid(row=8, column=1)

city = StringVar()
cityLabel = Label(tkWindow,text="City").grid(row=9, column=0)
cityEntry= Entry(tkWindow, textvariable=city,).grid(row=9, column=1)

stateLabel = Label(tkWindow,text="State").grid(row=10, column=0)
state = StringVar()
stateEntry   = Entry(tkWindow, textvariable=state,).grid(row=10, column=1)
pincodelabel = Label(tkWindow,text="Pincode").grid(row=11, column=0)
pincode = StringVar()
pincodeEntry    = Entry(tkWindow, textvariable=pincode,).grid(row=11, column=1)
showData = partial(showData,FirstName,LastName,username,mail,password,cpassword,line,city,state,pincode)

checkButton = Button(tkWindow, text="CheckPassword", command=checkPassword).grid(row=6, column=1)

#login button
#loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=12, column=0)
loginButton = Button(tkWindow, text="Show", command=showData).grid(row=12, column=1)
tkWindow.mainloop()