from tkinter import Button, Entry, Label, Tk, messagebox

def get_even_number():
    number = int(txt_number.get())
    evenNumber = []

    for i in range(1, number+1):
        if i % 2 == 0:
            evenNumber.append(i)
    messagebox.showinfo('Even number', str(evenNumber))
    txt_number.delete(0, 'end')
    
root = Tk()
root.title('Python Form')

lbl_number = Label(root, text='Enter number', width=20)
txt_number = Entry(root, width=20)
btn_ok = Button(root, text='OK', width=10, command=get_even_number)

lbl_number.grid(row=0, column=0)
txt_number.grid(row=0, column=1)
btn_ok.grid(row=1, column=0, columnspan=2)


root.mainloop()