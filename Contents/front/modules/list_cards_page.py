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

    res_json = response.content if response.status_code == 200 else None

    res_json = json.dumps([
        {"card_id": "テストID1", "card_name": "テスト小分類1", "note_content": "テストノート1"},
        {"card_id": "テストID2", "card_name": "テスト小分類2", "note_content": "テストノート2"},
        {"card_id": "テストID3", "card_name": "テスト小分類3", "note_content": "テストノート3"},
    ])

    return render_template('list_cards.html', res_json=res_json)