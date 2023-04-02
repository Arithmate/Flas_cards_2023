from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests


list_cards_router = Blueprint("list_cards_router", __name__)


@list_cards_router.route("/list_cards/get_list/<small_category_id_str>", methods=['post'])
def get_list(small_category_id_str):
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/list_cards/get_list/{small_category_id_str}"

    response = requests.get(url=url, headers=headers)

    res_json = response.content.decode() if response.status_code == 200 else None

    return render_template('list_cards.html', res_json=res_json)