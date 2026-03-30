student={}
def add_student(student,):
    roll=int(input("enter roll number: "))
    name=(input("enter name: "))
    marks1=int(input("enter marks 1: "))
    marks2=int(input("enter marks 2: "))
    marks3=int(input("enter marks 3: "))
    student[roll]={"name":name,"marks":[marks1,marks2,marks3]}
    print("student added successfully!")
    
def display_student(student):
    roll = int(input("Enter roll number: "))

    if roll in student:
        print(f"Name: {student[roll]['name']}")
        print(f"Marks: {student[roll]['marks']}")
    else:
        print("Student not found.")


                

