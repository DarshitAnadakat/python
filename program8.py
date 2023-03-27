sub1 = int(input("Enter the marks of subject 1: "))
sub2 = int(input("Enter the marks of subject 2: "))
sub3 = int(input("Enter the marks of subject 3: "))
sub4 = int(input("Enter the marks of subject 4: "))

total = sub1 + sub2 + sub3 + sub4
percentage = (total / 400) * 100

if sub1 < 40 or sub2 < 40 or sub3 < 40 or sub4 < 40:
    result = "FAIL"
    grade = "With Held**"
else:
    result = "PASS"
   
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

print("Total marks =", total)
print("Percentage =", percentage)
print("Result =", result)
print("Grade =", grade)