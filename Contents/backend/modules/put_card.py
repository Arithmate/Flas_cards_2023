from flask import Flask, Blueprint
from flask import request
from flask import render_template
from lib.db_util import select, insert
from datetime import datetime

import uuid
import json
import requests

put_card_router = Blueprint("put_card_router", __name__)

@put_card_router.route("/put_card", methods=['put'])
def put():
    """
    DBにアクセスしてデータをアップデート
    """
    data = json.loads(request.data.decode('utf-8'))

    card_id = data["card_id"]
    registered_at = datetime.now()

    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # 大分類設定
    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    large_category_name = data["large_category_name"]

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
        large_category_id = str(uuid.uuid4()).replace('-','')
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

    small_category_name = data["small_category_name"]

    small_category_sql = f"""
    SELECT 
        small_category_id
        ,small_category_name
    FROM
        SmallCategory01
    WHERE
        is_deleted = 0
        AND small_category_name = '{small_category_name}'
        AND large_category_id = '{large_category_id}';
    """

    small_category_record_list = select(small_category_sql)

    if len(small_category_record_list) == 1:
        small_category_id = small_category_record_list[0]["small_category_id"]
        small_category_name = small_category_record_list[0]["small_category_name"]

    else:
        small_category_id = str(uuid.uuid4()).replace('-','')
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

    note_content = data["note_content"]
    note_update_sql = f"""
    UPDATE
        Notes01
    SET
        note_content = '{note_content}'
        ,updated_at = '{registered_at}'
    WHERE
        card_id = '{card_id}';
    """
    insert(note_update_sql)

    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # タグ設定
    #ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    tag_delete_sql = f"""
    UPDATE
        Tags01
    SET
        is_deleted = True
    WHERE
        card_id = '{card_id}';
    """
    insert(tag_delete_sql)

    tag_name_list = data["tag_name_list"]
    for tag_name in tag_name_list:
        if tag_name:
            tag_id = str(uuid.uuid4()).replace('-','')
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
    
    card_name = data["card_name"]
    significance = data["significance"]
    study_state = data["study_state"]

    card_update_sql = f"""
    UPDATE
        Cards01
    SET
        card_name = '{card_name}'
        ,large_category_id = '{large_category_id}'
        ,small_category_id = '{small_category_id}'
        ,significance = '{significance}'
        ,study_state = '{study_state}'
        ,updated_at = '{registered_at}'
    WHERE
        card_id = '{card_id}';
    """

    insert(card_update_sql)

    return json.dumps({"card_id":card_id})


@put_card_router.route("/put_card/delete/<card_id_str>", methods=['put'])
def delete(card_id_str):
    """
    DBにアクセスしてデータを削除
    """
    print("バックエンド削除", card_id_str)

    card_delete_sql = f"""
    UPDATE
        Cards01
    SET
        is_deleted = True
    WHERE
        card_id = '{card_id_str}';
    """
    insert(card_delete_sql)

    return json.dumps({"card_id":card_id_str})
