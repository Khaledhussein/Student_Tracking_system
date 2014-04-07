#marks operations
###########################
import MySQLdb
import DB_OP

###########################
def marks(StdID,SecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark):
     try:
          con=DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO marks (StdID,SecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark) VALUES('%s','%s','%s','%s','%s','%s')"""%(StdID,SecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()



def updating(StdID,SecID,NStdID,NSecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM info WHERE StdID =%s AND SecID=%s"%(StdID,SecID))
          cur.execute("""INSERT INTO marks (StdID,SecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark) VALUES('%s','%s','%s','%s','%s','%s')"""%(NStdID,NSecID,FirstExamMark,SecondExamMark,PartisMark,FinalExamMark))
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
     Q.execute("select * from marks")
     print Q.fetchall()

def delete(StdID,SecID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM marks WHERE StdID=%s AND SecID =%s"%(StdID,SecID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DP_OP.disconnect()

