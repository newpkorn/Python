def get_result(num1, num2):

    print('------- Sutkun -------')

    row = 0
    while row <= 12:
        num = num1
        while num <= num2:
            if row == 0:
                print('Sutkun {}\t'.format(num), end="")
            else:
                print(num, 'x', row, '=', num*row, '\t', end="")
            num += 1
        #print("")
        row += 1

        print("")
##########################################################################

def get_result1(num1, num2):

    print("")
    row = 1

    for title in range(num1, num2+1):
        print('Sutkun {}\t'.format(title), end="")
    print("")

    while row <= 12:
        num = num1
        col = 1
        while col < num2:
            print(num, 'x', row, '=', num*row, '\t', end="")
            num+=1
            col+=1
        print("")
        row+=1
    print("")

startNumber = int(input("Start Index : "))
toNumber = int(input("To Index : "))

#get_result(startNumber, toNumber)

get_result1(startNumber, toNumber)