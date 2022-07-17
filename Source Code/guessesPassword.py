password = "HelloWorld"

counter = 0
userGuess = input("Enter your password : ")

while userGuess != password:
    counter += 1
    print("Access Denied !")

    userGuess = input("Enter your password : ")
    if userGuess == password:
        counter += 1
        print("Accesss Grated!, The password is", password)
        print("Totle number of guesses is ", counter)