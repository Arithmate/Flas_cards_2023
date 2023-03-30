from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests

put_card_router = Blueprint("put_card_router", __name__)

@put_card_router.route("/put_card", methods=['put'])
def put():
    """
    バックエンドサーバーにアクセスしてアップデートを依頼
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
    url = host + "/detail_card/post"
    params = {
        "card_name":request.form["card_name"],
        "large_category_name":request.form["large_category_name"],
        "small_category_name":request.form["small_category_name"],
        "note_conent":request.form["note_conent"],
        "tag_name_list":tag_name_list,
        "significance":request.form["significance"],
        "study_state":request.form["study_state"],
    }

    res = requests.post(url=url, headers=headers, params=params)
    return json.loads(res.content)
