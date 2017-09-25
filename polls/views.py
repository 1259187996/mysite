from django.shortcuts import render

# Create your views here.

import pymysql



def showStudents(request):

    # pymysql.install_as_MySQLdb()
    #
    # # 打开数据库链接
    # conn = pymysql.connect("114.67.139.80", "root", "mysql_root", "im_status")
    #
    # # 使用cursor方式获取操作游标
    # cursor = conn.cursor()
    #
    # # 使用execute方式执行sql语句
    # cursor.execute("select * from t_user")
    #
    # # 使用fetchone方式获取一条数据
    # data = cursor._do_get_result()


  # list = [{id: 1, 'name': 'Jack'}, {id: 2, 'name': 'Rose'}]
    return  render(request,'student.html',{'students': data})