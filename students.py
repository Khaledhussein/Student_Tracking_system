#students insertion table

###########################
import MySQLdb

###########################
def std(Name,StdID,regestiry_date,absents,SubGrade,SubID):
     try:
          con = MySQLdb.connect('127.0.0.1','root', '', 'aaa');
          cur=con.cursor()
          cur.execute("""INSERT INTO students (Name,StdID,registry_date,absents,SubGrade,SubID) VALUES('%s','%s','%s','%s','%s','%s')"""%(Name,StdID,regestiry_date,absents,SubGrade,SubID))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          con.close()
