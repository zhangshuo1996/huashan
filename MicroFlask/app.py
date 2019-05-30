from flask import Flask, request
from flask import render_template
import time
from nameko.standalone.rpc import ClusterRpcProxy
import json

from config import CONFIG

app = Flask(__name__)


@app.route('/')
def hello_world():

    return "hello world"


@app.route('/projects/search')
def project_info():
    school_name = request.args.get('search_school_name')
    teacher_name = request.args.get('search_teacher_name')
    search_type = request.args.get('search_type')

    with ClusterRpcProxy(CONFIG) as rpc:
        # 根据学校名字和教师名字获取项目
        results1, results2 = rpc.project.get_project_by_school_teacher(school_name, teacher_name, search_type)
        # print("--", results1)
        projects1 = json.loads(results1, encoding='utf8')
        projects2 = json.loads(results2)
        # print("?", type(projects))

        if len(results1) == 0 or len(results2) == 0:
            return {}
        print("--", projects1)
    return render_template("project.html", projects1=projects1, projects2=projects2, teacher_name=teacher_name, school_name=school_name)

# @app.route('/projects/<school_name>/<teacher_name>')
# def project_info(school_name, teacher_name):
#
#     with ClusterRpcProxy(CONFIG) as rpc:
#
#         # 根据学校名字和教师名字获取项目
#         result = rpc.project.get_project_by_school_teacher(school_name, teacher_name)
#         print("--", result)
#         projects = json.loads(result)
#         print("?", type(projects))
#
#         if len(result) == 0:
#             return {}
#
#     return render_template("project.html", projects=projects, teacher_name=teacher_name, school_name=school_name)

if __name__ == '__main__':
    app.run()
