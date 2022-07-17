import sys
from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('wordcapital.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n')                        # read line
            country, capital = line.split('/')              # split word with '/'Biejing
            country = country.capitalize()                  # convert to capital letter
            capital = capital.capitalize()                  # convert to capital letter
            world_capital[country] = capital                # dictionary type


def write_to_file(country_name, capital_name):
    with open('wordcapital.txt', 'a') as file:
        file.write('\n')                                    # write new line
        file.write(country_name + '/' + capital_name)       # write file with format country name / capital name
        file.close()

root = Tk()
root.withdraw()
world_capital = {}  # dictionary
while True:
    read_from_file()                                        # call function read file
    simpledialog.askstring
    query_country = ''
    query_country = simpledialog.askstring('Country', 'Type the name of a country : ')
    query_country = query_country.capitalize()
    if query_country in world_capital:
        result = world_capital[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result)
    else:
        new_capital = simpledialog.askstring('Teach me', 'I don\'t know the answer. Please teach me what is the capital citi of ' + query_country + '?')
        messagebox.showinfo('Thanks', 'Thank ypu for teach me. i will definitely know it next time')
        new_capital = new_capital.capitalize()
        write_to_file(query_country, new_capital)              # write to file
    answer = simpledialog.askstring('Continue', 'Do you want to try again? y/n: ')
    if answer == 'n':
        messagebox.showinfo('Thanks', 'Thank you for playing.')
        root.destroy()
        sys.exit()
