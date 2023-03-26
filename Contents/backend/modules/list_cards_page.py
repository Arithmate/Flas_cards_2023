from flask import Flask
from flask_cors import CORS
from flask import request
from flask import render_template
from lib.db_util import select, insert

import json

app = Flask(__name__)
CORS(app)

@app.route("/list_cards/get_list", methods=['GET'])
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

@app.route("/list_cards/put", methods=['PUT'])
def put(
    list_cards_id,
    list_cards_name,
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
    (list_cards_id
    ,list_cards_name
    ,sort_number)
    VALUES
    (UNHEX({list_cards_id})
    ,'{list_cards_name}'
    ,{sort_number});
    """

    insert(sql)

    return None
    
if __name__ =='__main__':
    app.run()
