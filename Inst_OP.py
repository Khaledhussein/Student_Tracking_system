#Instructors operations
###########################
import MySQLdb
import DB_OP

###########################
def inst(InstID,FName,LName,phone_no,Email):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO instructors (InstID,FName,LName,phone_no,Email) VALUES('%s','%s','%s','%s','%s')"""%(InstID,FName,LName,phone_no,Email))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()


def updating(InstID,NInstID,FName,LName,phone_no,Email):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM instructors WHERE InstID =%s"%(InstID))
          cur.execute("""INSERT INTO instructors (InstID,FName,LName,phone_no,Email) VALUES('%s','%s','%s','%s','%s')"""%(NInstID,FName,LName,phone_no,Email))
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
     Q.execute("select * from instructors")
     print Q.fetchall()

def delete(InstID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM instructors WHERE SubjID =%s"%(InstID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DP_OP.disconnect()

