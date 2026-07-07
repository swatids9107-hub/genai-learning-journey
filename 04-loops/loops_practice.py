


# 1️ Basic for loop
for i in range(1,5):
    print(i)

# 2️ Sum of numbers from 1 to 9
total = 0
for i in range(1,10):
    total += i
print(total)

# 3️ Multiplication table
num = int(input("Enter the number: "))
for i in range(1,11):
    print(num, "*", i, "=", num * i)

# 4️ Multiples of 3 or 5 less than 100
for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

# 5️ Common multiples of 3 and 5
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# 6️ Sum of even numbers between 1 and 50
total = 0
for i in range(1,51):
    if i % 2 == 0:
        total += i
print(total)

# 7️ While loop with list
numbers = [5,4,4,3,1,-1,-2,-3,-4,-5]
total = 0
i = 0

while numbers[i] > 0:
    total += numbers[i]
    i += 1

print(total)
