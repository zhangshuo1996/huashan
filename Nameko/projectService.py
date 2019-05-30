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

        # 从eds_spider 数据库的jijin表中得到的数据
        if type(search_type) is not "NoneType":
            sql = ("select * from jijin where org = ? and `name` = ? and type = ? order by year desc")
            results = mydb.select(sql, school_name, teacher_name, search_type)
        else:
            sql = ("select * from jijin where org = ? and `name` = ? order by year desc")
            results = mydb.select(sql, school_name, teacher_name)


        # 从eds_spider 数据库的eval_project表中得到的数据
        sql2 = ("select * from eval_project where ORG = ? and Person = ? and type = ?")

        results2 = mydb.select(sql2, school_name, teacher_name, search_type)
        print("-"*50)
        print(results)
        print("-"*50)

        return json.dumps(results, ensure_ascii=False), json.dumps(results2, ensure_ascii=False)


# p = Project()
# p.get_project_by_school_teacher("清华大学", "郑玉芬", "")