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
    res_json = json.dumps([{}])
    return render_template(
        'post_card.html',
        success_message='GET OK',
        res_json=res_json,
    )


@post_card_router.route("/post_card/insert", methods=['post'])
def post():
    """
    単語カードを作成
    """
    res_json = json.dumps([{}])
    card_name = request.form["card_name"]
    large_category_name = request.form["large_category_name"]
    small_category_name = request.form["small_category_name"]

    if (not card_name
            or not large_category_name
            or not small_category_name
        ):
        return render_template(
            'post_card.html',
            message='「単語名・大分類・小分類」は必須入力です。',
            res_json=res_json,
        )

    if request.form.get("is_separator"):
        # しおりフラグONの場合、しおり作成APIを呼ぶ
        headers = {
            "content-Type": "application/json"
        }
        separator_host = "http://backend:5006"
        separator_url = separator_host + "/post_card/separator"
        separator_data = {
            "card_name": card_name,
            "large_category_name": large_category_name,
            "small_category_name": small_category_name,
        }

        separator_response = requests.post(url=separator_url, headers=headers, data=json.dumps(separator_data))

        if separator_response.status_code != 200:
            return render_template(
                'post_card.html',
                message='しおり作成に失敗しました。',
                res_json=res_json,
            )

        res_json = separator_response.content.decode() if separator_response.status_code == 200 else None

        return render_template(
            'post_card.html',
            message='しおり作成に成功しました。',
            res_json=res_json,
        )

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
        "card_name": card_name,
        "large_category_name": large_category_name,
        "small_category_name": small_category_name,
        "note_content": request.form["note_content"],
        "tag_name_list": tag_name_list,
        "significance": request.form["significance"],
        "study_state": request.form["study_state"],
    }

    post_response = requests.post(
        url=url, headers=headers, data=json.dumps(data))

    if post_response.status_code != 200:
        return render_template(
            'post_card.html',
            message='使用できない文字が含まれています',
            res_json=res_json,
        )

    res_json = post_response.content.decode() if post_response.status_code == 200 else None

    return render_template(
        'post_card.html',
        message='登録に成功しました。',
        res_json=res_json,
    )
