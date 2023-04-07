from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests

small_category_router = Blueprint("small_category_router", __name__)


@small_category_router.route("/small_list/get_list/<large_category_id_str>", methods=['get'])
def get_list(large_category_id_str):
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/small_list/get_list/{large_category_id_str}"

    response = requests.get(url=url, headers=headers)

    res_json = response.content.decode() if response.status_code == 200 else None

    return render_template('small_category.html', res_json=res_json)
