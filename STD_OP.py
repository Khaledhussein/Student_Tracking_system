#students Operations

###########################
import MySQLdb
import DB_OP

###########################
def std(Name,StdID,SubID):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO students (Name,StdID,SubID) VALUES('%s','%s','%s')"""%(Name,StdID,SubID))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()
