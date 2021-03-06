#Subjects Opeations
###########################
import MySQLdb
import DB_OP
###########################
def subj(SubjID,Name="NULL",description="NULL"):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO subjects (SubjID,Name,description) VALUES(%s,%s,%s)"""%(SubjID,Name,description))
     except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
     finally:
          con.commit()
          DB_OP.disconnect()

def update(SubjID,NSubjID,Name,description):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.subjects SET SubjID=%s,Name=%s,description=%s WHERE subjects.SubjID=%s"%(NSubjID,Name,description,SubjID))
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
     Q.execute("select * from subjects")
     return Q.fetchall()

def delete(SubjID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM subjects WHERE SubjID =%s"%(SubjID))
     except MySQLdb.Error as err:
          print("Something went wrong: {}".format(err[1]))
     finally:
          edit.commit()
          DB_OP.disconnect()
