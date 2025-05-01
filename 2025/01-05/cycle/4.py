b = int(input("Input first number: "))
d = int(input("Input second number: "))
counter = 0
total = 0
for i in range(b, d + 1):
    counter += 1
    total += i

print(total / counter)