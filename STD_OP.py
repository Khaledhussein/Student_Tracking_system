#students Operations

###########################
import MySQLdb
import DB_OP

###########################
def std(StdID,FName,LName,phone_no,Email):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO students (StdID,FName,LName,phone_no,Email) VALUES('%s','%s','%s','%s','%s')"""%(StdID,FName,LName,phone_no,Email))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()


def updating(StdID,NStdID,FName,LName,phone_no,Email):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM students WHERE InstID =%s"%(StdID))
          cur.execute("""INSERT INTO studnets (StdID,FName,LName,phone_no,Email) VALUES('%s','%s','%s','%s','%s')"""%(NStdID,FName,LName,phone_no,Email))
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



def delete(StdID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM students WHERE StdID =%s"%(StdID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DP_OP.disconnect()
