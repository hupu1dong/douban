import sqlite3

#创建数据表
# '''
# conn = sqlite3.connect("test.db")
#
# print("Opened database successfully!!")
#
# c = conn.cursor()   #获取游标
# sql1 = '''
#     drop table company;
# '''
# sql = '''
#         create table company
#             (id int primary key not null,
#             name text not null,
#             age int not null,
#             address char(50),
#             salary real);
# '''
# c.execute(sql1)
# c.execute(sql)  #执行sql语句
# conn.commit()   #提交数据库操作
# conn.close()    #关闭数据库连接
#
# print("成功建表")
# '''

#3.插入数据
# conn = sqlite3.connect("test.db")
#
# print("Opened database successfully!!")
#
# c = conn.cursor()   #获取游标
# sql = '''
#     insert into company (id,name,age,address,salary)
#         values (1,'张大屌',43,"杭州",8900);
# '''
# c.execute(sql)  #执行sql语句
# conn.commit()   #提交数据库操作
# conn.close()    #关闭数据库连接
#
# print("插入数据完毕！")

#4..查询数据

conn = sqlite3.connect("test.db")

print("Opened database successfully!!")

c = conn.cursor()   #获取游标
sql = '''
    select id,name,address,salary from company
'''
cursor = c.execute(sql)  #执行sql语句
for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3])

conn.close()    #关闭数据库连接

print("插入数据完毕！")
