

import os
from SQLoperate import Judgment
import SQLoperate as sql
from SQLoperate import AdminOption
from SQLoperate import StudentOption
import getpass
from time import sleep

os.system("TITLE Student Course Management System v2.1")

def Menu():
    print("""\n\n\n\n                               =======================================================
    \n\n\n                                       Welcome to Student Selection System          
    \n\n\n                               =======================================================
    \n\n\n                                     ----------Press any key to continue---------- 
    \n\n\n""")
    os.system("pause")
    os.system("cls")



def Login():

    z=0

    while True:
        os.system("cls")
        ID=input("\n\nPlease enter your ID:\n>>>")
        PD=getpass.getpass("\n\nPlease enter your Password:\n>>>")
        if(z==3):
            print("\n\nYou have entered the wrong three times and the program will exit ! ! !")
            break
        if(ID=="admin"):
            if(sql.adminJudge(ID,PD)):
                z=0
                os.system("cls")
                afterLogin(ID)
                AdminOptions()
                break
            else:
                z=z+1
                print("\n\nThe entered account or password is incorrect ! ! !({}/3)".format(z))
                sleep(2)
        else:
            if(sql.Judgment(ID,PD)):
               z=0
               os.system("cls")
               afterLogin(ID)
               Options(ID)
               break
            else:
               z=z+1
               print("\n\nThe entered account or password is incorrect ! ! !({}/3)".format(z))
               sleep(2)



def afterLogin(ID):

    if(ID=="admin"):
        ID="Administrator"

    print("""\n\n\n\n                               =======================================================
    \n\n\n                                             Welcome  back  ， """+ID+" ! "+
    """\n\n\n                               =======================================================
    \n\n\n                                     ----------Press any key to continue---------- \n\n\n""")

    os.system("pause")
    os.system("cls")

    if ID !="Administrator":
        sql.Stu_Inf(ID)

    sleep(2)
    os.system("cls")



def Options(ID):
    stu=StudentOption
    while True:
        a=input("""\n\n\n\n*****************************************************************
        \n\n\n 1、 View selected course number
        \n\n\n 2、 View course information
        \n\n\n 3、 Enter the course selection system 
        \n\n\n 4、 Change Password 
        \n\n\n 5、 Quit 
        \n\n\n*****************************************************************
        \n\n\n>>>""")

        os.system("cls")

        if a=="1":
            stu.View_selected_course_number(ID)
            sleep(2)
            os.system("cls")

        elif a=="2":
            
            stu.View_Cour_Inf()
            sleep(2)
            os.system("cls")

        elif a=="3":

            os.system("cls")

            Course_Selection_System(ID)

        elif a=="4":
            
            stu.Change_PD(ID)
            sleep(2)
            os.system("cls")

        elif a=="5":
            break
        else:
            print("Please enter as required !")
            sleep(2)

def AdminOptions():
    ad=AdminOption
    while True:
        a=input("""\n\n\n\n*****************************************************************
        \n\n\n 1、 View user information
        \n\n\n 2、 Add student account
        \n\n\n 3、 Delete student account
        \n\n\n 4、 Change account password  
        \n\n\n 5、 Quit
        \n\n\n*****************************************************************
        \n\n\n>>>""")
        os.system("cls")

        if a=="1":

            ad.View_User()
            sleep(2)
            os.system("cls")
            
        elif a=="2":

            ad.Add_Stu_Acc()
            sleep(2)
            os.system("cls")

        elif a=="3":
            
            ad.Delete_User()
            sleep(2)
            os.system("cls")

        elif a=="4":

            ad.Change_PD()
            sleep(2)
            os.system("cls")
            
        elif a=="5":
            break
        else:
            print("Please enter as required !")
            sleep(2)

def Course_Selection_System(ID):
    stu=StudentOption
    while(True):
        a=input("""\n\n\n\n*****************************************************************
        \n\n\n 1、 View selected course number
        \n\n\n 2、 View course information
        \n\n\n 3、 Add Course 
        \n\n\n 4、 Delete course 
        \n\n\n 5、 Quit 
        \n\n\n*****************************************************************
        \n\n\n>>>""")
        
        os.system("cls")

        if a=="1":

            stu.View_selected_course_number(ID)
            sleep(2)
            os.system("cls")
        
        elif a=="2":

            stu.View_Cour_Inf()
            sleep(2)
            os.system("cls")

        elif a=="3":
            
            stu.Cour_Selection(ID)
            sleep(2)
            os.system("cls")

        elif a=="4":
            
            stu.Delete_course(ID)
            sleep(2)
            os.system("cls")

        elif a=="5":
            break

        else:
            print("Please enter as required !")
            sleep(2)
