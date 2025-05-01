number = input("Input a number: ")
plus = 0
multi = 1
i = 0
while i < len(number):
    plus += int(number[i])
    multi *= int(number[i])
    i += 1
print(plus, multi)








