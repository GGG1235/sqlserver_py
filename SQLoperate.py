
import pyodbc
import os
from getpass import getpass

cnxn= pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=SCMS;UID=sa;PWD=1997') 

def Connection():
    try:
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=SCMS;UID=sa;PWD=1997')
    except:
        print("Error")

def Judgment(ID,PD):
    Connection()
    cursor = cnxn.cursor()
    
    Str="""select * from Student_Information
where studentID="""+"'"+ID+"' "+"and "+"password='"+PD+"'"

    cursor.execute(Str)
    row=cursor.fetchone()
    if(row==None):
        return False
    else:
        return True


#    while True:
#       row= cursor.fetchone()
#       if not row:
#          break
#       print(row)

def adminJudge(ID,PD):
    Connection()
    cursor = cnxn.cursor()
    
    Str="""select * from Admin_Information
where ID="""+"'"+ID+"' "+"and "+"PD='"+PD+"'"

    cursor.execute(Str)
    row=cursor.fetchone()
    if(row==None):
        return False
    else:
        return True

#    while True:
#       row= cursor.fetchone()
#       if not row:
#          break
#       print(row)


def Stu_Inf(ID):
    Connection()
    cursor=cnxn.cursor()

    Str="""select * from Student_Account
    where studentID='"""+ID+"'"

    cursor.execute(Str)
    row=cursor.fetchone()

    splt="\n\t{:10}\t{:10}\t{:16}\t{:10}\n"

    print(splt.format("studentID","studentName","studentSex","studentClass"))
    print(splt.format(row.studentID,row.studentName,row.studentSex,row.studentClass))

#    while True:
#       row= cursor.fetchone()
#       if not row:
#          break
#       print(row)

class StudentOption:
    def __init__(self):
        return super().__init__(*args, **kwargs)

    def View_selected_course_number(ID):
        Connection()
        cursor=cnxn.cursor()
        splt="\tCoureID:{}\tCoureName:{}\tLecturer:{}\n"

        SQL="""select Select_Course_Conditions.CouresID,Course_Information.CoureName,Course_Information.Lecturer from Course_Information,Select_Course_Conditions
        where Select_Course_Conditions.CouresID=Course_Information.CoureID and Select_Course_Conditions.studentID= '"""+ID+"'"

        print("\n\n\tID : {}\n".format(ID))
        cursor.execute(SQL)
        row=cursor.fetchone()
        if row is None:
            print("\n\tNo course selected ! ! !\n")
        else:
            cursor.execute(SQL)
            while True:
                row=cursor.fetchone()
                if not row:
                    break
                print(splt.format(row.CouresID,row.CoureName,row.Lecturer))

    def View_Cour_Inf():
        Connection()
        cursor=cnxn.cursor()
        Str="""select * from Course_Information"""
        
        cursor.execute(Str)
        splt="{:10}\t{:16}\t{:10}"
        print(splt.format("CoureID","CoureName","Lecturer"))
        while True:
            row=cursor.fetchone()
            if not row:
                break
            print(splt.format(row.CoureID,row.CoureName,row.Lecturer))

        In=input("""\n\nPlease enter the course ID you are looking for\n>>>""")
        print("\n\n\n")
        if In=="exit" or In=="quit" or In=="n" or In=="N":
            print("Exiting ! ! !")
        else:
            In1="'%"+In+"%'"
            Str1=Str+""" where CoureID LIKE """+In1
            cursor.execute(Str1)
            print(splt.format("CoureID","CoureName","Lecturer"))
            while True:
                row=cursor.fetchone()
                if not row:
                    break
                print(splt.format(row.CoureID,row.CoureName,row.Lecturer))

    def  Cour_Selection(ID):
        courNum=input("\n\nPlease enter the course ID you want to choose\n>>>")
        
        ID="'"+ID+"'"
        courNum="'"+courNum+"'"
        Together="("+ID+","+courNum+")"

        Connection()
        cursor=cnxn.cursor()

        Sql1="""select * from Course_Information where coureID = """+courNum
        Sql2="""select * from Select_Course_Conditions where studentID ="""+ID+" and CouresID = "+courNum

        cursor.execute(Sql1)
        row1=cursor.fetchone()

        cursor.execute(Sql2)
        row2=cursor.fetchone()

        if row1 is None:
            print("\n\nThe course ID you entered does not exist ! ! !\n")
        elif row2 is not None:
            print("\n\nYou have selected this course ! ! !\n")
        else:
            Sql="INSERT INTO Select_Course_Conditions (studentID,CouresID) VALUES "+Together

            cursor.execute(Sql)
            cnxn.commit()

            print("\n\nSuccessful class selection !\n")

    def Delete_course(ID):
        courNum=input("\n\nPlease enter the course ID you want to deselect\n>>>")

        ID="'"+ID+"'"
        courNum="'"+courNum+"'"
        Together="("+ID+","+courNum+")"

        Connection()
        cursor=cnxn.cursor()

        Sql1="""select * from Select_Course_Conditions where studentID="""+ID+" and CouresID = "+courNum

        cursor.execute(Sql1)
        row1=cursor.fetchone()

        if row1 is None:
            print("\n\nYou did not choose this course\n")
        else:
            Sql="""DELETE FROM Select_Course_Conditions WHERE studentID = """+ID+" AND CouresID = "+courNum

            cursor.execute(Sql)
            cursor.commit()

            print("\n\nSuccessful withdrawal !\n")

    def Change_PD(ID):
        
        PD=getpass("\n\nplease enter your password\n>>>")

        ID="'"+ID+"'"
        PD="'"+PD+"'"
        sql="""SELECT * FROM Student_Information WHERE studentID= """+ID+" AND password="+PD

        Connection()
        cursor=cnxn.cursor()

        cursor.execute(sql)
        row=cursor.fetchone()

        if row is None:
            print("\n\nwrong password !\n")
        else:
            PD1=getpass("\n\nPlease enter the password you want to change\n>>>")

            PD2=getpass("\n\nPlease re-enter the password you want to change\n>>>")    

            if PD1==PD2:

                SQL0="""UPDATE Student_Information 
    SET password = '"""+PD1+"""'  
    WHERE
	studentID = """+ID
                cursor.execute(SQL0)
                cursor.commit()

                print("\n\nPassword changed successfully !\n")

            else:
                print("\n\nThe password entered twice is different !\n")



class AdminOption:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def View_User():
        Connection()
        cursor=cnxn.cursor()
        Str="""select * from Student_Account"""
        
        cursor.execute(Str)
        splt="{:10}\t{:10}\t{:16}\t{:10}"
        print(splt.format("studentID","studentName","studentSex","studentClass"))
        while True:
            row=cursor.fetchone()
            if not row:
                break
            print(splt.format(row.studentID,row.studentName,row.studentSex,row.studentClass))

        In=input("""\n\nPlease enter the keyword you want to query\n>>>""")
        print("\n\n\n")
        if In=="exit" or In=="quit" or In=="n" or In=="N":
            print("Exiting ! ! !")
        else:
            In1="'%"+In+"%'"
            Str1=Str+""" where studentID LIKE """+In1+"""
           or studentName LIKE """+In1+"""
          or studentClass LIKE """+In1+""";"""
            cursor.execute(Str1)
            print(splt.format("studentID","studentName","studentSex","studentClass"))
            while True:
                row=cursor.fetchone()
                if not row:
                    break
                print(splt.format(row.studentID,row.studentName,row.studentSex,row.studentClass))

    def Change_PD():
        ID=input("\n\nPlease enter the account ID you want to modify\n>>>")

        sql="""SELECT * FROM Student_Account WHERE studentID= '"""+ID+"'"

        Connection()
        cursor=cnxn.cursor()

        cursor.execute(sql)
        row=cursor.fetchone()

        if ID=="exit" or ID=="quit" or ID=="n" or ID=="N":
            print("Exiting ! ! !")
        elif row is None:
            print("The account ID you entered does not exist ! ! !")
        else:
            PD=getpass("\n\nPlease enter the password you want to modify\n>>>")
            ID="'"+ID+"'"
            PD="'"+PD+"'"
            Connection()
            cursor=cnxn.cursor()
            sql="""UPDATE Student_Information 
    SET password = """+PD+""" 
    WHERE
	studentID = """+ID

            cursor.execute(sql)
            cnxn.commit()
            print("\n\nSuccessfully modified ! ")
        
    def Delete_User():
        ID=input("\n\nPlease enter the account ID you want to delete\n>>>")
        if ID=="exit" or ID=="quit" or ID=="n" or ID=="N":
            print("Exiting ! ! !")
        else:
            ID="'"+ID+"'"

            sql_sel_cour_con0="""SELECT * FROM Select_Course_Conditions WHERE studentID ="""+ID

            Connection()
            cursor=cnxn.cursor()
            cursor.execute(sql_sel_cour_con0)
            row=cursor.fetchone()


#           Connection()
#           cursor=cnxn.cursor()

            sql_stu_Info="""DELETE FROM Student_Information WHERE studentID = """+ID
            sql_stu_Acc="""DELETE FROM Student_Account WHERE studentID = """+ID
            sql_sel_cour_con="""DELETE FROM Select_Course_Conditions WHERE studentID = """+ID
        

            if row==None:
                sql=sql_stu_Info+" "+sql_stu_Acc
            else:
                sql=sql_stu_Info+" "+sql_sel_cour_con+" "+sql_stu_Acc

            cursor.execute(sql)
            cnxn.commit()
            print("\n\nsuccessfully deleted ! ")

    def Add_Stu_Acc():
        ID=input("\n\nPlease enter the student ID you want to add\n>>>")

        sql="""SELECT * FROM Student_Account WHERE studentID= '"""+ID+"'"

        Connection()
        cursor=cnxn.cursor()

        cursor.execute(sql)
        row=cursor.fetchone()

        if ID=="exit" or ID=="quit" or ID=="n" or ID=="N":
            
            print("Exiting ! ! !")

        elif row is not None:
            
            print("\n\nThe ID you want to add already exists ！")

        else:
            Name=input("\n\nPlease enter the student Name you want to add\n>>>")
            Sex=input("\n\nPlease enter the student Sex you want to add\n>>>")
            Class=input("\n\nPlease enter the student Class you want to add\n>>>")
            password=getpass("\n\nPlease enter the student password you want to add\n>>>")

            ID="'"+ID+"'"
            Sex="'"+Sex+"'"
            Name="'"+Name+"'"
            Class="'"+Class+"'"
            password="'"+password+"'"

            Together0="("+ID+","+Name+","+Sex+","+Class+")"
            Together1="("+ID+","+password+")"

            sql_stu_Acc="""INSERT INTO Student_Account (studentID,studentName,studentSex,studentClass) VALUES """+Together0
            sql_stu_Info="""INSERT INTO Student_Information (studentID,password) VALUES """+Together1

            sql=sql_stu_Acc+" "+sql_stu_Info

            cursor.execute(sql)
            cnxn.commit()

            print("\n\nAdded successfully ! ")