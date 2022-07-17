from tkinter import Button, Entry, Label, Tk, simpledialog, messagebox

def bmi_calculatior():
    name = txt_name.get()
    width = int(txt_width.get())
    height = int(txt_height.get())

    result = int((width / height / height)*10000)

    messagebox.showinfo('BMI', ''+ name + '\'s BMI is : ' +str(result))
    
def cls():
    txt_name.delete(0, 'end')
    txt_width.delete(0, 'end')
    txt_height.delete(0, 'end')

root = Tk()
root.title('BMI Calculation')

lbl_name = Label(root, text='Name :')
lbl_width = Label(root, text='Width :')
lbl_heigth = Label(root, text='Height :')

txt_name = Entry(root, width=20)
txt_width = Entry(root, width=20)
txt_height = Entry(root, width=20)

btn_ok = Button(root, text=' OK ', width=10, command=bmi_calculatior)
btn_cls = Button(root, text='Clear', width=20, command=cls)

lbl_name.grid(row=0, column=0)
txt_name.grid(row=0, column=1)

lbl_width.grid(row=1, column=0)
txt_width.grid(row=1, column=1)

lbl_heigth.grid(row=2, column=0)
txt_height.grid(row=2, column=1)

btn_ok.grid(row=3, column=0)
btn_cls.grid(row=3, column=1)

root.mainloop()