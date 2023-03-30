from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests


list_cards_router = Blueprint("list_cards_router", __name__)


@list_cards_router.route("/list_cards/view", methods=['GET'])
def view():
    """
    htmlを表示
    """
    return render_template('list_cards.html', success_message='GET OK')


@list_cards_router.route("/list_cards/get_list/<small_category_id_str>", methods=['GET'])
def get_list(small_category_id_str):
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/list_cards/get_list/{small_category_id_str}"

    res = requests.get(url=url, headers=headers)
    return json.loads(res.text)