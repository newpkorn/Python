password = 'Password'

counter = 0
guessPassword = input('Enter Password : ')

while guessPassword != password:
    counter += 1
    print('Access denied !')

    guessPassword = input('Enter Password : ')

    if guessPassword == password:
        counter += 1
        print('Access grated!. Your password is : ', password)
        print('The number of password guesses is ', counter)
