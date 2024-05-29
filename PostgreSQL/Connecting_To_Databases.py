import psycopg2

def create_table():
    conn = psycopg2.connect(host='localhost',database='studentdb',user='postgres',password='Itwinetech@1234',port='5432')
    cur = conn.cursor()
    cur.execute("create table students(students_id serial primary key, name text, address text, age int, number text);")
    print("Students table created")
    conn.commit()
    conn.close()
    
def insert_data():
    name = input('Enter name: ')
    address = input('Enter Address: ')
    age = input('Enter age: ')
    number = input('Enter number: ') 
    conn = psycopg2.connect(host='localhost',database='studentdb',user='postgres',password='Itwinetech@1234',port='5432')
    cur = conn.cursor()
    cur.execute("insert into students(name,address,age,number) values (%s,%s,%s,%s)",(name,address,age,number))
    print("Data added in students table")
    conn.commit()
    conn.close()
    
def read_data():
    conn = psycopg2.connect(host='localhost',database='studentdb',user='postgres',password='Itwinetech@1234',port='5432')
    cur = conn.cursor()
    cur.execute("select * from students;")
    students = cur.fetchall()
    for student in students:
        print(f'ID {student[0]}, Name:{student[1]}, Address:{student[2]}, Age:{student[3]}, Number:{student[4]}')
    conn.commit()
    conn.close()
    
def delete_data():
    conn = psycopg2.connect(host='localhost',database='studentdb',user='postgres',password='Itwinetech@1234',port='5432')
    cur = conn.cursor()
    students_id = input('Enter id of the student to be delete: ')
    cur.execute('select * from students where students_id = %s',(students_id))
    student = cur.fetchone()
    if student:
        print(f'Student to be deleted: ID {student[0]}, Name:{student[1]}, Address:{student[2]}, Age:{student[3]}, Number:{student[4]}')
        decision = input('Do you want to delete this Student (yes/no)? ').lower()
        if decision == 'yes':
            cur.execute('delete from students where students_id = %s',(students_id))       
        print("Student record deleted")
    conn.commit()
    conn.close()

def update_data():
    students_id = input('Enter id of the student to be updated: ')
    name = input('Enter name: ')
    address = input('Enter Address: ')
    age = input('Enter age: ')
    number = input('Enter number: ') 
    conn = psycopg2.connect(host='localhost',database='studentdb',user='postgres',password='Itwinetech@1234',port='5432')
    cur = conn.cursor()
    cur.execute("update students set name=%s , address=%s , age=%s , number=%s where students_id=%s",(name,address,age,number,students_id))
    print("Data Updated in students table")
    conn.commit()
    conn.close()
    

while True:
    print("\n Welcome to the student database management system")
    print("1. Create Table")
    print("2. Insert Table")
    print("3. Read Table")
    print("4. Update Table")
    print("5. Delete Table")
    print("6. Exit")
    
    choice = int(input("Enter your choice (1-6): "))
    if choice == 1:
        create_table()
    elif choice == 2:
        insert_data()
    elif choice == 3:
        read_data()
    elif choice == 4:
        update_data()
    elif choice == 5:
        delete_data()
    elif choice == 6:
        break
    else:
        print("InvalidChoice, Please enter a number between 1-6")
        
        
    