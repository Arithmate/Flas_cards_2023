from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests

post_card_router = Blueprint("post_card_router", __name__)

@post_card_router.route("/post_card/view", methods=['post'])
def view():
    """
    htmlを表示
    """
    return render_template('post_card.html', success_message='GET OK')

@post_card_router.route("/post_card/insert", methods=['post'])
def post():
    """
    バックエンドサーバーにアクセスしてインサートを依頼
    """
    tag_name_list = [
        request.form["tag_name_0"] or "",
        request.form["tag_name_1"] or "",
        request.form["tag_name_2"] or "",
        request.form["tag_name_3"] or "",
        request.form["tag_name_4"] or "",
    ]

    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + "/post_card"
    data = {
        "card_name":request.form["card_name"],
        "large_category_name":request.form["large_category_name"],
        "small_category_name":request.form["small_category_name"],
        "note_conent":request.form["note_conent"],
        "tag_name_list":tag_name_list,
        "significance":request.form["significance"],
        "study_state":request.form["study_state"],
    }

    requests.post(url=url, headers=headers, data=json.dumps(data))

    return render_template('post_card.html', success_message='GET OK')
