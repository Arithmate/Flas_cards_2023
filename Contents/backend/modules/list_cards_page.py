from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template
from lib.db_util import select, insert

import json

list_cards_router = Blueprint("list_cards_router", __name__)

@list_cards_router.route("/list_cards/get_list/<small_category_id_str>", methods=['GET'])
def get_list(small_category_id_str):
    """
    DBにアクセスしてデータを取得
    jsonデータを返却
    """
    sql = f"""
    SELECT 
        HEX(card_id)
        ,card_name
        ,HEX(primal_note_id)
    FROM
        Cards01
    WHERE
        is_deleted = 0
        AND small_category_id = UNHEX({small_category_id_str})
    ORDER BY
        sort_number
        ,registered_at;
    """
    record_list = select(sql)
    card_id_list = []
    card_name_list = []
    note_id_list = []

    for record in record_list:
        card_id_list.append(record["card_id"])
        card_name_list.append(record["card_name"])
        note_id_list.append(record["primal_note_id"])

    return {
        "card_list": record_list,
        "card_id_list": card_id_list,
        "card_name_list": card_name_list,
        "card_and_note_id_list": note_id_list,
    }

