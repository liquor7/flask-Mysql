import MySQLdb
db=MySQLdb.connect("localhost","root","199403","recommend")
cursor=db.cursor()
sql="create table user_anime(user int,anime int)"
cursor.execute(sql)
db.close()