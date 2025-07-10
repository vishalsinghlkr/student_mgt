from service import add_student,search_students,all_data,delete_record

def is_valid_name(name):
    return isinstance(name, str) and name.strip() != "" and not name.strip().isdigit()

def is_valid_class(class_):
    return isinstance(class_, str) and class_.strip() != "" and not class_.strip().isdigit()

def is_valid_stream(stream):
    return isinstance(stream, str) and stream.strip() != "" and not stream.strip().isdigit()

def is_valid_age(age):
    return age.isdigit() and 5 <= int(age) <= 100

def is_valid_city(city):
    return isinstance(city, str) and city.strip() != ""

def is_valid_id(id_):
    return str(id_).isdigit()

def validate_and_add_student(**kwargs):
    name = kwargs.get("name")
    class_ = kwargs.get("class")
    stream = kwargs.get("stream")
    age = kwargs.get("age")
    city = kwargs.get("city")
    errors = []
    if not is_valid_name(name):
        errors.append("Invalid Name.")
    if not is_valid_class(class_):
        errors.append("Invalid Class.")
    if not is_valid_stream(stream):
        errors.append("Invalid Stream.")
    if not is_valid_age(age):
        errors.append("Age must be a number between 5 and 100.")
    if not is_valid_city(city):
        errors.append("Invalid City.")

    if errors:
        print("\nError in input:")
        for error in errors:
            print( error)
    else:
        try:
            add_student(**kwargs)
        except Exception as e:
            print("Failed to add student:", e)


def validate_and_search(option,student):
    id_=student.get("id")
    name = student.get("name")
    class_ = student.get("class")

    if option == 1:
        
        if is_valid_name(name):
            search_students(option, name=name)
        else:
            print("Invalid name.")

    elif option == 2:
        
        if is_valid_id(id_):
            search_students( option,by_id=int(id_))
        else:
            print("Invalid ID.")

    elif option == 3:
        
        if is_valid_name(name) and is_valid_class(class_):
            search_students(option, name=name, s_class=class_)
        else:
            print("Invalid name or class.")

    elif option == 4:
        print("Exiting search.")

    else:
        print(" Invalid option selected.")

def fetch_all_data():
    all_data()

def validate_and_delete(option, student_data):
    del_id = student_data.get("id")  
    name = student_data.get("name")

    if del_id is not None:
        try:
            del_id = int(del_id)  
        except ValueError:
            print("Invalid ID format")
            return
    if option == 1:
        if is_valid_name(name):
            delete_record(option, name=name)
        else:
            print("Invalid Name")

    elif option == 2:
        if is_valid_id(del_id):
            delete_record(option, del_id=del_id)
        else:
            print("Invalid ID")

    elif option == 3:
        return

    else:
        print("Invalid Input")

