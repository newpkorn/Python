from tkinter import *
class rectangleArea:
    def __init__(self, win):
        self.width_lb = Label(win, text='Enter width : ')
        self.heigth_lb = Label(win, text='SEnter height : ')
        self.output_lb = Label(win, text='Area of rectangle is : ')

        self.width_input = Entry()
        self.height_input = Entry()
        self.output = Entry()

        self.width_lb.place(x=80, y=50)
        self.width_input.place(x=200, y=50)
        self.heigth_lb.place(x=80, y=100)
        self.height_input.place(x=200, y=100)

        self.output_lb.place(x=80, y=150)
        self.output.place(x=200, y=150)

        self.ok_button = Button(win, text='OK', command=self.area, width=30)
        self.ok_button.place(x=80, y=200)

    def area(self):
        self.output.delete(0, 'end')
        width = int(self.width_input.get())
        height = int(self.height_input.get())

        resut = width * height

        self.output.insert(END, str(resut))


window = Tk()
rectangleArea(window)
window.title('Area Calculator')
window.geometry("400x300+10+10")
window.mainloop()