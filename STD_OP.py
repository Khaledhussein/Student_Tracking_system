#students Operations

###########################
import MySQLdb
import DB_OP

###########################
def std(StdID,FName="NULL",LName="NULL",phone_no="NULL",Email="NULL"):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO students (StdID,FName,LName,phone_no,Email) VALUES(%s,%s,%s,%s,%s)"""%(StdID,FName,LName,phone_no,Email))
     except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
     finally:
          con.commit()
          DB_OP.disconnect()


def update(StdID,NStdID,FName,LName,phone_no,Email):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.students SET StdID=%s,FName=%s,LName=%s,Phone_no =%s,Email=%s WHERE students.StdID=%s"%(NStdID,FName,LName,phone_no,Email,StdID))
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
     Q.execute("select * from students")
     return Q.fetchall()

