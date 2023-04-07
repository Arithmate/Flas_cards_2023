from flask import Flask, Blueprint, redirect
from flask import render_template
import requests

large_category_router = Blueprint("large_category_router", __name__)

@large_category_router.route("/", methods=['GET'])
def view():
    """
    htmlを表示
    """
    host = "http://localhost:5005"
    url = host + "/large_list/get_list"

    return redirect(url) 


@large_category_router.route("/large_list/get_list", methods=['get'])
def get_list():
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + "/large_list/get_list"

    response = requests.get(url=url, headers=headers)

    res_json = response.content.decode() if response.status_code == 200 else None

    return render_template('large_category.html', res_json=res_json)
