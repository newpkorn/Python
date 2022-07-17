import random
def randomizer(minValue, maxValue):
    result = random.randint(minValue, maxValue)
    return result

minValue = int(input("Enter min value : "))
maxValue = int(input("Enter max value : "))

randomValue = randomizer(minValue, maxValue)

print("The random number is : ", randomValue)