import pymysql
db = pymysql.connect(host='47.104.236.183', db='eds_spider', user='root', password='SLX..eds123', port=3306,
                             charset='utf8')
cursor = db.cursor()
sql = ("select * from jijin where org = %s and `name` = %s order by year desc")
school_name = "清华大学"
teacher_name = "郑力"
cursor.execute(sql, (school_name, teacher_name))
results = cursor.fetchall()
print("results  ", results)