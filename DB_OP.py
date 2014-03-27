#Creating tables
#DataBase Operations

###########################
import MySQLdb

###########################
def connect():
    x=MySQLdb.connect('127.0.0.1', 'root', '', 'sad');
    return x
def disconnect():
    y=connect().close()
    return y
try:
    connect()
    
    cur = connect().cursor()


    cur.execute("DROP TABLE IF EXISTS instructors")
    CTIN="""CREATE TABLE instructors (InstID INT(9) NOT NULL PRIMARY KEY,Name char(10) NOT NULL,SubjID INT(9) NOT NULL)"""
    cur.execute(CTIN)
    #CTIN is a variable includes creating table for instructors.

    cur.execute("DROP TABLE IF EXISTS students")
    CTST="""CREATE TABLE students (Name char(20) NOT NULL,StdID INT(9) NOT NULL PRIMARY KEY,registry_date DATE NOT NULL,absents INT(2), SubjID INT(9))"""
    cur.execute(CTST)
    #CTST is a variable includes creating table for students.


    cur.execute("DROP TABLE IF EXISTS subjects")
    CTSU="""CREATE TABLE subjects (Name char(20) NOT NULL,SubjID INT(9) NOT NULL PRIMARY KEY,registry_date DATE NOT NULL,StdID INT(9),InstID INT(9))"""
    cur.execute(CTSU)
    #CTSU is a variable includes creating table for subjects.

    #making relations
   # cur.execute("""ALTER TABLE instructors ADD FOREIGN KEY (SubjID) REFERENCES  Subjects (SubjID)""")
   # cur.execute("""ALTER TABLE students ADD FOREIGN KEY (SubjID) REFERENCES  Subjects (SubjID)""")
    #cur.execute("""ALTER TABLE subjects ADD FOREIGN KEY (stdid) REFERENCES  students (stdid)""")
    #cur.execute("""ALTER TABLE subjects ADD FOREIGN KEY (instid) REFERENCES  instructors (instid)""") #failed idk why!!!!!!!!!!!!!
    
    
except Exception,error:
  
    print (error)
    
finally:
    disconnect()
