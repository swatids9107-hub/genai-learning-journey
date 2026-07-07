# Grade Calculator with Input Validation

name = input("Enter the student name: ")
marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks allotted: "))

if marks_obtained < 0 or total_marks <= 0:
    print("Invalid input! Marks cannot be negative or zero.")
elif marks_obtained > total_marks:
    print("Invalid input! Marks obtained cannot exceed total marks.")
else:
    percentage = (marks_obtained / total_marks) * 100
    print("Percentage = {:.2f}".format(percentage))

    if percentage >= 90:
        print(name, "Outstanding performance - O")
    elif percentage >= 80:
        print(name, "Exemplary performance - A++")
    elif percentage >= 70:
        print(name, "Distinction - A+")
    elif percentage >= 60:
        print(name, "First Class - A")
    elif percentage >= 50:
        print(name, "Second Class - B+")
    elif percentage >= 35:
        print(name, "Pass")
    else:
        print(name, "Fail")
