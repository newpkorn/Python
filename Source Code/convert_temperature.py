def is_converted(choice, temp):
    if choice == '1':
        result = (temp - 32) / 1.8
    elif choice == '2':
        result = (temp * 1.8) + 32

    return int(result)

print("Press 1 to convert from Fahrenheit to Celsius.\nPress 2 to convert from Celsius to Fahrenheit.")

choice = input(("Please enter  : "))
temp = int(input("Enter temperature : "))

print(is_converted(choice, temp))