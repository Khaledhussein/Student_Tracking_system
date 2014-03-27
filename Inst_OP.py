#Instructors operations
###########################
import MySQLdb
import DB_OP

###########################
def inst(insid,insname,suid):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO instructors (instid,name,subjid) VALUES('%s','%s','%s')"""%(insid,insname,suid))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()
