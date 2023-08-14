"""

This module has database related operations
Author: Anjali Gupta
"""
import mysql.connector


def get_connection_to_database():
    connection = mysql.connector.connect(
        user="root", password="admin", host="localhost", database="KNOWT"
    )
    return connection


def DatabaseCreate(database_name):
    connection = mysql.connector.connect(
        user="root", password="admin", host="localhost"
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    cursor.close()
    connection.close()


def TablesCreate():
    connection = get_connection_to_database()
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Users(username varchar(30) Primary Key, password varchar(20))"
    )   
    cursor.close()
    connection.close()


def Authenticate(username, password):
    connection = get_connection_to_database()
    cursor = connection.cursor()
    query = "SELECT password from Users where username=%s"
    parameter = (username,)
    cursor.execute(query, parameter)
    result = cursor.fetchone()
    if result!=None :
        result = result[0]
    else :
        print('No records found')
        return False
    connection.close()
    if result == password:
        return True
    else:
        return False

def Register():
    connection = get_connection_to_database()
    cursor = connection.cursor()
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    query = "INSERT INTO Users (username, password) VALUES (%s, %s)"
    parameter = (user_name,password)
    cursor.execute(query, parameter)
    connection.commit()
    connection.close()
    print(f"\n\tUser {user_name} created and added to the database\n")


  
