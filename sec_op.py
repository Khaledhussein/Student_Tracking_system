#sections Operations

###########################
import MySQLdb
import DB_OP

###########################
def sec(SecID,Name,SubjID,InstID):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO sections (SecID,Name,SubjID,InstID) VALUES('%s','%s','%s','%s')"""%(SecID,Name,SubjID,InstID))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()


def query():
     try:
          con=DB_OP.connect()
     except Exception,r:
          print r
     Q=con.cursor()
     Q.execute("select * from sections")
     print Q.fetchall()


def delete(SecID,SubjID,InstID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("DELETE FROM sections WHERE SecID=%s AND SubjID =%s AND InstID=%s"%(SecID,SubjID,InstID))
     except Exception,error:
         print(error)
     finally:
          edit.commit()
          DP_OP.disconnect()
