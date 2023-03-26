from flask import Flask
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests

app = Flask(__name__)
CORS(app)

@app.route('/small_category/view', methods=['GET'])
def view():
    """
    htmlを表示
    """
    return render_template('small_category.html', success_message='GET OK')


@app.route("/small_category/get_list", methods=['GET'])
def get_list():
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:9000"
    url = host + "/small_category/get_list"

    res = requests.get(url=url, headers=headers)
    return json.loads(res.text)


@app.route("/small_category/put", methods=['PUT'])
def put():
    """
    バックエンドサーバーにアクセスしてインサートを依頼
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:9000"
    url = host + "/small_category/put"

    res = requests.get(url=url, headers=headers)
    return json.loads(res.text)

if __name__ =='__main__':
    app.run()