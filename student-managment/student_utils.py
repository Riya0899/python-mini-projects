from student_data import *

def search_student(student):
    roll=int(input("enter rollnumber to search: "))
    if roll in student:
        print(f"found: rollno:{roll},name:{student[roll]['name']},marks={student[roll]['marks']}")
    else:
        print("student not found")
        
def calculate_avg(student):
    roll = int(input("Enter roll number: "))

    if roll in student:
        marks = student[roll]['marks']
        avg = sum(marks) / len(marks)
        print(f"Average marks: {avg}")
    else:
        print("Student not found.")

    
