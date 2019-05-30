"""
author: sky
desc: get_famous_teachers_by_school 表 es_institution es_teacher
"""
from nameko.rpc import rpc
import json
import os
# os.chdir("C:\zhangshuo\\nameko_demo")
# from Nameko.mydb import db
# from config import DB_CONFIG
import mydb
from config import DB_CONFIG
import pymysql

# 需要预先调用，且只调用一次
mydb.create_engine(**DB_CONFIG)


class Project(object):
    name = "project"

    @rpc
    def get_project_by_school_teacher(self, school_name, teacher_name, search_type):
        """
        根据学校名字和教师名字来获取其项目
        :param school_name:
        :param teacher_name:
        :return:
        """
        db = pymysql.connect(host='47.104.236.183', db='eds_spider', user='root', password='SLX..eds123', port=3306,
                             charset='utf8')
        cursor = db.cursor()
        # 从eds_spider 数据库的jijin表中得到的数据
        if type(search_type) is not "NoneType" and len(search_type) > 0:
            print("with type")
            sql = ("select * from jijin where org = %s and `name` = %s and type = %s order by year desc")
            cursor.execute(sql, (school_name, teacher_name, search_type))
            results = cursor.fetchall()
        else:
            print("no type")
            sql = ("select * from jijin where org = %s and `name` = %s order by year desc")
            cursor.execute(sql, (school_name, teacher_name))
            results = cursor.fetchall()

        # 从eds_spider 数据库的eval_project表中得到的数据
        sql2 = ("select * from eval_project where ORG = %s and Person = %s and type = %s")
        cursor.execute(sql2, (school_name, teacher_name, search_type))
        results2 = cursor.fetchall()
        print("-1"*50)
        print(results)
        print("-1"*50)

        return json.dumps(results, ensure_ascii=False), json.dumps(results2, ensure_ascii=False)


# p = Project()
# p.get_project_by_school_teacher("清华大学", "郑力", "")