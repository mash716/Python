import pymysql
 
connector = pymysql.connect(
    host='localhost', 
    db='sdb', 
    user='root', 
    passwd='root', 
    charset='utf8',
)
cursor = connector.cursor()
 
sql = "insert into test_table values('1','python')"
cursor.execute(sql)
sql = "insert into test_table values('2','パイソン')"
cursor.execute(sql)
sql = "insert into test_table values('3','ぱいそん')"
cursor.execute(sql)
 
connector.commit()
 
cursor.close()
connector.close()