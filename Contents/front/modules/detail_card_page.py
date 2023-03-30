from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests

detail_card_router = Blueprint("detail_card_router", __name__)


@detail_card_router.route("/detail_card/view", methods=['GET'])
def view():
    """
    htmlを表示
    """
    return render_template('detail_card.html', success_message='GET OK')


@detail_card_router.route("/detail_card/<card_id_str>", methods=['GET'])
def get_list(card_id_str):
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/detail_card/{card_id_str}"

    res = requests.get(url=url, headers=headers)
    return json.loads(res.text)
