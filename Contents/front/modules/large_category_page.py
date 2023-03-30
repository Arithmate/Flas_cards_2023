from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template
import json
import requests

large_category_router = Blueprint("large_category_router", __name__)

@large_category_router.route("/", methods=['GET'])
def view():
    """
    htmlを表示
    """
    return render_template('large_category.html', success_message='GET OK')


@large_category_router.route("/large_category/view", methods=['GET'])
def root():
    """
    htmlを表示
    """
    return render_template('large_category.html', success_message='GET OK')


@large_category_router.route("/large_category/get_list", methods=['GET'])
def get_list():
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + "/large_category/get_list"

    res = requests.get(url=url, headers=headers)

    print("#ーーーーーーーーーーーーーー")
    print(res.content)
    print("#ーーーーーーーーーーーーーー")

    res_list = ["大分類1", "大分類2", "大分類3"]

    return render_template('large_category.html', res_list=res_list)
