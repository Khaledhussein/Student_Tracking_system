#Info operations
###########################
import MySQLdb
import DB_OP

###########################
def info(StdID,SubjID,RegDate,absents):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO info (StdID,SubjID,RegDate,absents) VALUES('%s','%s','%s','%s')"""%(StdID,SubjID,RegDate,absents))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()

def updating(StdID,NStdID,SubjID,RegDate,absents):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM info WHERE StdID =%s"%(StdID))
          cur.execute("""INSERT INTO info (StdID,SubjID,RegDate,absents) VALUES('%s','%s','%s','%s')"""%(NStdID,SubjID,RegDate,absents))
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
     Q.execute("select * from info")
     print Q.fetchall()
