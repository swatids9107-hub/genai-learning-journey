# 1️ Create an empty list
l = []
print(l)

# 2️ Create a list of integers
l1 = [1, 2, 3, 4, 5]
print(l1)

# 3️ Create a list with strings (homogeneous list)
l3 = ['Python', 'Swathi', 'Swam', 'AI', 'ML']
print(l3)

# 4️ Access elements using index
print(l1[0])   # first element
print(l1[-1])  # last element

# 5️ Nested list (list inside a list)
l5 = [1, 2, 3, ['python', 'swam', 'AI']]
print(l5)
print(l5[3])   # accessing inner list

# 6️ Append - add element at the end
l1.append(6)
print(l1)

# 7️ Extend - add multiple elements
l1.extend([7, 8, 9])
print(l1)

# 8️ Insert - add element at specific position
l1.insert(0, 10)
print(l1)

# 9️ Update / modify elements
l1 = list(range(1, 6))
print(l1)

l1[0] = 10
print(l1)

l1[1:5] = [20, 30, 40, 50]
print(l1)

# 10 Delete operations
l1.pop()        # remove last element
print(l1)

l1.remove(10)   # remove specific value
print(l1)

# Clear the list
l1.clear()
print(l1)

# Delete entire list
del l1

# 1️1️ Loop through a list
l1 = [1, 2, 3, 4]
for i in l1:
    print(i + 1)

# 1️2️ Create a new list using loop
l1 = [1, 2, 3, 4]
out = []

for i in l1:
    out.append(i + 1)

print(out)

# 1️3️ Separate even and odd numbers
l2 = [1,2,3,4,5,6,7,8,9]

even = []
odd = []

for i in l2:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)

# 1️4️ Enumerate example
l3 = ['Python', 'Statistics', 'AI']

for i, j in enumerate(l3):
    print(i, j)
