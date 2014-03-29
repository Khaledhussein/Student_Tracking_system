#students Operations

###########################
import MySQLdb
import DB_OP

###########################
def std(Name,StdID,SubjID):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO students (Name,StdID,SubjID) VALUES('%s','%s','%s')"""%(Name,StdID,SubjID))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()

def updating(StdID,NstdID,Name,SubjID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM students WHERE StdID =%s"%(StdID))
          cur.execute("""INSERT INTO students (Name,StdID,SubjID) VALUES('%s','%s','%s')"""%(Name,NstdID,SubjID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()

def query():
     try:
          con=DB_OP.connect()
     except Exception,r:
          print r
     Q=con.cursor()
     Q.execute("select * from students")
     print Q.fetchall()
