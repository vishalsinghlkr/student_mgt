from validation import validate_and_add_student,validate_and_search,fetch_all_data,validate_and_delete
while True:
    print(" __________________________Welcome to the Student managment table:__________________________\n")
    print("--------------------->   How Can I Help You?    <-----------------")
    print(" 1. Add Student: ")
    print(" 2. Search Student:")
    print(" 3. Delete Records")
    print(" 4. Fetch All The Data From Table")
    
    
    option=int(input("""Enter valid option(1,2,3,4): """))
    if option==1:
        student_data = {
                "name": input("Enter Name: "),
                "class": input("Enter Class: "),
                "stream": input("Enter Stream: "),
                "age": input("Enter Age: "),
                "city": input("Enter City: ")
            }

        validate_and_add_student(**student_data)
    elif option==2:
        print("Search Options:")
        print("1. Search by Name")
        print("2. Search by ID")
        print("3. Search by Name and Class")
        print("4. Return To Main Menu")

        try:
            choose = int(input("Select an option (1/2/3/4): "))
        except ValueError:
            print("Option must be a number.")     
        student_data = {}
        if choose == 1:
            student_data["name"] = input("Enter Name: ")
        elif choose == 2:
            student_data["id"] = input("Enter ID: ")
        elif choose == 3:
            student_data["name"] = input("Enter Name: ")
            student_data["class"] = input("Enter Class: ")
        elif choose == 4:
            print(" Returning to Main Menu...")
            
        else:
            print("Invalid option selected.")
        validate_and_search(choose, student_data)

    elif option==3:
        print("How do you want to delete your data?")
        print("1. Delete by Name")
        print("2. Delete by ID")
        print("3. Return To Main Menu")
        
        try:
            choose = int(input("Select the Option (1 or 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        student_data={}
        if choose == 1:
            student_data["name"] = input("Enter Name: ")
        elif choose == 2:
            student_data["id"] = input("Enter ID: ")

        validate_and_delete(choose,student_data)

    elif option==4:
        fetch_all_data()
    else:
        cont = input("\nDo you want to Exit? (yes/no): ")
        if cont.lower().strip() != "yes":
             break
        
                
