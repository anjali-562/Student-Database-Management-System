
import mysql.connector

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
    main_table = class_name+class_division
    table_name = class_name+class_division+'_acadmic_data'
    print("Table Name: ", table_name)
    query = "CREATE TABLE IF NOT EXISTS {}(rno varchar(20)," \
                "physics varchar(20),chemistry varchar(20),maths varchar(20))".format(table_name, main_table)


    cursor.execute(query )
    print("=================================================================")
    # insert data into the class
    record = int(input("Enter Student Count: "))
    print("Enter Student Details")
    while record!=0 :
        rno = input("Enter Roll No.: ")
        physics = input("Enter Marks for Physics: ")
        chemistry = input("Enter Marks for Chemistry: ")
        maths = input("Enter Marks for Maths: ")
        
        query = "INSERT INTO {} (rno, physics,chemistry,maths) VALUES (%s, %s,%s, %s)".format(table_name)
        para = (rno, physics,chemistry,maths)
        cursor.execute(query,para)
        connection.commit()

        print("Inserted Record into the table")

        record -=1     
        print("=================================================================") 

    connection.close()

def viewData(class_name=None):
    connection = get_connection_to_database()
    cursor = connection.cursor()

    if class_name==None:
        class_name = input("Enter class : ")
        class_name = class_name + "_acadmic_data"
    query = "SELECT * FROM {} ".format(class_name)

    cursor.execute(query)
    
    column_names = cursor.column_names
    for name in column_names :
        name = name.upper()
        print(name ,end='\t\t\t')
    print('\n')

    for data in cursor.fetchall():
        for record in data:
            print(record,end='\t\t\t')
        print("\n")


def deleteData():       

    connection = get_connection_to_database()
    cursor = connection.cursor()

    class_name = input("Enter class : ")
    table_name = class_name+'_acadmic_data'

    print("=================================================================\n") 
    print("\t\t\t\tPresent Data\n")
    print("=================================================================\n") 
    viewData(class_name=table_name)

    rno = input("Enter rno to be deleted: ")
    
    
    
    query = "DELETE FROM {} WHERE rno=%s".format(table_name)
    parameter = (rno,)
    cursor.execute(query,parameter)
    connection.commit()

    print("=================================================================\n") 
    print("\t\t\t\tUpdated Data\n")
    print("=================================================================\n") 
    viewData(class_name=table_name)

    connection.close() 




def updateData():
    connection = get_connection_to_database()
    cursor = connection.cursor()

    class_name = input("Enter class : ")
    table_name = class_name+'_acadmic_data'

    print("=================================================================\n") 
    print("\t\t\t\tPresent Data\n")
    print("=================================================================\n") 
    viewData(class_name=table_name)

    rno = input("Enter rno for which data is to be updated: ")
    
    print("1. Edit Score for Physics")
    print("2. Edit Score for Chemistry")
    print("3. Edit Score for Maths")
    choice = int(input("Enter Choice"))
    marks = input("Enter updated Marks")

    if choice == 1:
        query = "UPDATE {} SET physics=%s WHERE rno=%s".format(table_name)
    elif choice == 2:
        query = "UPDATE {} SET chemistry=%s WHERE rno=%s".format(table_name)
    elif choice == 3:
        query = "UPDATE {} SET maths=%s WHERE rno=%s".format(table_name)

    
    parameter = (marks,rno)
    cursor.execute(query,parameter)
    connection.commit()

    print("=================================================================\n") 
    print("\t\t\t\tUpdated Data\n")
    print("=================================================================\n") 
    viewData(class_name=table_name)

    connection.close() 
