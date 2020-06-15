import os
import platform

list_student=['user1','user2','user3','user4'] # list of student

def showdata(data):# function for Student Management System
    print("""\nWelcome to Student Management System \n
Enter1 : To View Students Name
Enter2 : To Add Students Name
Enter3 : To Search Student Name
Enter4 : To Remove Student Name \n""")
    
    try:# use for when user enter valid input
        user_input=int(input("Please Select an above option: "))
    except:#when user input a string then show error
        exit("\nInvalid Option")
        
    else:# if except not run then else is run
        if(user_input==1):#This Option Will Print List Of Students
            print("\nThe List of students: \n")
            for student in data:
                print(f"==> {student}")
                
        elif(user_input==2):#This Option Will Add New Student In The List
            new_student=input("\nEnter a New Student Name: ")
            if (new_student in data):#This Condition Checking The New Student
                print(f"\nThis Student {new_student} already in the Database")
            else:
                data.append(new_student)
                print(f"\n=> New Student {new_student} is successfully added \n")
                for student in data:
                    print(f"==> {student}")

        elif(user_input==3):#This Option Will Search Student From The List
            search_student=input("\nEnter Student Name to Search: ")
            if(search_student in data):#This Condition Searching The Student
                print(f"\nRecord Found of student {search_student}")
            else:
                print(f"\n=> No Record Found of this student {search_student}")

        elif(user_input==4):#This Option Will Remove Student From The List
            remove_student=input("\nEnter Student Name to remove: ")
            if(remove_student in data):#This Condition Removing The Student From The List
                data.remove(remove_student)
                print(f"\nStudent {remove_student} Successfully Removed \n")
                for show_data in data:
                    print(show_data)
            else:
                print(f"\n=> No Record Found of This student {remove_student}")

        else:#Validating User Option
            print("\nYou Enter a invalid Option")

showdata(list_student)#calling a function and pass a list

while True:#making a runable program
    yes_no=input("\nWant to you run again yes/ no?: ")
    if yes_no.lower()=='y':
        if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        showdata(list_student)
        
    else:
        exit("\nInvalid Input")
