from student_utils import *
while True:
    print("1. add student")
    print("2. view student")
    print("3. search student")
    print("4. calculate average")
    print("5. exit")
    ch=int(input("enter choice: "))
    if ch==1:
        add_student(student)
    elif ch==2:
        display_student(student)
    elif ch==3:
        search_student(student)
    elif ch==4:
        calculate_avg(student)
    elif ch==5:
        print("exiting program...")
        break