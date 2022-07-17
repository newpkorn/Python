evenNumber = []

number = int(input('Enter number : '))

for i in range(1, number+1):
    if i % 2 == 0:
        evenNumber.append(i)

print(evenNumber)