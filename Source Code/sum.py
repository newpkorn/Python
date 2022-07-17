def sumation_1(n):

    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum


def sumation_2(n):
    sum = 0
    sum = n*(n+1)/2

    return int(sum)

n = int(input("Input N : "))

print(sumation_1(n))
print(sumation_2(n))