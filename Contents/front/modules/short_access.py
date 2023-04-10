from flask import Flask, Blueprint
from lib.db_util import DataBase

import json

get_any_router = Blueprint("get_any_router", __name__)

@get_any_router.route("/get_any/large", methods=['get'])
def get_large():
    """
    リストを取得
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

    return json.dumps({"record_list":record_list})


@get_any_router.route("/get_any/small", methods=['get'])
def get_small():
    """
    リストを取得
    """
    db = DataBase()
    sql = f"""
    SELECT 
        small_category_id
        ,small_category_name
    FROM
        SmallCategory01
    WHERE
        is_deleted = 0
    ORDER BY
        sort_number
        ,registered_at;
    """
    record_list = db.select(sql)

    name_list = []
    index_list = []
    for index, record in enumerate(record_list):
        if record["small_category_name"] not in name_list:
            name_list.append(record["small_category_name"])
        else:
            index_list.append(index)

    for index in reversed(index_list):
        del record_list[index]

    return json.dumps({"record_list":record_list})



@get_any_router.route("/short_delete/<card_id_str>", methods=['get'])
def delete(card_id_str):
    """
    DBにアクセスしてデータを削除
    """
    db = DataBase()

    card_delete_sql = f"""
    UPDATE
        Cards01
    SET
        is_deleted = True
    WHERE
        card_id = '{card_id_str}';
    """
    db.insert(card_delete_sql)
    db.commit()
    