from flask import Flask
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests

app = Flask(__name__)
CORS(app)

@app.route("/detail_card/view", methods=['GET'])
def view():
    """
    htmlを表示
    """
    return render_template('detail_card.html', success_message='GET OK')


@app.route("/detail_card/get_list", methods=['GET'])
def get_list():
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:9000"
    url = host + "/detail_card/get_list"

    res = requests.get(url=url, headers=headers)
    return json.loads(res.text)


@app.route("/detail_card/put", methods=['PUT'])
def put():
    """
    バックエンドサーバーにアクセスしてインサートを依頼
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:9000"
    url = host + "/detail_card/put"

    res = requests.get(url=url, headers=headers)
    return json.loads(res.text)

if __name__ =='__main__':
    app.run()