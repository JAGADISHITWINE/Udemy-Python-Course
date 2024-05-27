import psycopg2

def updating_single_field():
    conn = psycopg2.connect(host='localhost',database='studentdb',user='postgres',password='Itwinetech@1234',port='5432')
    cur = conn.cursor()
    students_id = input('Enter id of the student to be updated: ')
    fields = {
        "1":("name","Enter the new name: "),
        "2":("address","Enter the new address: "),
        "3":("age","Enter the new age: "),
        "4":("number","Enter the new number: "),
    }
    print("Which field would you like to update")
    for key in fields:
        print(f'{key}:{fields[key[0]]}')
        
    field_choice = input('Enter the number of the field you want to update: ')
    
    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        new_value = input(prompt)
        sql = f"update students set {field_name}=%s where students_id=%s"
        cur.execute(sql,(new_value,students_id))
        print(f"{field_name} updated successfully")
    else:
        print("Invalid Choice")
        
    conn.commit()
    conn.close()