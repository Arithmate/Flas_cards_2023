from flask import Flask
from flask import request
from flask import render_template
from lib.db_util import select, insert

import json
import requests

app = Flask(__name__)


@app.route("/small_category/get_list", methods=['GET'])
def get_list():
    """
    DBにアクセスしてデータを取得
    jsonデータを返却
    """
    sql = f"""
    SELECT *
    FROM SmallCategory01
    WHERE is_deleted = 0
    ORDER BY sort_number;
    """

    res = select(sql)

    return res

@app.route("/small_category/put", methods=['PUT'])
def put(
    small_category_id,
    small_category_name,
):
    """
    DBにアクセスしてデータをインサート
    """
    sort_number = 0

    sql = f"""
    SELECT count(*)
    FROM SmallCategory01
    WHERE is_deleted = 0
    ORDER BY sort_number;
    """
    sort_number = select(sql)[0]["count(*)"]

    sql = f"""
    INSERT INTO SmallCategory01 
    (small_category_id
    ,small_category_name
    ,sort_number)
    VALUES
    (UNHEX({small_category_id})
    ,'{small_category_name}'
    ,{sort_number});
    """

    insert(sql)

    return None
    
    
