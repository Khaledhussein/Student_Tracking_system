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