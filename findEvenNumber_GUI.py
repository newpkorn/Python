import tkinter as tk
from tkinter.constants import END, N

def find():
    number = int(input_number.get())
    if number % 2 == 0:
        result.configure(text='Even')
    else:
        result.configure(text='Odd')

def clear():
    input_number.delete(0, END)
    result.configure(text='Result : ')

root = tk.Tk()
root.title('My App')

input_lbl = tk.Label(root, text='Enter number : ')
input_number = tk.Entry(root, width=12)

find_bt = tk.Button(root, text='Find', command=find)
cls_bt = tk.Button(root, text='Clear', command=clear)

result = tk.Message(root, text='Result : ')

input_lbl.grid(row=0, column=0)
input_number.grid(row=0, column=1)
find_bt.grid(row=1, column=0)
cls_bt.grid(row=1, column=1)
result.grid(row=2, column=0, columnspan=2)

root.mainloop()