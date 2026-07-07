# Simple BMI (Body Mass Index) Calculator

name = input("Enter your name: ")
height_cm = int(input("Enter your height in cm: "))
weight_kg = float(input("Enter your weight in kg: "))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

print("BMI =", bmi)

# BMI categories are based on WHO (World Health Organization) standards
if bmi < 18.5:
    print(name, "is underweight")
elif bmi < 25:
    print(name, "has normal weight")
elif bmi < 30:
    print(name, "is overweight")
else:
    print(name, "is obese")
