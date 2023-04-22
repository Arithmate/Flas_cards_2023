from flask import Flask, Blueprint, redirect, url_for
from flask import request
from flask import render_template

import json
import requests

put_card_router = Blueprint("put_card_router", __name__)


@put_card_router.route("/put_card/view/<card_id_str>", methods=['post'])
def view(card_id_str):
    """
    単語詳細画面を表示する
    """

    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/detail_card/{card_id_str}"

    response = requests.get(url=url, headers=headers)

    res_json = response.content.decode() if response.status_code == 200 else None

    return render_template('put_card.html', res_json=res_json)


@put_card_router.route("/list_cards/get_list/<small_category_id_str>/<message>", methods=['get'])
def get_list_with_message(small_category_id_str, message):
    """
    単語一覧画面を表示して、メッセージを渡す
    削除・修正後の画面遷移用
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/list_cards/get_list/{small_category_id_str}"

    response = requests.get(url=url, headers=headers)

    res_json = response.content.decode() if response.status_code == 200 else None

    return render_template(
        'list_cards.html',
        message=message,
        res_json=res_json,
    )


@put_card_router.route("/put_card/update", methods=['post'])
def put():
    """
    単語の情報全てを修正する
    """
    card_id = request.form["card_id"]
    large_category_name = request.form["large_category_name"]
    small_category_name = request.form["small_category_name"]

    # ーーーーーーーーーーーーーーーーーーー
    # 修正
    # ーーーーーーーーーーーーーーーーーーー
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
        "card_id": card_id,
        "card_name": request.form["card_name"],
        "large_category_name": large_category_name,
        "small_category_name": small_category_name,
        "note_content": request.form["note_content"],
        "tag_name_list": tag_name_list,
        "significance": request.form["significance"],
        "study_state": request.form["study_state"],
        "sort_number": str(int(request.form["sort_number"]) - 1),
    }

    put_response = requests.put(
        url=url, headers=headers, data=json.dumps(data))

    if put_response.status_code != 200:

        # ーーーーーーーーーーーーーーーーーーー
        # 失敗時のレスポンス用に詳細取得
        # ーーーーーーーーーーーーーーーーーーー
        headers = {
            "content-Type": "application/json"
        }
        host = "http://backend:5006"
        url = host + f"/detail_card/{card_id}"

        get_response_for_error = requests.get(url=url, headers=headers)
        res_json_for_error = get_response_for_error.content.decode(
        ) if get_response_for_error.status_code == 200 else None

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
        message='変更を保存しました。',
        res_json=res_json,
    )


@put_card_router.route("/put_card/update_note/<small_category_id_str>", methods=['post'])
def put_note(small_category_id_str):
    """
    ノートを修正する
    """
    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + "/put_card"
    data = {
        "card_id": request.form["card_id"],
        "note_content": request.form["note_content"],
    }

    put_response = requests.put(
        url=url, headers=headers, data=json.dumps(data))
    
    if put_response.status_code != 200:
        return redirect(url_for(
            'put_card_router.get_list_with_message',
            small_category_id_str=small_category_id_str,
            message="変更を保存できませんでした。",
        ))

    return redirect(url_for(
        'put_card_router.get_list_with_message',
        small_category_id_str=small_category_id_str,
        message="ノートの変更を保存しました。",
    ))


@put_card_router.route("/put_card/delete/<small_category_id_str>", methods=['post'])
def delete(small_category_id_str):
    """
    単語を削除する
    """
    card_id = request.form["card_id"]

    # ーーーーーーーーーーーーーーーーーーー
    # 削除
    # ーーーーーーーーーーーーーーーーーーー

    headers = {
        "content-Type": "application/json"
    }
    host = "http://backend:5006"
    url = host + f"/put_card/delete/{card_id}"

    delete_response = requests.put(url=url, headers=headers)

    if delete_response.status_code != 200:

        # ーーーーーーーーーーーーーーーーーーー
        # 失敗時のレスポンス用に詳細取得
        # ーーーーーーーーーーーーーーーーーーー
        headers = {
            "content-Type": "application/json"
        }
        host = "http://backend:5006"
        url = host + f"/detail_card/{card_id}"

        get_response_for_error = requests.get(url=url, headers=headers)
        res_json_for_error = get_response_for_error.content.decode(
        ) if get_response_for_error.status_code == 200 else None
        
        return render_template(
            'put_card.html',
            message='削除できませんでした。',
            res_json=res_json_for_error,
        )

    return redirect(url_for(
        'put_card_router.get_list_with_message',
        small_category_id_str=small_category_id_str,
        message="単語を削除しました。",
    ))


