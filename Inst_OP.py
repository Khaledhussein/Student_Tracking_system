#Instructors operations
###########################
import MySQLdb
import DB_OP

###########################
def inst(Instid,Name,SubjID):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO instructors (InstID,Name,SubjID) VALUES('%s','%s','%s')"""%(Instid,Name,SubjID))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()


def updating(InstID,NinstID,Name,SubjID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM instructors WHERE InstID =%s"%(InstID))
          cur.execute("""INSERT INTO instructors (InstID,Name,SubjID) VALUES('%s','%s','%s')"""%(InstID,Name,SubjID))
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
