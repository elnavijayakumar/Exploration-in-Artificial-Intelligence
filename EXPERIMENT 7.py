# Data Cleaning and Exploratory Data Analysis using Pandas
import pandas as pd
data = {
 "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
 "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
 "Attendance": [92, 85, None, 88, 95, 90],
 "Mark": [86, 91, 78, None, 95, 82]
}
df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())
# Missing value treatment
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())
# Remove duplicate records
df = df.drop_duplicates()
print("\n--- Cleaned Dataset ---")
print(df)
print("\n--- Descriptive Statistics ---")
print(df.describe())
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))
print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))

OUTPUT
--- Original Dataset ---
   Name Department Attendance Mark
0 Anitha CSE 92.0 86.0
1 Bala CSE 85.0 91.0
2 Chitra ECE NaN 78.0
3 Dinesh CSE 88.0 NaN
4 Ezhil ECE 95.0 95.0
5 Fathima CSE 90.0 82.0
Missing Values:
Name 0
Department 0
Attendance 1
Mark 1
dtype: int64
--- Cleaned Dataset ---
 Name Department Attendance Mark
0 Anitha CSE 92.0 86.000000
1 Bala CSE 85.0 91.000000
2 Chitra ECE 90.0 78.000000
3 Dinesh CSE 88.0 86.400000
4 Ezhil ECE 95.0 95.000000
5 Fathima CSE 90.0 82.000000
--- Department-wise Average Marks ---
Department
CSE 86.35
ECE 86.50
Name: Mark, dtype : float64
--- EDA Summary ---
Highest Mark : 95.0
Lowest Mark : 78.0
Average Mark : 86.4
Average Attendance : 90.0
