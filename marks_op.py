#marks operations
###########################
import MySQLdb
import DB_OP

###########################
def Fmark(StdID,SecID,FirstExamMark="NULL"):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO marks (StdID,SecID,FirstExamMark) VALUES(%s,%s,%s)"""%(StdID,SecID,FirstExamMark))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()
def Smark(StdID,SecID,SecondExamMark="NULL"):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.marks SET SecondExamMark=%s WHERE students.StdID=%s AND students.SecID=%s)"%(SecondExamMark,StdID,SecID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()
def Pmark(StdID,SecID,PartisMark="NULL"):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.marks SET PartisMark=%s WHERE students.StdID=%s AND students.SecID=%s)"%(PartisMark,StdID,SecID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()
def Fimark(StdID,SecID,FinalMark="NULL"):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.marks SET FinalMark=%s WHERE students.StdID=%s AND students.SecID=%s)"%(FinalMark,StdID,SecID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()




def update(StdID,SecID,NStdID,NSecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.marks SET StdID=%s,SecID=%s,FirstExamMark=%s,SecondExamMark=%s,PartisMark=%s,FinalExamMark=%s WHERE students.StdID=%s AND students.SecID=%s)"%(NStdID,NSecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark,StdID,SecID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()


def querymarks(StdID,SecID):
     try:
          con=DB_OP.connect()
          Q=con.cursor()
          Q.execute("select * from marks WHERE StdID =%s AND SecID=%s"%(StdID,SecID))
          x= Q.fetchall()
          z=x[0][2:]
          return z 
     except Exception,r:
          print r


def query():
     try:
          con=DB_OP.connect()
     except Exception,r:
          print r
     Q=con.cursor()
     Q.execute("select * from marks")
     print Q.fetchall()


Fmark(1,1,2)
