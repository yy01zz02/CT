    db.commit()
    cu.close()
    db.close()   
    return result

def FetchOne(dbname,table, condition=''):
    db = sqlite3.connect(dbname)  
    cu=db.cursor()
    if condition!='':
        condition="where %s"%condition
    records =cu.execute('''select * from %s %s'''%(table,condition))
    records =cu.fetchone()
    if records:
        result =list(records)
    else:
        result=None   
    db.commit()
    cu.close()
    db.close()   
    return result