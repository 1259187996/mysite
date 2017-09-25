import pymysql

pymysql.install_as_MySQLdb()

# 打开数据库链接
conn = pymysql.connect("114.67.139.80","root","mysql_root","im_status")

# 使用cursor方式获取操作游标
cursor = conn.cursor()

# 使用execute方式执行sql语句
cursor.execute("select version()")

# 使用fetchone方式获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库
conn.close()