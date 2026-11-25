# Student Marks, Percentage, Grade and Academic Details

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 3: "))

total = m1 + m2 + m3
percentage = total / 3

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Academic Details ---")
print("Name       :", name)
print("Roll No    :", roll)
print("Total      :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
