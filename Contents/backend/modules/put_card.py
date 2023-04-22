from flask import Flask, Blueprint
from flask import request
from flask import render_template
from lib.db_util import DataBase
from lib.util import reset_sort_number
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

    db = DataBase()

    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # 単語・大分類・小分類は、無入力だった場合変更前の値を使用
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    card_sql = f"""
    SELECT 
        c.card_name
        ,c.sort_number
        ,c.significance
        ,c.study_state
        ,s.small_category_name
        ,l.large_category_name
    FROM
        Cards01 as c
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
        AND c.card_id = '{card_id}';
    """
    card_record_list = db.select(card_sql)

    card_name = data.get("card_name") or card_record_list[0]["card_name"]
    small_category_name = data.get("small_category_name") or card_record_list[0]["small_category_name"]
    large_category_name = data.get("large_category_name") or card_record_list[0]["large_category_name"]
    note_content = data.get("note_content") or ""
    tag_name_list = data.get("tag_name_list") or []
    significance = data.get("significance") or card_record_list[0]["significance"]
    study_state = data.get("study_state") or card_record_list[0]["study_state"]

    before_number = int(card_record_list[0]["sort_number"])
    new_number_str = data.get("sort_number") or str(before_number)
    new_number = int(new_number_str)

    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # 大分類設定
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

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
    large_category_record_list = db.select(large_category_sql)
    large_category_id = ""

    if len(large_category_record_list) == 1:
        large_category_id = large_category_record_list[0]["large_category_id"]
        large_category_name = large_category_record_list[0]["large_category_name"]

    else:
        large_category_id = str(uuid.uuid4()).replace('-', '')
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
        db.insert(large_category_insert_sql)

    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # 小分類設定
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    small_category_sql = f"""
    SELECT 
        small_category_id
        ,small_category_name
    FROM
        SmallCategory01
    WHERE
        is_deleted = False
        AND small_category_name = '{small_category_name}'
        AND large_category_id = '{large_category_id}';
    """

    small_category_record_list = db.select(small_category_sql)

    if len(small_category_record_list) == 1:
        small_category_id = small_category_record_list[0]["small_category_id"]
        small_category_name = small_category_record_list[0]["small_category_name"]

    else:
        small_category_id = str(uuid.uuid4()).replace('-', '')
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
        db.insert(small_category_insert_sql)

    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # ノート設定
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    note_update_sql = f"""
    UPDATE
        Notes01
    SET
        note_content = '{note_content}'
        ,updated_at = '{registered_at}'
    WHERE
        card_id = '{card_id}';
    """
    db.insert(note_update_sql)

    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # タグ設定
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    if len(tag_name_list) > 0:
        # リクエストがある場合のみ、タグ情報を上書き
        tag_delete_sql = f"""
            UPDATE
                Tags01
            SET
                is_deleted = True
            WHERE
                card_id = '{card_id}';
        """
        db.insert(tag_delete_sql)

        for tag_name in tag_name_list:
            if tag_name:
                tag_id = str(uuid.uuid4()).replace('-', '')
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
                db.insert(tag_insert_sql)

    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # ソート番号を設定
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    reset_sort_number(db, small_category_id)

    if before_number < new_number:
        # 後ろにずらす場合
        # for文でリストを正順にまわして一つずつソート番号を -1で上書きしていく
        for index in range((before_number + 1), (new_number + 1), 1):
            sort_update_sql = f"""
                UPDATE
                    Cards01
                SET
                    sort_number = {str(index - 1)}
                WHERE
                    sort_number = {str(index)}
                    AND small_category_id = '{small_category_id}';
            """
            db.insert(sort_update_sql)

    elif before_number > new_number:
        # 前にずらす場合
        # for文でリストを逆順にまわして一つずつソート番号を+1で上書きしていく
        for index in range((before_number - 1), (new_number - 1), -1):
            sort_update_sql = f"""
                UPDATE
                    Cards01
                SET
                    sort_number = {str(index + 1)}
                WHERE
                    sort_number = {str(index)}
                    AND small_category_id = '{small_category_id}';
            """
            db.insert(sort_update_sql)

    else:
        pass

    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # その他のパラメータ設定
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーー

    card_update_sql = f"""
    UPDATE
        Cards01
    SET
        card_name = '{card_name}'
        ,large_category_id = '{large_category_id}'
        ,small_category_id = '{small_category_id}'
        ,significance = '{significance}'
        ,study_state = '{study_state}'
        ,sort_number = {new_number}
        ,updated_at = '{registered_at}'
    WHERE
        card_id = '{card_id}';
    """
    db.insert(card_update_sql)
    reset_sort_number(db, small_category_id)

    db.commit()

    return json.dumps([{"card_id": card_id}])


@put_card_router.route("/put_card/update_note", methods=['put'])
def update_note():
    """
    DBにアクセスしてデータをアップデート
    """
    data = json.loads(request.data.decode('utf-8'))
    card_id = data["card_id"]
    note_content = data.get("note_content") or ""

    registered_at = datetime.now()

    db = DataBase()

    note_update_sql = f"""
    UPDATE
        Notes01
    SET
        note_content = '{note_content}'
        ,updated_at = '{registered_at}'
    WHERE
        card_id = '{card_id}';
    """
    db.insert(note_update_sql)
    db.commit()

    return json.dumps([{"card_id": card_id}])


@put_card_router.route("/put_card/delete/<card_id_str>", methods=['put'])
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

    return json.dumps([{"card_id": card_id_str}])
