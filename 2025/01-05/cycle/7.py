number = int(input("Input a number: "))

for i in range(1, number):
    if number % i == 0:
        print(False)
        break
    else:
        print(True)