#marks operations
###########################
import MySQLdb
import DB_OP

###########################
def Fmark(StdID,SecID,FirstExamMark="NULL"):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO marks (StdID,SecID,FirstExamMark) VALUES(%d,%d,%d)"""%(StdID,SecID,FirstExamMark))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()
def Smark(StdID,SecID,SecondExamMark="NULL"):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.marks SET SecondExamMark=%d WHERE marks.StdID=%d AND marks.SecID=%d"%(SecondExamMark,StdID,SecID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()
def Pmark(StdID,SecID,PartisMark="NULL"):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.marks SET PartisMark=%d WHERE marks.StdID=%d AND marks.SecID=%d"%(PartisMark,StdID,SecID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()
def Fimark(StdID,SecID,FinalExamMark="NULL"):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.marks SET FinalExamMark=%d WHERE marks.StdID=%d AND marks.SecID=%d"%(FinalExamMark,StdID,SecID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()




def update(StdID,SecID,NStdID,NSecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("UPDATE sts.marks SET StdID=%d,SecID=%d,FirstExamMark=%d,SecondExamMark=%d,PartisMark=%d,FinalExamMark=%d WHERE marks.StdID=%d AND marks.SecID=%d"%(NStdID,NSecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark,StdID,SecID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()


def querymarks(StdID,SecID):
     try:
          con=DB_OP.connect()
          Q=con.cursor()
          Q.execute("select * from marks WHERE StdID =%d AND SecID=%d"%(StdID,SecID))
          x= Q.fetchall()
          return x 
     except Exception,r:
          print r


def query():
     try:
          con=DB_OP.connect()
     except Exception,r:
          print r
     Q=con.cursor()
     Q.execute("select * from marks")
     return Q.fetchall()
