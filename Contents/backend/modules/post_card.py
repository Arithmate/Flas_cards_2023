from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request
from flask import render_template
from lib.db_util import select, insert
from datetime import datetime

import uuid
import json
import requests

post_card_router = Blueprint("post_card_router", __name__)

@post_card_router.route("/post_card", methods=['post'])
def post(body):
    """
    DBにアクセスしてデータをインサート
    """

    card_id = uuid.uuid4()
    registered_at = datetime.now()

    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # 大分類設定
    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    large_category_name = body.large_category_name

    large_category_sql = f"""
    SELECT 
        large_category_id
        ,large_category_name
    FROM
        LargeCategory01
    WHERE
        is_deleted = 0
        AND large_category_name = '{large_category_name}';
    """
    large_category_record_list = select(large_category_sql)
    large_category_id = ""

    if len(large_category_record_list) == 1:
        large_category_id = large_category_record_list[0]["large_category_id"]
        large_category_name = large_category_record_list[0]["large_category_name"]

    else:
        large_category_id = uuid.uuid4()
        large_category_insert_sql = f"""
        INSERT INTO LargeCategory01 
            (large_category_id
            ,large_category_name
            ,registered_at
            ,updated_at)
        VALUES
            ({large_category_id}
            ,'{large_category_name}'
            ,'{registered_at}'
            ,'{registered_at}');
        """
        insert(large_category_insert_sql)

    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # 小分類設定
    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    small_category_name = body.small_category_name

    small_category_sql = f"""
    SELECT 
        small_category_id
        ,small_category_name
    FROM
        SmallCategory01
    WHERE
        is_deleted = 0
        AND small_category_name = '{small_category_name}';
    """

    small_category_record_list = select(small_category_sql)

    if len(small_category_record_list) == 1:
        small_category_id = small_category_record_list[0]["small_category_id"]
        small_category_name = small_category_record_list[0]["small_category_name"]

    else:
        small_category_id = uuid.uuid4()
        small_category_insert_sql = f"""
        INSERT INTO SmallCategory01 
            (small_category_id
            ,small_category_name
            ,large_category_id
            ,registered_at
            ,updated_at)
        VALUES
            ({small_category_id}
            ,'{small_category_name}'
            ,'{large_category_id}'
            ,'{registered_at}'
            ,'{registered_at}');
        """
        insert(small_category_insert_sql)

    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # ノート設定
    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    note_conent = body.note_conent

    note_id = uuid.uuid4()
    note_insert_sql = f"""
    INSERT INTO Notes01 
        (note_id
        ,card_id
        ,note_conent
        ,registered_at
        ,updated_at)
    VALUES
        ({note_id}
        ,{card_id}
        ,'{note_conent}'
        ,'{registered_at}'
        ,'{registered_at}');
    """
    insert(note_insert_sql)

    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # タグ設定
    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    tag_name_list = body.tag_name_list

    for tag_name in tag_name_list:
        if tag_name:
            tag_id = uuid.uuid4()
            tag_insert_sql = f"""
            INSERT INTO Tags01 
                (tag_id
                ,card_id
                ,tag_name
                ,registered_at
                ,updated_at)
            VALUES
                ({tag_id}
                ,{card_id}
                ,'{tag_name}'
                ,'{registered_at}'
                ,'{registered_at}');
            """
            insert(tag_insert_sql)

    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # その他のパラメータ設定
    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    
    sort_number = 0

    sql = f"""
    SELECT
        count(*)
    FROM
        Cards01
    WHERE
        is_deleted = 0
    ORDER
        BY sort_number;
    """
    sort_number = select(sql)[0]["count(*)"]

    card_name = body.card_name
    significance = body.significance
    study_state = body.study_state

    sql = f"""
    INSERT INTO Cards01 
        (card_id
        ,card_name
        ,primal_note_id
        ,large_category_id
        ,small_category_id
        ,sort_number
        ,significance
        ,study_state)
    VALUES
        ({card_id}
        ,'{card_name}'
        ,'{note_id}'
        ,({large_category_id}
        ,({small_category_id}
        ,'{sort_number}'
        ,'{significance}'
        ,'{study_state}');
    """
    insert(sql)

    return None