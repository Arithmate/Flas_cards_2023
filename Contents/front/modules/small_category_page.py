from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests

small_category_router = Blueprint("small_category_router", __name__)


@small_category_router.route('/small_category/view', methods=['GET'])
def view():
    """
    htmlを表示
    """
    return render_template('small_category.html', success_message='GET OK')


@small_category_router.route("/small_category/get_list/<large_category_id_str>", methods=['GET'])
def get_list(large_category_id_str):
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/small_category/get_list/{large_category_id_str}"

    res = requests.get(url=url, headers=headers)
    print(res)

    res_list = ["小分類1", "小分類2", "小分類3"]

    return render_template('small_category.html', res_list=res_list)
