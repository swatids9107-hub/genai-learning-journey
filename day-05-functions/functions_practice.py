# 1️ Simple function
def function1():
    print("SWATHI")
    print("Swathi wants to be a Gen AI engineer")

function1()
print("Arguments are outside the function")


# 2️ BMI Calculator using function
def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / height_m**2
    print("BMI:", bmi)

    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

name = input("Enter your name: ")
height_cm = int(input("Enter your height (cm): "))
weight_kg = float(input("Enter your weight (kg): "))

height_m = height_cm / 100

result = bmi_calculator(name, height_m, weight_kg)
print(result)


# 3️ Multiplication function
def multiply(x, y):
    return x * y

a = multiply(3, 7)
print("Multiplication:", a)


# 4️ Even or Odd
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(even_or_odd(number))


# 5️ Positive or Negative
def positive_or_negative(num):
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"

number = int(input("Enter a number: "))
print(positive_or_negative(number))


# 6️ Find largest number in a list
def find_largest(numbers):
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    return largest

numbers = [12, 45, 3, 67, 23]
print("Largest number:", find_largest(numbers))


# 7️ Find smallest number in a list
def find_smallest(numbers):
    smallest = numbers[0]

    for i in numbers:
        if i < smallest:
            smallest = i

    return smallest

numbers = [12,34,65,78,9,7,536,4,2,67,1,89]
print("Smallest number:", find_smallest(numbers))


# 8️ Find both smallest and largest
def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]

    for i in numbers:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i

    return smallest, largest

numbers = [12, 34, 65, 78, 9, 7, 536, 4, 2, 67, 1, 89]
small, large = min_max(numbers)

print("Smallest:", small)
print("Largest:", large)


# 9️ Student Marks Analyzer
def analyze_marks(marks):
    highest = marks[0]
    lowest = marks[0]
    total = 0

    for i in marks:
        if i > highest:
            highest = i
        if i < lowest:
            lowest = i
        total += i

    average = total / len(marks)

    return highest, lowest, average

marks = [10,20,30,40,50,60,70,80,90,100]

high, low, avg = analyze_marks(marks)

print("Student Performance Summary")
print("Highest:", high)
print("Lowest:", low)
print("Average:", avg)
