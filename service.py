import psycopg2
from connection import conna

def add_student(**kwargs):
    conn=conna
    cur=conn.cursor()
    name=kwargs.get("name")
    class_=kwargs.get("class")
    stream=kwargs.get("stream")
    age=kwargs.get("age")
    city=kwargs.get("city")
    
    cur.execute("""insert into students(name, class, stream, age, city)
                values(%s,%s,%s,%s,%s)
               """ ,(name,class_,stream,age,city))
    conn.commit()
    print("Your Data Added Successfuly.....")
    cur.close()
    # conna.close()
def all_data():
    conn=conna
    cur=conn.cursor()
    cur.execute(""" Select* from students;
""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_record(option, **kwargs):
    conn = conna
    cur = conn.cursor()

    if option == 1:
        name=kwargs.get("name")
        cur.execute("SELECT * FROM students WHERE name = %s", (name,))
        rows = cur.fetchall()
        if not rows:
            print(f"No records found with name: {name}")
            return
        print("\nMatching Records:")
        for row in rows:
            print(row)
        conf = input("Are you to delete these records? (Yes/No): ").lower()
        if conf == "yes":
            cur.execute("DELETE FROM students WHERE name = %s", (name,))
            conn.commit()
            print(f"All records with name '{name}' have been deleted.")
        else:
            print("Deletion canceled.")

    elif option == 2:
        del_id=kwargs.get("del_id")
        cur.execute("SELECT * FROM students WHERE id = %s", (del_id,))
        row = cur.fetchone()
        if not row:
            print(f"No record found with ID: {del_id}")
            return
        print("\nRecord Found:")
        print(row)
        conf = input("Are you sure to delete this record? (Yes/No): ").lower()
        if conf == "yes":
            cur.execute("DELETE FROM students WHERE id = %s", (del_id,))
            conn.commit()
            print(f" Record with ID {del_id} has been deleted.")
        else:
            print("Deletion canceled.")

    else:
        print(" Invalid deletion option.")

    cur.close()
    
def search_students(option,**kwargs): # change to kwargs 
    conn = conna
    cur = conn.cursor()
    if option == 1:
        name = kwargs.get("name")
        cur.execute("SELECT * FROM students WHERE name = %s", (name,))
        rows = cur.fetchall()
        if not rows:
            print(f"No records found with name: {name}")
        else:
            print(f"Records for name '{name}':")
            for row in rows:
                print(row)

    elif option == 2:
        by_id = kwargs.get("by_id")
        cur.execute("SELECT * FROM students WHERE id = %s", (by_id,))
        rows = cur.fetchall()
        if not rows:
            print(f"No record found with ID: {by_id}")
        else:
            print(f"Record for ID {by_id}:")
            for row in rows:
                print(row)

    elif option == 3:
        name = kwargs.get("name")
        s_class = kwargs.get("s_class")
        cur.execute("SELECT * FROM students WHERE name = %s AND class = %s", (name, s_class))
        rows = cur.fetchall()
        if not rows:
            print(f"No record found with Name '{name}' and Class '{s_class}'")
        else:
            print(f"Records for Name '{name}' and Class '{s_class}':")
            for row in rows:
                print(row)

    elif option == 4:
        print("Returning to menu.")
        return
    else:
        print("Invalid option.")

    cur.close()

    