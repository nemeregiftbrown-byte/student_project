all_students = [] 

def add_student():
    name = input("Enter student name: ")
    score = int(input('Enter student score: '))
    all_students.append(
        {
            "name": name,
            "score": score
        }
     )

def view_students():
    for student in all_students:
        print("Student name is: ",student["name"], "     score is: ", student["score"])

def calculate_average():
    total_score = 0
    for student in all_students:
        total_score = total_score + student["score"]
    
    average = total_score / len(all_students)
    print("\ntotal_score is: ", total_score)
    print("\naverage score is: ", average)  

def check_result(): 
    for student in all_students:
        if student["score"] >= 50:
            print("\nstudent: ", student["name"], "\nScore: ", student["score"], "\nResult: passed\n\n")
        else : 
           print("student: ", student["name"], "\nScore: ", student["score"], "\nResult: failed\n\n")


def options():
    print("\n\n======= STUDENT MANAGEMENT SYSTEM =======\n")
    
    print("1. Add student")
    
    print("2. view all students")
    
    print("3. Calculate average score")
    
    print("4. check pass or fail")
    
    print("5. Exit\n")

    choice = input("Enter your choice: ")

    print("your selected:", choice)

    return choice

    

    




while(True):
    choice = options()
    
    if choice == "1":
        add_student()
        

    elif choice == "2":
        view_students()


    elif choice == "3":
        calculate_average()    


    elif choice == "4":
        check_result() 


    elif choice == "5":
        break



