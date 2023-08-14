import Acadmic
import Stats
import platform
import os
import Student


def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))

def enter_to_continue():
    n =input("Enter any key contiue")
    clrscreen()

def MenuDataManagement():
    clrscreen()
    while True:
        print("\t\t\tSTUDENT DATA MANAGEMENT\n")
        print("=====================================================================")
        print("1. Student Acadamic data Management")
        print("2. Student Stats Viewer")
        print("0. Return to Main Menu")
        print("=================================================================")

        choice = int(input("Enter Choice: "))
        if choice == 1:
            MenuAcadmic()
        elif choice == 2:
            MenuStats()        
        elif choice == 0:
            return 
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Press any key to continue: ")


def MainMenu():
    clrscreen()
    while True:
        print("\t\t\t Select Action\n")
        print("=================================================================")
        print("1. Add New Class to the Database")
        print("2. Update Information for present class")       
        print("3. View Student Data")       
        print("4. Student Data Management")       
        print("0. Return to Main Menu")
        print("=================================================================")
        choice = int(input("Enter Choice between 1 to 3 ------> : "))
        if choice == 1:
            Student.insertData()
            enter_to_continue()
        elif choice == 2:
            Student.updateData()     
            enter_to_continue()   
        elif choice == 3:
            Student.viewData()   
            enter_to_continue()     
        elif choice == 4:
            MenuDataManagement() 
            enter_to_continue()
        elif choice == 0:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuAcadmic():
    clrscreen()

    while True:
        # clrscreen()
        print("\t\t\t STUDENT ACADMIC DATA MANAGEMENT\n")
        print("=================================================================")
        print("1. Add Student Record")
        print("2. Delete Student Record")
        print("3. Update Student Record")
        print("4. View Record")
        print("5. Return to Main Menu")
        print("=================================================================")
        choice = int(input("Enter Choice between 1 to 5 ------> : "))
        if choice == 1:
            Acadmic.insertData() 
            enter_to_continue()       
        elif choice == 2:
            Acadmic.deleteData()
            enter_to_continue()
        elif choice == 3:
            Acadmic.updateData()
            enter_to_continue()
        elif choice == 4:
            Acadmic.viewData()
            enter_to_continue()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuStats():
    clrscreen()
    while True:
        print("\t\t\t STUDENT STATS VIEWER\n")
        print("=================================================================")
        print("1. View Gender Distribution")
        print("2. View Marks Distribution")
        print("0. Return to previous Menu")
        print("=================================================================")
        choice = int(input("Enter Choice between 1 to 5 ------> : "))
        if choice == 1:
            Stats.show_gender_plot()
            enter_to_continue()
        elif choice == 2:
            Stats.show_marks_plot()
            enter_to_continue()
       
        elif choice == 0:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")


