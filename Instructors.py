#Instructors insertion
###########################
import MySQLdb

###########################
def inst(insid,insname,suid):
     try:
          con = MySQLdb.connect('127.0.0.1','root', '', 'aaa');
          cur=con.cursor()
          cur.execute("""INSERT INTO instructors (instid,name,subid) VALUES('%s','%s','%s')"""%(insid,insname,suid))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          con.close()
