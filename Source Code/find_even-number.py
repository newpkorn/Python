def is_even(number):
    evenNumber = []
    for i in range(1, number+1):
        if i % 2 == 0:
            evenNumber.append(i)
    return evenNumber

number = int(input("Number : "))

print("Those even number is : ", is_even(number))