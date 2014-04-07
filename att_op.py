#Attendance Opeations
###########################
import MySQLdb
import DB_OP
###########################
def att(StdID,SecID,absents,RegDate):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO attendance (StdID,SecID,absents,RegDate) VALUES('%s','%s','%s','%s')"""%(StdID,SecID,absents,RegDate))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()

def updating(StdID,SecID,NStdID,NSecID,absents,RegDate):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM attendance WHERE StdID =%s AND SecID=%s"%(StdID,SecID))
          cur.execute("""INSERT INTO attendance (StdID,SecID,absents,RegDate) VALUES('%s','%s','%s','%s')"""%(NStdID,NSecID,absents,RegDate))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DP_OP.disconnect()
def query():
     try:
          con=DB_OP.connect()
     except Exception,r:
          print r
     Q=con.cursor()
     Q.execute("select * from attendance")
     print Q.fetchall()

def delete(StdID,SecID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM attendance WHERE StdID=%s AND SecID =%s"%(StdID,SecID))
     except Exception,error:
          print(error)
     finally:
          edit.commit()
          DP_OP.disconnect()
