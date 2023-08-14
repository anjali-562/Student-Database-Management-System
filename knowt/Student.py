import mysql.connector
import random

def get_connection_to_database():
    connection = mysql.connector.connect(
        user="root", password="admin", host="localhost", database="KNOWT"
    )
    return connection


def insertData():
    connection = get_connection_to_database()
    cursor = connection.cursor()
    class_name = input("Enter Class Name : ")
    class_division = input("Enter Class Division : ")

    # create a seprate table for the class
    table_name = class_name+class_division
    print("Table Name: ", table_name)
    query = "CREATE TABLE IF NOT EXISTS {}(rno varchar(30) Primary Key, name varchar(20),admission_no varchar(20),gender varchar(20))".format(table_name)
    cursor.execute(query )
    print("=================================================================")
    # insert data into the class
    record = int(input("Enter Student Count: "))
    print("Enter Student Details")
    while record!=0 :
        rno = input("Enter Roll No.: ")
        name = input("Enter Name: ")
        admin_no = random.choice(range(1,1000))
        gender = input("Enter gender: ")
        
        query = "INSERT INTO {} (rno, name,admission_no,gender) VALUES (%s, %s,%s, %s)".format(table_name)
        para = (rno,name,admin_no,gender)
        cursor.execute(query,para)
        connection.commit()

        print("Inserted Record into the table")

        record -=1     
        print("=================================================================") 

    connection.close()

def updateData():

    connection = get_connection_to_database()
    cursor = connection.cursor()

    class_name = input("Enter class : ")

    print("=================================================================\n") 
    print("\t\t\t\tPresent Data\n")
    print("=================================================================\n") 
    viewData(class_name=class_name)

    rno = input("Enter rno for which data is to be updated: ")
    name = input("Enter updated name")
    query = "UPDATE {} SET name=%s WHERE rno=%s".format(class_name)
    parameter = (name,rno)
    cursor.execute(query,parameter)
    connection.commit()

    print("=================================================================\n") 
    print("\t\t\t\tUpdated Data\n")
    print("=================================================================\n") 
    viewData(class_name=class_name)

    connection.close() 


def viewData(class_name=None):
    connection = get_connection_to_database()
    cursor = connection.cursor()

    if class_name==None:
        class_name = input("Enter class : ")
    query = "SELECT * FROM {} ".format(class_name)

    cursor.execute(query)
    
    column_names = cursor.column_names
    for name in column_names :
        name = name.upper()
        print(name ,end='\t\t')
    print('\n')

    for data in cursor.fetchall():
        for record in data:
            print(record,end='\t\t\t')
        print("\n")


    