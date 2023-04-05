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
        c.card_id
        ,c.card_name
        ,n.note_content
        ,s.small_category_name
        ,l.large_category_id
        ,l.large_category_name
    FROM
        Cards01 as c
    INNER JOIN
        Notes01 as n
    ON
        c.primal_note_id = n.note_id
    INNER JOIN
        SmallCategory01 as s
    ON
        c.small_category_id = s.small_category_id
    INNER JOIN
        LargeCategory01 as l
    ON
        s.large_category_id = l.large_category_id
    WHERE
        c.is_deleted = 0
        AND c.small_category_id = '{small_category_id_str}'
    ORDER BY
        c.sort_number
        ,c.registered_at;
    """
    record_list = select(sql)

    return json.dumps(record_list)

