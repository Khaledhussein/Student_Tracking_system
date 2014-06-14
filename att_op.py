#Attendance Opeations
###########################
import MySQLdb
import DB_OP
###########################
def att(StdID,SecID,absents="NULL",RegDate="NULL"):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO attendance (StdID,SecID,absents,RegDate) VALUES(%s,%s,%s,%s)"""%(StdID,SecID,absents,RegDate))
     except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
     finally:
          con.commit()
          DB_OP.disconnect()

def update(StdID,SecID,NStdID,NSecID,absents,RegDate):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.attendance SET attendance.StdID=%s,attendance.SecID=%s,attendance.absents=%s,attendance.RegDate=%s WHERE attendance.StdID=%s AND attendance.SecID=%s"%(NStdID,NSecID,absents,RegDate,StdID,SecID))
     except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
     finally:
          edit.commit()
          DB_OP.disconnect()
def query():
     try:
          con=DB_OP.connect()
     except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
     Q=con.cursor()
     Q.execute("select * from attendance")
     return Q.fetchall()

def delete(StdID,SecID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM attendance WHERE StdID=%s AND SecID =%s"%(StdID,SecID))
     except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
     finally:
          edit.commit()
          DB_OP.disconnect()
def absents(StdID,SecID):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("select absents from attendance where StdID=%s AND SecID=%s"%(StdID,SecID))
          return cur.fetchall()
     except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
     finally:
          DB_OP.disconnect()
