#Subjects Opeations
###########################
import MySQLdb
import DB_OP
###########################
def subj(SubjID,Name,description):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO subjects (SubjID,Name,description) VALUES('%s','%s','%s')"""%(SubjID,Name,description))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()

def updating(SubjID,NSubjID,Name,description)):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM subjects WHERE SubjID =%s"%(SubjID))
          cur.execute("""INSERT INTO subjects (SubjID,Name,description) VALUES('%s','%s','%s')"""%(NSubjID,Name,description))
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
     Q.execute("select * from subjects")
     print Q.fetchall()

def delete(SubjID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM subjects WHERE SubjID =%s"%(SubjID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DP_OP.disconnect()
