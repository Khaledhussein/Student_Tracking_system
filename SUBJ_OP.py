#Subjects Opeations
###########################
import MySQLdb
import DB_OP
###########################
def subj(Name,SubjID,registry_date,StdID,InstID):
     try:
          con = DB_OP.connect()
          cur=con.cursor()
          cur.execute("""INSERT INTO subjects (Name,SubjID,registry_date,StdID,InstID) VALUES('%s','%s','%s','%s','%s')"""%(Name,SubjID,registry_date,StdID,InstID))
     except Exception,error:
          print(error)
     finally:
          con.commit()
          DB_OP.disconnect()

          
#updating function AND the insertion function did the same both updated the table
#Alwas there is no more than on field i really tried the only way now ican think of
#of is updating in another file
def updating(Nname,Name,nsubjid,SubjID,Nregistry_date,registry_date,nStdID,StdID,nInstID,InstID):
     try:
          edit = DB_OP.connect()
          cur=edit.cursor()
          cur.execute("update subjects set Name='%s' where name ='%s'"%(Nname,Name))
          cur.execute("update subjects set Subjid='%s' where subjid='%s'"%(nsubjid,SubjID))
          cur.execute("update subjects set registry_date='%s' where registry_date='%s'"%(Nregistry_date,registry_date))
          cur.execute("update subjects set StdID='%s' Where StdID='%s'"%(nStdID,StdID))
          cur.execute("update subjects set InstID='%s' where InstID='%s'"%(nInstID,InstID))
          
     except Exception,error:
          print(error)
     finally:
          edit.commit()
          DB_OP.disconnect()

subj("same7",1234,"2003-4-8",6546,654)
#updating("khaled0","khaled",1234,1230,"2003-4-4","2003-4-8",65460,6546,6540,654)
