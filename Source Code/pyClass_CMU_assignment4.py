def not_poor(str1):
    new_str = ''
    snot = str1.find('not')
    spoor = str1.find('poor')

    if snot > 0 or spoor > 0:
        return str1
    begin = 0

    while snot > 0 and spoor > 0:
        if spoor > snot:
            new_str += "".join(str1[begin:snot]+"good")
        else:
            new_str += "".join(str1[begin:spoor+4])
        begin = spoor+4
        if begin >= len(str1):
            break

        snot = str1.find('not', begin)
        spoor = str1.find('poor', begin)
    new_str += "".join(str1[begin:])
    return new_str


str1 = input('Input string to be converted : ')
conv_str = not_poor(str1)
print('The converted string is ', conv_str)