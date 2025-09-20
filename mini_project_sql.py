import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name TEXT NOT NULL,
    roll_no INTEGER UNIQUE,
    subject TEXT,
    marks INTEGER       
)
               

""")
conn.commit()
conn.close()
print("Welcome to Student Database Manager")
def add_student():
    name = input("enter name :")
    roll_no = int(input("enter roll no :"))
    subject = input("enter subject :")
    marks = int(input("enter marks :"))

    import sqlite3
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute( "INSERT INTO students(name,roll_no,subject,marks) VALUES(?,?,?,?)",(name,roll_no,subject,marks))
    conn.commit()
    conn.close()

    print(f"student {name} added sucessfully")
def update_marks():
    roll_no = int(input("Enter roll number of the student: "))
    new_marks = int(input("Enter updated marks: "))

    import sqlite3
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # Update the marks for the student with the given roll number
    cursor.execute("UPDATE students SET marks = ? WHERE roll_no = ?", (new_marks, roll_no))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Marks for student with roll number {roll_no} have been updated successfully.")
    else:
        print(f"No student found with roll number {roll_no}.")

    conn.close()
def search_student():
    student_name = input("enter name :")

    import sqlite3
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name = ?", (student_name,))

    student_details = cursor.fetchall()
    if student_name:
        print("student details : \n")    
        for i in student_details:
            print(i)
    else:
        print(f"{student_name} not found in database")
    conn.close()
def export_data():
    import sqlite3
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()
    import pandas as pd
    df = pd.DataFrame(all_students)
    df.to_csv("students.csv",index=False)
    print("csv file created for database")

while True:
    enter_choice = int(input("choose number between 1 to 5 : "))
    if 1 <= enter_choice <= 5:
        if enter_choice == 1:
            print(add_student())
        elif enter_choice == 2:
            print(update_marks())
        elif enter_choice == 3:
            print(search_student())
        elif enter_choice == 4:
            print(export_data())
        elif enter_choice == 5:
            print("exiting the program .....")
            break
    else:
        print("invalid input please try entering again")
    
    
    