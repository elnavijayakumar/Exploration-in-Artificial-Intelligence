# Student Marks, Percentage and Grade
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))
total = 0
for i in range(1, n + 1):
 mark = float(input(f"Enter mark for Subject {i}: "))
 total += mark
percentage = total / n
if percentage >= 90:
 grade = "A+"
 performance = "Outstanding"
elif percentage >= 80:
 grade = "A"
 performance = "Excellent"
elif percentage >= 70:
 grade = "B"
 performance = "Very Good"
  elif percentage >= 60:
 grade = "C"
 performance = "Good"
elif percentage >= 50:
 grade = "D"
 performance = "Average"
else:
 grade = "F"
 performance = "Needs Improvement"
print("\n--- Academic Performance ---")
print("Student Name :", name)
print("Total Marks :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade :", grade)
print("Performance :", performance)
Sample Output
Enter student name: Priya
Enter number of subjects: 5
Enter mark for Subject 1: 85
Enter mark for Subject 2: 78
Enter mark for Subject 3: 92
Enter mark for Subject 4: 88
Enter mark for Subject 5: 81
--- Academic Performance ---
Student Name : Priya
Total Marks : 424.0
Percentage : 84.8 %
Grade : A
Performance : Excellent
