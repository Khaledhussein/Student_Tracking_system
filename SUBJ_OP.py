#Subjects Opeations
###########################
import MySQLdb
import DB_OP
###########################
def subj(SubjID,Name,StdID,InstID):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO subjects (SubjID,Name,StdID,InstID) VALUES('%s','%s','%s','%s')"""%(SubjID,Name,registry_date,StdID,InstID))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()

def updating(SubjID,NSubjID,Name,StdID,InstID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM subjects WHERE SubjID =%s"%(SubjID))
          cur.execute("""INSERT INTO subjects (SubjID,Name,StdID,InstID) VALUES('%s','%s','%s','%s')"""%(NSubjID,Name,StdID,InstID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()
