import sys
from tkinter import Tk, simpledialog, messagebox

root = Tk()
root.withdraw()

while True:
    price = int(simpledialog.askstring('Price', 'Price : '))
    amount = int(simpledialog.askstring('Money', 'Money amount : '))

    if  amount >= price:
        discount = (price*10)/100
        result = price - discount
        change = amount - result

        messagebox.showinfo('Billing : ', 'Price : '+str(price)+'\nGet discount : '+str(discount)+'\nTotal : '+str(result)+'\nYour money : '+str(amount)+'\nYour change : '+str(change))
                            
    else :
        messagebox.showwarning('ERROR', 'Your input money not enough!!')

    ans = simpledialog.askstring('Continue ?', 'Do you want to exit? (y/n)')
    if ans == 'y':
        messagebox.showinfo('Exit', 'Thank you')
        root.destroy()
        sys.exit()

root.mainloop()