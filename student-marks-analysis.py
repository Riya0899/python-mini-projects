import numpy as np

# NumPy is a Python library used for working with arrays and
# performing mathematical operations efficiently.

# 🔹 Creating a NumPy Array:
# Example:
# arr = np.array([1, 2, 3, 4])

# 🔹 2D Array (Matrix):
# rows = students, columns = subjects
# Example:
# arr = np.array([[1, 2], [3, 4]])

# 🔹 Axis Concept:
# axis = 0 → column-wise (downwards)
# axis = 1 → row-wise (across)

# 🔹 Mean (Average):
# Formula: sum of values / total values
# Syntax: np.mean(array)
# Example:
# np.mean([10, 20, 30]) → 20

# 🔹 Median (Middle Value):
# Middle value after sorting
# Example:
# np.median([10, 30, 20]) → 20

# 🔹 Standard Deviation (Spread of data):
# Measures how much values deviate from mean
# Syntax: np.std(array)

# ==========================================================
# 📊 STUDENT MARKS ANALYZER PROJECT
# ==========================================================

# Project : Student Marks Analyzer

# Input: Marks of students (NumPy arrays)
# Features:
# Calculate mean, median, standard deviation
# Find topper and lowest scorer
# Subject-wise performance
# Concepts: Arrays, aggregation functions
# Sample Data: Rows = Students, Columns = Subjects
marks = np.array([
    [85, 78, 92, 88, 76],
    [70, 65, 80, 75, 72],
    [90, 92, 88, 95, 91],
    [60, 55, 58, 62, 65],
    [78, 82, 85, 80, 79]
])

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5"]
subjects = ["Math", "Physics", "Chemistry", "English", "CS"]

# -------------------------------
# 📊 Overall Statistics
# -------------------------------
mean_marks = np.mean(marks)
median_marks = np.median(marks)
std_dev = np.std(marks)

print("📊 Overall Performance:")
print("Mean Marks:", mean_marks)
print("Median Marks:", median_marks)
print("Standard Deviation:", std_dev)

# -------------------------------
# 🏆 Topper & Lowest Scorer
# -------------------------------
total_marks = np.sum(marks, axis=1)

topper_index = np.argmax(total_marks)
lowest_index = np.argmin(total_marks)

print("\n🏆 Topper:", students[topper_index], "with", total_marks[topper_index], "marks")
print("📉 Lowest Scorer:", students[lowest_index], "with", total_marks[lowest_index], "marks")

# -------------------------------
# 📚 Subject-wise Performance
# -------------------------------
subject_avg = np.mean(marks, axis=0)

print("\n📚 Subject-wise Average:")
for i in range(len(subjects)):
    print(subjects[i], ":", subject_avg[i])

# -------------------------------
# 📈 Student-wise Performance
# -------------------------------
print("\n📈 Student-wise Total Marks:")
for i in range(len(students)):
    print(students[i], ":", total_marks[i])

# -------------------------------
# 🔍 Extra Insights
# -------------------------------
highest_subject_marks = np.max(marks, axis=0)

print("\n🔥 Highest Marks in Each Subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", highest_subject_marks[i])