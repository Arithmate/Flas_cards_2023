from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template
from lib.db_util import select, insert

import json

large_category_router = Blueprint("large_category_router", __name__)


@large_category_router.route("/large_category/get_list", methods=['GET'])
def get_list():
    """
    DBにアクセスしてデータを取得
    jsonデータを返却
    """
    sql = f"""
    SELECT 
        HEX(large_category_id)
        ,large_category_name
    FROM
        LargeCategory01
    WHERE
        is_deleted = 0
    ORDER BY
        sort_number
        ,registered_at;
    """
    record_list = select(sql)
    large_category_name_list = []
    large_category_id_list = []

    for record in record_list:
        large_category_id_list.append(record["large_category_id"])
        large_category_name_list.append(record["large_category_name"])

    return {
        "large_category_list": record_list,
        "large_category_id_list": large_category_id_list,
        "large_category_name_list": large_category_name_list,
    }

