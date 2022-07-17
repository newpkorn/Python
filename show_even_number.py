def is_even(number):
    if number > 0:
        for i in range(1, number):
            if (i % 2) == 0:
                print(i)
                
    else :
        print("Enter the number > 0")

    return number

number = int(input("Input Number : "))

print(is_even(number))