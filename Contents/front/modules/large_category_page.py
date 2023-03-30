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
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + "/large_category/get_list"

    response = requests.get(url=url, headers=headers)

    res_json = response.content if response.status_code == 200 else None

    res_json = json.dumps([
        {"large_category_id": "テストID1", "large_category_name": "テスト大分類1"},
        {"large_category_id": "テストID2", "large_category_name": "テスト大分類2"},
        {"large_category_id": "テストID3", "large_category_name": "テスト大分類3"},
    ])

    return render_template('large_category.html', res_json=res_json)


@large_category_router.route("/large_category/get_list", methods=['post'])
def get_list():
    """
    バックエンドサーバーにアクセスしてjsonデータを取得
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + "/large_category/get_list"

    response = requests.get(url=url, headers=headers)

    res_json = response.content if response.status_code == 200 else None

    res_json = json.dumps([
        {"large_category_id": "テストID1", "large_category_name": "テスト大分類1"},
        {"large_category_id": "テストID2", "large_category_name": "テスト大分類2"},
        {"large_category_id": "テストID3", "large_category_name": "テスト大分類3"},
    ])

    return render_template('large_category.html', res_json=res_json)
