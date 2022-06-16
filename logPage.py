import sys
import os
from tkinter import *
from functools import partial
from tkinter import filedialog as fd
def openDoctor():
    os.system('doctor.py')
def openPatient():
    os.system('Patient.py')

#window
tkWindow = Tk()
tkWindow.geometry('250x70')
tkWindow.title('Sagar')

UserLabel = Label(tkWindow,text="Select UserType").grid(row=1, column=3)


Doctor = Button(tkWindow, text="Doctor",command=openDoctor).grid(row=2, column=2)
Patient = Button(tkWindow, text="Patient",command=openPatient).grid(row=2, column=4)

tkWindow.mainloop()