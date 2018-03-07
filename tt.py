#encoding: utf-8

from pymysql import cursors, connect

# 连接数据库
conn = connect(host = '127.0.0.1',
               user = 'root',
               password = 'password',
               db = 'guest',
               charset = 'utf8mb4',
               cursorclass = cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        #创建嘉宾数据
        sql = 'INSERT INTO firstTest_guest (realname, phone, email, sign,  create_time, event_id) VALUES ("tom", 18800001001, "tom@mail.com", 0, now(), 1);'
        cursor.execute(sql)
        #提交事务
        conn.commit()
    #
    # with conn.cursor() as cursor:
    #     sql = "select realname,phone,email,sign from firstTest_guest where phone=%s"
    #     cursor.execute(sql, ('18800001001',))
    #     result = cursor.fetchone()
    #     print(result)
finally:
    conn.close()

