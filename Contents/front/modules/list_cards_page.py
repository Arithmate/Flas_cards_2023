from flask import Flask
from flask import request
from flask import render_template

import json
import requests

app = Flask(__name__)


@app.route("/list_cards/view", methods=['GET'])
def view():
    """
    htmlを表示
    """
    return render_template('list_cards.html', success_message='GET OK')


@app.route("/list_cards/get_list", methods=['GET'])
def get_list():
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:9000"
    url = host + "/list_cards/get_list"

    res = requests.get(url=url, headers=headers)
    return json.loads(res.text)


@app.route("/list_cards/put", methods=['PUT'])
def put():
    """
    バックエンドサーバーにアクセスしてインサートを依頼
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:9000"
    url = host + "/list_cards/put"

    res = requests.get(url=url, headers=headers)
    return json.loads(res.text)