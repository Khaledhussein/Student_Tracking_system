#Creating tables

###########################
import MySQLdb

###########################

try:
    con = MySQLdb.connect('127.0.0.1', 'root', '', 'aaa');

    cur = con.cursor()

    
    cur.execute("DROP TABLE IF EXISTS instructors")
    CTIN="""CREATE TABLE instructors (InstID INT(5) NOT NULL PRIMARY KEY,Name char(10) NOT NULL,SubID INT(6) NOT NULL)"""
    cur.execute(CTIN)
    #CTIN is a variable includes creating table for instructors.

    
    cur.execute("DROP TABLE IF EXISTS students")
    CTST="""CREATE TABLE students (Name char(20) NOT NULL,StdID INT(9) NOT NULL PRIMARY KEY,registry_date DATE NOT NULL,absents INT(2),Subgrade INT(3) NOT NULL, SubID INT(9))"""
    cur.execute(CTST)
    #CTST is a variable includes creating table for students.


    cur.execute("DROP TABLE IF EXISTS subjects")
    CTSU="""CREATE TABLE subjects (Name char(20) NOT NULL,SubID INT(9) NOT NULL PRIMARY KEY,registry_date DATE NOT NULL,absents INT(2),Stdgrade INT(3) NOT NULL,StdID INT(9),InsID INT(9))"""
    cur.execute(CTSU)
    #CTSU is a variable includes creating table for subjects.
    
    
    
    
    
except Exception,error:
  
    print (error)
    
finally:    
        
    if con:    
        con.close()
