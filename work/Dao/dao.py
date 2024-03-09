import pymysql

conn=pymysql.connect(
    host='127.0.0.1',
    port=3308,
    user='root',
    password='root',
    charset='utf8',
    database='test'
)
#定义游标对象
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)



