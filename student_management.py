all_students = [] 


while(True):
    print("======= STUDENT MANAGEMENT SYSTEM =======")

    print("1. Add student")

    print("2. view all students")

    print("3. Calculate average score")

    print("4. check pass or fail")

    print("5. Exit\n")

    choice = input("Enter your choice: ")

    print("your selected:", choice)

    if choice == "1":
        name = input("Enter student name: ")
        score = int(input('Enter student score:'))
        all_students.append(
            {
                "name": name,
                "score": score
            }
        )

    elif choice == "2":
        for items in all_students:
            print()

    if score >= 50:
        print("passed")
    else:
        print("failed")


    print("My name is Ololade")