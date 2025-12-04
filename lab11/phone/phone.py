import psycopg2
import csv
import re   
coon = psycopg2.connect(host="localhost", dbname = "postgres", user = "postgres", password = 'new_password' , port = 5432)

cur = coon.cursor()

def add_contact_console():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone: ")
    
    cur.execute(
        "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )
    coon.commit()
    print("Contact added!")

#add_contact_console()

def add_contacts_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )
    coon.commit()
    print("SUCCES")

#add_contacts_from_csv('a.csv')

def update_contact():
    phone = input("Enter phone of contact to update: ")
    new_first_name = input("New first name (leave blank if no change): ")
    new_phone = input("New phone (leave blank if no change): ")

    if new_first_name:
        cur.execute("UPDATE contacts SET first_name = %s WHERE phone = %s", (new_first_name, phone))
    if new_phone:
        cur.execute("UPDATE contacts SET phone = %s WHERE phone = %s", (new_phone, phone))

    coon.commit()
    print("Contact updated!")

def search_contacts():
    keyword = input("Enter first name, last name or phone to search: ")
    cur.execute(
        "SELECT * FROM contacts WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone LIKE %s",
        (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

#search_contacts()



def delete_contact():
    keyword = input("Enter first name or phone to delete: ")
    cur.execute(
        "DELETE FROM contacts WHERE first_name = %s OR phone = %s",
        (keyword, keyword)
    )
    coon.commit()
    print("Contact deleted!")


def ups(name,surname,phone):
    cur.execute(
        
        "SELECT * FROM contacts WHERE first_name = %s and last_name = %s",
        (name,surname)
        
    )
    if cur.fetchall():
        cur.execute(
        
        "UPDATE contacts set  phone = %s WHERE first_name = %s and last_name = %s",
        (phone,name, surname)
        
    )
    else:
        cur.execute(
            "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
                (name, surname, phone)
        )
    coon.commit()

nu = [["L", "Bro", "94"],
      ["One", "Two", "+77051225072"]
]

def inslist(list):
    cursed = []

    for i in nu:
        if re.fullmatch(r'\+?\d{10,}', i[2]):

            cur.execute(
                "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s,%s,%s)",
                (i[0],i[1],i[2])
            )        
        else:
            cursed.append(i)
        coon.commit()
    return cursed
#inslist(nu)

def limof(limit, offset):
    cur.execute(
        "SELECT first_name,last_name, phone FROM contacts " \
        "LIMIT %s OFFSET %s",
        (limit, offset)
    )
    for i in cur.fetchall():
        print(i)
 

# 
# 
#limof(3,1)
#ups("Dias","Ksopr","54655")