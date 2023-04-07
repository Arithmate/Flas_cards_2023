from flask import Flask, Blueprint
from lib.db_util import DataBase

import json

small_category_router = Blueprint("small_category_router", __name__)

@small_category_router.route("/small_list/get_list/<large_category_id_str>", methods=['GET'])
def get_list(large_category_id_str):
    """
    DBにアクセスしてデータを取得
    jsonデータを返却
    """
    db = DataBase()
    sql = f"""
    SELECT 
        s.small_category_id
        ,s.small_category_name
        ,l.large_category_name
    FROM
        SmallCategory01 as s
    INNER JOIN
        LargeCategory01 as l
    ON
        s.large_category_id = l.large_category_id
    WHERE
        s.is_deleted = 0
        AND s.large_category_id = '{large_category_id_str}'
    ORDER BY
        s.sort_number
        ,s.registered_at;
    """
    record_list = db.select(sql)

    return json.dumps(record_list)