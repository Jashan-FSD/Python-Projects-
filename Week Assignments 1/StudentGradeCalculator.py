# Function to calculate average
def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

# Function to assign grade
def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

# Main Program
print("Student Grade Calculator")

marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))

average = calculate_average(marks1, marks2, marks3)
grade = assign_grade(average)

print("\nAverage Marks =", round(average,2))
print("Grade =", grade)