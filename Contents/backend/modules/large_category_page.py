from flask import Flask, Blueprint
from lib.db_util import DataBase

import json

large_category_router = Blueprint("large_category_router", __name__)


@large_category_router.route("/large_list/get_list", methods=['GET'])
def get_list():
    """
    DBにアクセスしてデータを取得
    jsonデータを返却
    """
    db = DataBase()
    sql = f"""
    SELECT 
        large_category_id
        ,large_category_name
    FROM
        LargeCategory01
    WHERE
        is_deleted = 0
    ORDER BY
        sort_number
        ,registered_at;
    """
    record_list = db.select(sql)

    return json.dumps(record_list)
