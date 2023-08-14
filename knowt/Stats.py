import matplotlib.pyplot as plt
import mysql.connector

def get_connection_to_database():
    connection = mysql.connector.connect(
        user="root", password="admin", host="localhost", database="KNOWT"
    )
    return connection


def show_gender_plot():

    connection = get_connection_to_database()
    cursor = connection.cursor()
    class_name = input("Enter Class Name : ")

    female_count = "SELECT COUNT(*) FROM {} WHERE gender='F'".format(class_name)
    cursor.execute(female_count)
    female_count = cursor.fetchall()[0][0]

    male_count = "SELECT COUNT(*) FROM {} WHERE gender='M'".format(class_name)
    cursor.execute(male_count)
    male_count = cursor.fetchall()[0][0]

    y = [male_count,female_count]
    mylabels = ["Male", "Female"]

    plt.pie(y, labels = mylabels,shadow = True)
    plt.legend()
    plt.show() 

    connection.close()


def show_marks_plot():

    connection = get_connection_to_database()
    cursor = connection.cursor()
    class_name = input("Enter Class Name : ")
    table_name = class_name+'_acadmic_data'
       
    print("Choose Subject to see plot")
    print("1. Physics")
    print("2. Chemistry")
    print("3. Maths")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        parameter = 'physics'
    elif choice == 2:
        parameter = 'chemistry'
    elif choice == 3:
        parameter = 'maths'
    query = "SELECT rno,{} FROM {}".format(parameter,table_name)

    cursor.execute(query)
    data = cursor.fetchall()

    x_axis = []
    y_axis = []

  
    for record in data:
        x_axis.append(record[0])  
        y_axis.append(record[1])

    plt.scatter(x_axis,y_axis)
    plt.show()

    connection.close()



