from flask import Flask
from flask import request
from flask import render_template

import json
import requests

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    # TODO: index.htmlを返す
    if request.method == 'GET':
        return render_template('index.html', success_message='GET OK')

    else:
        return render_template('index.html', error_message='GET NG')


@app.route("/api/user_detail", methods=['GET', 'POST'])
def user():
    # TODO: jsonを返す
    if request.method == 'POST':

        res = "json_res"
        data_json_list = []
        data_map = {}

        name_list = ["前田", "山田", "太田", "中田", "村田"]
        job_list = ["課長", "主任", "一般", "一般", "一般"]

        for index in range(len(name_list)):
            data_map = {
                "user_name": name_list[index],
                "job": job_list[index]
            }
            data_json = json.dumps(data_map)

            data_json_list.append(data_json)

        # TODO: リストの各要素をSeparatorで繋げる
        data_json_sep_def = ""

        for single_data in data_json_list:
            data_json_sep_def += "Separator" + single_data

        data_json_sep = data_json_sep_def[9:len(data_json_sep_def)]

        # TODO: 繋がったjsonと通信成否確認文でjsonを作る
        response_message = "200"

        res_map = {
            "message": response_message,
            "content": data_json_sep
        }
        
        res = json.dumps(res_map)

        return res

    else:
        return render_template('index.html', error_message='POST error')


@app.route("/api/connect_sub", methods=['GET', 'POST'])
def sub():
    
    if request.method == 'GET':
        return render_template('index.html', error_message='POST error')
   
    else:
        url = "http://backend:9000"
        headers = {
            "content-Type": "application/json"
        }

        res = requests.get(url=url, headers=headers)
        json_response = json.loads(res.text)

        return json_response
