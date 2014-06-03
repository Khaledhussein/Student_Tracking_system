import MySQLdb
import DB_OP
import inst_op
import marks_op
import att_op
import std_op
import subj_op
import sec_op

print """
                      ############################################
                      #                                          #  
                      #    Welcome To Student Tracking System    #
                      #                                          #
                      ############################################
"""
try:
     CNDB=input("To create your database please press 1 , If you already have a database press anykey \n")
     if CNDB ==1:
          DB_OP.initializing()
     else:
          print "You have now a database"

except Exception,r:
     print (r)


while True:
     print """
Please select your category:
(1) Instructors operations
(2) Students operations
(3) Subjects operations
(4) Sections operations
(5) Attendance operations
(6) Marks operations
(7) Make your own MySQL statement
(8) Exit
"""
     select=input("\n")
     if select==1:
          while True:
               print"""
Select your operation:
(1) Add new instructor
(2) Update instructos
(3) Show all instructors
(4) Exit
"""
               Iselect=input("\n")
               if Iselect == 1:
                    InstID=input("Please insert the Instructor ID: ")
                    FName=raw_input("Please insert the instructor's First Name: ")
                    FName="\'"+FName+"\'"
                    LName=raw_input("Please insert the instructor's Last Name: ")
                    LName="\'"+LName+"\'"
                    phone_no=raw_input("Please insert the instructor's phone number: ")
                    phone_no="\'"+phone_no+"\'"
                    Email=raw_input("Please insert the instructor's Email: ")
                    Email="\'"+Email+"\'"
                    inst_op.inst(InstID,FName,LName,phone_no,Email)
               elif Iselect == 2:
                    InstID=input("Please insert the old Instructor ID: ")
                    NInstID=input("Please insert the new Instructor ID: ")
                    FName=raw_input("Please insert the new instructor's First Name: ")
                    FName="\'"+FName+"\'"
                    LName=raw_input("Please insert the new instructor's Last Name: ")
                    LName="\'"+LName+"\'"
                    phone_no=raw_input("Please insert the new instructor's phone number: ")
                    phone_no="\'"+phone_no+"\'"
                    Email=raw_input("Please insert the new instructor's Email: ")
                    Email="\'"+Email+"\'"
                    inst_op.update(InstID,NInstID,FName,LName,phone_no,Email)
               elif Iselect == 3:
                    A=inst_op.query()
                    print "----------------------------------------------------------------------------------------------------------------------------"
                    print ("|\tInstID\t       | | FirstName\t        | |      LastName\t | | Phone No.\t          | |        Email         |")
                    print "----------------------------------------------------------------------------------------------------------------------------"
                    x=[]
                    for i in A:
                         x.append(list(i))
                    for i in range (0,len(x)):
                         x[i][0]=int(x[i][0])
                    for row in x:
                         for val in row:
                              print "|","{:20}".format(val),"|",
                         print
                    print "----------------------------------------------------------------------------------------------------------------------------"
               elif Iselect == 4:
                    break
     elif select == 2:
          while True:
               print"""
Select your operation
(1) Add new student
(2) Update student
(3) Show all students
(4) Exit
"""
               STselect=input("\n")
               if STselect == 1:
                    StdID=input("Please insert the Student's ID: ")
                    FName=raw_input("Please insert the Student's First Name: ")
                    FName="\'"+FName+"\'"
                    LName=raw_input("Please insert the Student's Last Name: ")
                    LName="\'"+LName+"\'"
                    phone_no=raw_input("Please insert the Student's phone number: ")
                    phone_no="\'"+phone_no+"\'"
                    Email=raw_input("Please insert the Student's Email: ")
                    Email="\'"+Email+"\'"
                    std_op.std(StdID,FName,LName,phone_no,Email)
               elif STselect == 2:
                    StdID=input("Please insert the old student's ID: ")
                    NStdID=input("Please insert the new student's ID: ")
                    FName=raw_input("Please insert the new Student's First Name: ")
                    FName="\'"+FName+"\'"
                    LName=raw_input("Please insert the new Student's Last Name: ")
                    LName="\'"+LName+"\'"
                    phone_no=raw_input("Please insert the new Student's phone number: ")
                    phone_no="\'"+phone_no+"\'"
                    Email=raw_input("Please insert the new Student's Email: ")
                    Email="\'"+Email+"\'"
                    std_op.update(StdID,NStdID,FName,LName,phone_no,Email)
               elif STselect == 3:
                    A=std_op.query()
                    print "----------------------------------------------------------------------------------------------------------------------------"
                    print ("|\tStdID \t       | | FirstName\t        | |      LastName\t | | Phone No.\t          | |        Email         |")
                    print "----------------------------------------------------------------------------------------------------------------------------"
                    x=[]
                    for i in A:
                         x.append(list(i))
                    for i in range (0,len(x)):
                         x[i][0]=int(x[i][0])
                    for row in x:
                         for val in row:
                              print "|","{:20}".format(val),"|",
                         print
                    print "----------------------------------------------------------------------------------------------------------------------------"
               elif STselect == 4:
                    break
     elif select == 3:
          while True:
               print """
Select your operation
(1) Add new subject
(2) Update subject
(3) Show all subjects
(4) Delete a subject
(5) Exit
"""
               Suselect=input("\n")
               if Suselect == 1:
                    SubjID=input("Please insert the subject's ID: ")
                    Name=raw_input("Please Insert the subject's Name: ")
                    Name="\'"+Name+"\'"
                    description=raw_input("Please insert the subject's description: ")
                    description="\'"+description+"\'"
                    subj_op.subj(SubjID,Name,description)
               elif Suselect == 2:
                    SubjID=input("Please insert the old subject's ID: ")
                    NSubjID=input("Please insert the new subject's ID: ")
                    Name=raw_input("Please Insert the subject's Name: ")
                    Name="\'"+Name+"\'"
                    description=raw_input("Please insert the subject's description: ")
                    description="\'"+description+"\'"
                    subj_op.update(SubjID,NSubjID,Name,description)
               elif Suselect == 3:
                    A=subj_op.query()
                    print "--------------------------------------------------------------------------"
                    print ("|\tSubjID\t       | | Subject's Name\t| |    Description\t |")
                    print "--------------------------------------------------------------------------"
                    x=[]
                    for i in A:
                         x.append(list(i))
                    for i in range (0,len(x)):
                         x[i][0]=int(x[i][0])
                    for row in x:
                         for val in row:
                              print "|","{:20}".format(val),"|",
                         print
                    print "--------------------------------------------------------------------------"
               elif Suselect == 4:
                    SubjID=input("Please insert the subject's ID you want to delete: ")
                    subj_op.delete(SubjID)
               elif Suselect == 5:
                    break
     elif select == 4:
          while True:
               print"""
Select your operation
(1) Add new section
(2) Delete a section
(3) Show all sections
(4) Exit
"""
               Seselect = input("\n")
               if Seselect == 1:
                    SecID=input("Please insert the section's ID: ")
                    SubjID=input("Please insert the Subject that will be taught in this section: ")
                    InstID=input("Please insert the instructor's ID who will teach this Subject: ")
                    Name=raw_input("Please insert the section's name: ")
                    Name="\'"+Name+"\'"
                    sec_op.sec(SecID,SubjID,InstID,Name)
               elif Seselect == 2:
                    SecID=input("Please insert the section's ID: ")
                    SubjID=input("Please insert the Subject's ID: ")
                    InstID=input("Please insert the instructor's ID: ")
                    sec_op.delete(SecID,SubjID,InstID)
               elif Seselect == 3:
                    A=sec_op.query()
                    print "---------------------------------------------------------------------------------------------------"
                    print ("|\tSecID\t       | | SubjID        \t| |    InstID   \t | | Name\t\t  |")
                    print "---------------------------------------------------------------------------------------------------"
                    x=[]
                    for i in A:
                         x.append(list(i))
                    for i in range (0,len(x)):
                         x[i][0]=int(x[i][0])
                    for row in x:
                         for val in row:
                              print "|","{:20}".format(val),"|",
                         print
                    print "---------------------------------------------------------------------------------------------------"
               elif Seselect == 4:
                    break
     elif select == 5:
          while True:
               print"""
Please select your operation
(1) Add new attendance file
(2) Update an attendance file
(3) Show all attendance files
(4) Delete an attendance file
(5) Exit
"""
               Atselect=input("\n")
               if Atselect == 1:
                    StdID=input("Please insert the student's ID: ")
                    SecID=input("Please insert the section's ID: ")
                    absents=input("Please insert the absents of the student: ")
                    RegDate=raw_input("Please insert the regestery date (yyyy-mm-dd)")
                    RegDate="\'"+RegDate+"\'"
                    att_op.att(StdID,SecID,absents,RegDate)
               elif Atselect == 2:
                    StdID=input("Please insert the student's old ID: ")
                    SecID=input("Please insert the section's old ID: ")
                    NStdID=input("Please insert the student's new ID: ")
                    NSecID=input("Please insert the section's new ID: ")
                    absents=input("Please insert the absents of the student: ")
                    RegDate=raw_input("Please insert the regestery date (yyyy-mm-dd)")
                    RegDate="\'"+RegDate+"\'"
                    att_op.update(StdID,SecID,NStdID,NSecID,absents,RegDate)
               elif Atselect == 3:
                    A=att_op.query()
                    print "---------------------------------------------------------------------------------------------------"
                    print ("|\tStdID \t       | | SecID         \t| |    Absents  \t | |RegDate\t\t|")
                    print "---------------------------------------------------------------------------------------------------"
                    x=[]
                    for i in A:
                         x.append(list(i))
                    for i in range (0,len(x)):
                         x[i][0]=int(x[i][0])
#RegDate format problem
                    for row in x:
                         for val in row:
                              print "|","{:20}".format(val),"|",
                         print
                    print "---------------------------------------------------------------------------------------------------"
               elif Atselect == 4:
                    SecID=input("Please insert the section's ID: ")
                    StdID=input("Please insert the student's ID: ")
                    att_op.delete(StdID,SecID)
               elif Atselect == 5:
                    break
     elif select == 6:
          while True:
               print"""
Please select your operation
(1) Add the first exam mark
(2) Add the second exam mark
(3) Add the participation mark
(4) Add the participation mark(depending on absents)
(5) Add the final exam mark
(6) Update marks
(7) Show marks for one student
(8) Show all marks
(9) Exit
"""
               Maselect=input("\n")
               if Maselect==1:
                    StdID=input("Please insert the student's ID: ")
                    SecID=input("Please insert the section's ID: ")
                    FirstExamMark=input("Please insert the exam's mark: ")
                    marks_op.Fmark(StdID,SecID,FirstExamMark)
               elif Maselect == 2:
                    StdID=input("Please insert the student's ID: ")
                    SecID=input("Please insert the section's ID: ")
                    SecondExamMark=input("Please insert the exam's mark: ")
                    marks_op.Smark(StdID,SecID,SecondExamMark)
               elif Maselect == 3:
                    StdID=input("Please insert the student's ID: ")
                    SecID=input("Please insert the section's ID: ")
                    PartisMark=input("Please insert the participation mark: ")
                    marks_op.Pmark(StdID,SecID,PartisMark)
               elif Maselect == 4:
                    StdID=input("Please insert the student's ID: ")
                    SecID=input("Please insert the section's ID: ")
                    PartisMark=input("Please insert the participation mark: ")
                    absents=int(att_op.absents(StdID,SecID)[0][0])
                    Fpm=PartisMark-absents
                    marks_op.Pmark(StdID,SecID,Fpm)
               elif Maselect == 5:
                    StdID=input("Please insert the student's ID: ")
                    SecID=input("Please insert the section's ID: ")
                    FinalExamMark=input("Please insert the exam's mark: ")
                    marks_op.Fimark(StdID,SecID,FinalExamMark)
               elif Maselect == 6:
                    StdID=input("Please insert the old student's ID: ")
                    SecID=input("Please insert the old section's ID: ")
                    NStdID=input("Please insert the new student's ID: ")
                    NSecID=input("Please insert the new section's ID: ")
                    FirstExamMark=input("Please insert the new first exam's mark: ")
                    SecondExamMark=input("Please insert the new second exam's mark: ")
                    PartisMark=input("Please insert the new participation mark: ")
                    FinalExamMark=input("Please insert the new final exam's mark: ")
                    marks_op.update(StdID,SecID,NStdID,NSecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark)
               elif Maselect == 7:
                    StdID=input("Please insert the student's ID: ")
                    SecID=input("Please insert the section's ID: ")
                    A=marks_op.querymarks(StdID,SecID)
                    print "-----------------------------------------------------------------------------------------------------------"
                    print ("| StdID         | | SecID\t  | | First Exam    | | Second Exam   | | Participation | | Final Exam    |")
                    print "-----------------------------------------------------------------------------------------------------------"
                    x=[]
                    for i in A:
                         x.append(list(i))
                    for i in range (0,len(x)):
                         x[i][0]=int(x[i][0])
                    for row in x:
                         for val in row:
                              print "|","{:13}".format(val),"|",
                         print
                    print "-----------------------------------------------------------------------------------------------------------"
               elif Maselect == 8:
                    A=marks_op.query()
                    print "-----------------------------------------------------------------------------------------------------------"
                    print ("| StdID         | | SecID\t  | | First Exam    | | Second Exam   | | Participation | | Final Exam    |")
                    print "-----------------------------------------------------------------------------------------------------------"
                    x=[]
                    for i in A:
                         x.append(list(i))
                    for i in range (0,len(x)):
                         x[i][0]=int(x[i][0])
                    for row in x:
                         for val in row:
                              print "|","{:13}".format(val),"|",
                         print
                    print "-----------------------------------------------------------------------------------------------------------"
               elif Maselect == 9:
                    break
     elif select == 7:
          while True:
               print"""
(1) Write your own MySQL statment
(2) Exit
"""
               LL=input("\n")
               if LL == 1:
                    DB_OP.CLS()
               elif LL == 2:
                    break
     elif select == 8:
          print "Bye Bye :)"
          break
