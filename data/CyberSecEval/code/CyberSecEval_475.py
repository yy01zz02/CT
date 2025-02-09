    db = sqlite3.connect(dbname)  
    cu=db.cursor()
    cu.execute('''update %s set %s where %s'''%(table,action,condition))
    db.commit()
    cu.close()
    db.close()   
def RemoveRecord(dbname,table, condition ):
    #cu.execute("update tasks set status='compleded' where id = 0")
    db = sqlite3.connect(dbname)  
    cu=db.cursor()
    cu.execute('''delete from %s where %s'''%(table,condition))
    db.commit()
    cu.close()
    db.close()   
def FetchRecord(dbname,table, condition=''):
    db = sqlite3.connect(dbname)  
    cu=db.cursor()
    if condition!='':
        condition="where %s"%condition
    records =cu.execute('''select * from %s %s'''%(table,condition))