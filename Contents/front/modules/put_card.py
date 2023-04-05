from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template

import json
import requests

put_card_router = Blueprint("put_card_router", __name__)

@put_card_router.route("/put_card/view/<card_id_str>", methods=['post'])
def view(card_id_str):
    """
    htmlを表示
    """

    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/detail_card/{card_id_str}"

    response = requests.get(url=url, headers=headers)

    res_json = response.content.decode() if response.status_code == 200 else None

    return render_template('put_card.html', res_json=res_json)


@put_card_router.route("/put_card/update", methods=['post'])
def put():
    """
    バックエンドサーバーにアクセスしてアップデートを依頼
    """

    card_id = request.form["card_id"]
    large_category_name = request.form["large_category_name"]
    small_category_name = request.form["small_category_name"]

    # ーーーーーーーーーーーーーーーーーーー
    # 失敗時のレスポンス用に詳細取得
    # ーーーーーーーーーーーーーーーーーーー
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/detail_card/{card_id}"

    get_response_for_error = requests.get(url=url, headers=headers)
    res_json_for_error = get_response_for_error.content.decode() if get_response_for_error.status_code == 200 else None

    # ーーーーーーーーーーーーーーーーーーー
    # 修正
    # ーーーーーーーーーーーーーーーーーーー
    if (not request.form["card_name"]
        or not large_category_name
        or not small_category_name
        ):


        return render_template(
            'put_card.html',
            message='「単語名・大分類・小分類」は必須入力です。',
            res_json=res_json_for_error,
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
    url = host + "/put_card"
    data = {
        "card_id":card_id,
        "card_name":request.form["card_name"],
        "large_category_name":large_category_name,
        "small_category_name":small_category_name,
        "note_content":request.form["note_content"],
        "tag_name_list":tag_name_list,
        "significance":request.form["significance"],
        "study_state":request.form["study_state"],
    }

    put_response = requests.put(url=url, headers=headers, data=json.dumps(data))

    if put_response.status_code != 200:
        return render_template(
            'put_card.html',
            message='使用できない文字が含まれています',
            res_json=res_json_for_error,
        )

    # ーーーーーーーーーーーーーーーーーーー
    # レスポンス用に詳細取得
    # ーーーーーーーーーーーーーーーーーーー
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/detail_card/{card_id}"

    get_response = requests.get(url=url, headers=headers)
    res_json = get_response.content.decode() if get_response.status_code == 200 else None

    return render_template(
        'put_card.html',
        message='修正に成功しました。',
        res_json=res_json,
    )


@put_card_router.route("/put_card/delete", methods=['post'])
def delete():
    """
    バックエンドサーバーにアクセスして削除を依頼
    """
    # ーーーーーーーーーーーーーーーーーーー
    # 削除
    # ーーーーーーーーーーーーーーーーーーー
    card_id_str = request.form["card_id"]
    print("delete=======", card_id_str)
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/put_card/delete/{card_id_str}"

    delete_response = requests.put(url=url, headers=headers)

    if delete_response.status_code != 200:

        # ーーーーーーーーーーーーーーーーーーー
        # レスポンス用に詳細取得
        # ーーーーーーーーーーーーーーーーーーー
        headers = {
            "content-Type": "application/json"
        }
        host = "http://backend:5006"
        url = host + f"/detail_card/{card_id_str}"

        get_response = requests.get(url=url, headers=headers)
        res_json = get_response.content.decode() if get_response.status_code == 200 else None

        return render_template(
            'put_card.html',
            message='使用できない文字が含まれています',
            res_json=res_json,
        )

    return render_template(
        'post_card.html',
        message='削除に成功しました。',
    )