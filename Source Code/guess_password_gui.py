import sys
from tkinter import Tk, simpledialog, messagebox
from tkinter.constants import RADIOBUTTON


root = Tk()
root.withdraw()

counter = 0

password = ''
password = simpledialog.askstring('Gusee Password', 'Enter password')

while password != 'Password':
    simpledialog.askstring

    counter += 1
    messagebox.showinfo('Answer', 'Access denied')

    password = simpledialog.askstring('Gusee Password', 'Enter password')
    if password == 'Password':
        counter += 1

        messagebox.showinfo('Answer', 'Access grated! The correct password is : Password\n The number of you gusses is : '+str(counter))
