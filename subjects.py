#Subjects insetion table
###########################
import MySQLdb

###########################
def sub(Name,SubID,registry_date,absents,Stdgrade,StdID,InsID):
     try:
          con = MySQLdb.connect('127.0.0.1','root', '', 'aaa');
          cur=con.cursor()
          cur.execute("""INSERT INTO subjects (Name,SubID,registry_date,absents,Stdgrade,StdID,InsID) VALUES('%s','%s','%s','%s','%s','%s','%s')"""%(Name,SubID,registry_date,absents,Stdgrade,StdID,InsID))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          con.close()

sub("python",0125,'2014-03-10',2,99,2010,0215)
