#Creating tables
#DataBase Operations

###########################
import MySQLdb
import os
import shutil, errno
###########################
def connect():
    x=MySQLdb.connect('127.0.0.1', 'root', 'khaled', 'sts');
    return x
def disconnect():
    y=connect().close()
    return y
def initializing():
    try:
        connect()    
        cur = connect().cursor()
               

        CTAT="""CREATE TABLE attendance(StdID INT(9),SecID INT(9),absents INT(2),RegDate DATE)"""
        cur.execute(CTAT)
        #CTAT is a variable includes creating table for student's attendance.
        

        CTSM="""CREATE TABLE marks (StdID INT(9),SecID INT(9),FirstExamMark INT(2),SecondExamMark INT(2),PartisMark INT(2),FinalExamMark INT(2))"""
        cur.execute(CTSM)
        #CTSD is a variable includes creating table for student's marks.

        
        CTIN="""CREATE TABLE instructors (InstID INT(9) NOT NULL PRIMARY KEY,FName char(10),LName char(10),phone_no char(10),Email char(30))"""
        cur.execute(CTIN)
        #CTIN is a variable includes creating table for instructors.


        CTST="""CREATE TABLE students (StdID INT(9) NOT NULL PRIMARY KEY,FName char(10),LName char(10),phone_no char(10),Email char(30))"""
        cur.execute(CTST)
        #CTST is a variable includes creating table for students.


        CTSU="""CREATE TABLE subjects (SubjID INT(9) NOT NULL PRIMARY KEY,Name char(20),Description varchar(20))"""
        cur.execute(CTSU)
        #CTSU is a variable includes creating table for subjects.


        CTSE="""CREATE TABLE sections (SecID INT(9) NOT NULL,SubjID int(9),InstID int(9),Name char(20))"""
        cur.execute(CTSE)
        #CTSE is a variable includes creating table for sections.



        #Preparing for linking between tables.
        cur.execute("ALTER TABLE attendance ADD INDEX (StdID)")
        cur.execute("ALTER TABLE attendance ADD INDEX (SecID)")
        cur.execute("ALTER TABLE marks ADD INDEX (StdID)")
        cur.execute("ALTER TABLE marks ADD INDEX (SecID)")
        cur.execute("ALTER TABLE sections ADD INDEX (SecID)")
        cur.execute("ALTER TABLE sections ADD INDEX (SubjID)")
        cur.execute("ALTER TABLE sections ADD INDEX (InstID)")


        #Linking tables.
        cur.execute("ALTER TABLE attendance ADD FOREIGN KEY (StdID) REFERENCES sts.students (StdID)")
        cur.execute("ALTER TABLE attendance ADD FOREIGN KEY (SecID) REFERENCES sts.sections (SecID)")
        cur.execute("ALTER TABLE marks ADD FOREIGN KEY (StdID) REFERENCES sts.students (StdID)")
        cur.execute("ALTER TABLE marks ADD FOREIGN KEY (SecID) REFERENCES sts.sections (SecID)")
        cur.execute("ALTER TABLE sections ADD FOREIGN KEY (SubjID) REFERENCES sts.subjects (SubjID)")
        cur.execute("ALTER TABLE sections ADD FOREIGN KEY (InstID) REFERENCES sts.instructors (InstID)")

    except Exception:
        print ("You have created your DataBase Before")

    finally:
        disconnect()

def CLS(Command):
    try:
        con=connect()
        cur=con.cursor()
        cur.execute(Command)
        if "select" in Command :
            print cur.fetchall()
        else :
            con.commit()
    except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
    finally:
        disconnect()        

def Export():
    if os.path.exists("C:\\Users\\user\\Desktop\\BackUP\\sts"):
        shutil.rmtree("C:\\Users\\user\\Desktop\\BackUP\\sts")
    shutil.copytree("C:\\wamp\\bin\\mysql\\mysql5.5.20\\data\\sts","C:\\Users\\user\\Desktop\\BackUP\\sts")
    
def Import():
    if os.path.exists("C:\\wamp\\bin\\mysql\\mysql5.5.20\\data\\sts"):
        shutil.rmtree("C:\\wamp\\bin\\mysql\\mysql5.5.20\\data\\sts")
    shutil.copytree("C:\\Users\\user\\Desktop\\BackUP\\sts","C:\\wamp\\bin\\mysql\\mysql5.5.20\\data\\sts")
    
