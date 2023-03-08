from flask import Flask
from flask import request
from flask import render_template

import json

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():
    # TODO: jsonを返す
    if request.method == 'GET':

        res = "json_res"
        data_json_list = []
        data_map = {}

        name_list = ["前川","山川","大川","中川","村川"]
        job_list = ["課長","主任","一般","一般","一般"]

        for index in range (len(name_list)):
            data_map = {
                "user_name" : name_list[index],
                "job" : job_list[index]
            }
            data_json = json.dumps(data_map)

            data_json_list.append(data_json)

        # TODO: リストの各要素をSeparatorで繋げる
        data_json_sep_def = ""

        for single_data in data_json_list:
            data_json_sep_def += "Separator" + single_data

        data_json_sep = data_json_sep_def[9:len(data_json_sep_def)]

        response_message = "200"

        res_map = {
             "message" : response_message,
             "content" : data_json_sep
        }
        
        res = json.dumps(res_map)

        return res