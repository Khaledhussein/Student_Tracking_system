#Instructors operations
###########################
import MySQLdb
import DB_OP

###########################
def inst(InstID,FName="NULL",LName="NULL",phone_no="NULL",Email="NULL"):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO instructors (InstID,FName,LName,phone_no,Email) VALUES(%s,%s,%s,%s,%s)"""%(InstID,FName,LName,phone_no,Email))
     except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
     finally:
          con.commit()
          DB_OP.disconnect()


def update(InstID,NInstID,FName="NULL",LName="NULL",phone_no="NULL",Email="NULL"):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.instructors SET InstID=%s,FName=%s,LName=%s,Phone_no =%s,Email=%s WHERE instructors.InstID=%s"%(NInstID,FName,LName,phone_no,Email,InstID))
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
     Q.execute("select * from instructors")
     return Q.fetchall()
