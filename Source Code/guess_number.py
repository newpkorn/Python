import random as rd

def con(continues):
    if continues == 'y':
        opt()
    elif continues == 'n':
        return False

def opt():

    count = 0
    nRan = rd.randrange(1, 100)
    print(nRan)

    number = int(input('Enter the number that you guess between 1-100 : '))

    while number != nRan:
        count +=1
        if number < nRan:
            print('Too low, try again')
            number = int(input('Enter the number that you guess between 1-100 : '))
        elif number > nRan:
            print('Too high, try again')
            number = int(input('Enter the number that you guess between 1-100 : '))
        else:
            break
    print('Congratulation! You used ', count+1, ' attempts')

    continues = input('Do you want to continue? (y or n) : ')
    con(continues)

opt()