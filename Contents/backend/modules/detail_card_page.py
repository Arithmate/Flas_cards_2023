from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template
from lib.db_util import select, insert

import json

detail_card_router = Blueprint("detail_card_router", __name__)

@detail_card_router.route("/detail_card/<card_id_str>", methods=['GET'])
def get_detail(card_id_str):
    """
    DBにアクセスしてデータを取得
    jsonデータを返却
    """
    sql = f"""
    SELECT 
        HEX(c.card_id)
        ,c.card_name
        ,c.significance
        ,c.study_state

        ,l.large_category_name

        ,s.small_category_name

        ,n.note_content
    FROM
        Cards01 as c
    INNER JOIN
        LargeCategory01 as l
    ON
        c.large_category_id = l.large_category_id
    INNER JOIN
        SmallCategory01 as s
    ON
        c.small_category_id = s.small_category_id
    INNER JOIN
        Notes01 as n
    ON
        c.primal_note_id = s.note_id
    WHERE
        c.is_deleted = 0
        AND c.card_id = UNHEX({card_id_str})
    ORDER BY
        c.sort_number
        ,c.registered_at;
    """
    record = select(sql)[0]

    return {"card_detail": record}

