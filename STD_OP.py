#students Operations

###########################
import MySQLdb
import DB_OP

###########################
def std(Name,StdID,regestiry_date,absents,SubGrade,SubID):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO students (Name,StdID,registry_date,absents,SubGrade,SubID) VALUES('%s','%s','%s','%s','%s','%s')"""%(Name,StdID,regestiry_date,absents,SubGrade,SubID))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()
