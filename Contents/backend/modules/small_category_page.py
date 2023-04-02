from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template
from lib.db_util import select, insert

import json

small_category_router = Blueprint("small_category_router", __name__)

@small_category_router.route("/small_category/get_list/<large_category_id_str>", methods=['GET'])
def get_list(large_category_id_str):
    """
    DBにアクセスしてデータを取得
    jsonデータを返却
    """
    sql = f"""
    SELECT 
        small_category_id
        ,small_category_name
    FROM
        SmallCategory01
    WHERE
        is_deleted = 0
        AND large_category_id = '{large_category_id_str}'
    ORDER BY
        sort_number
        ,registered_at;
    """
    record_list = select(sql)

    return json.dumps(record_list)