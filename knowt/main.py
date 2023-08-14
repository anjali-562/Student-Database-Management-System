import Database
import Menulib
"""
Project : KnowT - Ultimate Portal for Teachers 
Author : Anjali Gupta
"""

def login():
    Menulib.clrscreen()
    print("=================================================================")
    print("*****************************************************************") 
    print("=================================================================\n") 
    print("\t\t\t LOGIN - Enter Your Credentials\n")
    print("=================================================================")
    print("*****************************************************************") 
    print("=================================================================\n")
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    
    response = Database.Authenticate(username=user_name, password=password)
    if response == True :
        print("*****************************************************************") 
        print(f"\t\t\tAuthentication Sussesfull! Welcome {user_name}")
        print("*****************************************************************") 

        
    else :
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        print(f"\t\t\tAuthentication Failed!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        welcome()



def welcome():
    Menulib.clrscreen()
    print("=================================================================")
    print("*****************************************************************") 
    print("=================================================================\n") 
    print("\t\tKnowT - Ultimate Portal for Teachers\n")
    print("=================================================================") 
    print("*****************************************************************")     
    print("=================================================================\n")
    print("1. Login")
    print("2. New User? Register ")

    choice = int(input("Enter Choice: "))

    while choice!=0:
        if choice == 1:
            login()
            break

        elif choice == 2 :
            Database.Register()
            welcome()
            break        

        elif choice == 0:
            print("Exiting...")
            break
        
        else:
            print("Wrong Choice.....Enter Your Choice again")
            choice = int(input("Enter Choice again: "))

def setup():
    Database.DatabaseCreate(database_name='KNOWT')
    Database.TablesCreate()

def start():
    Menulib.MainMenu()
        

if __name__ == "__main__" :
    setup()
    welcome()
    start()



