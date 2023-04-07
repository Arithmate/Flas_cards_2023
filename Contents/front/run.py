# Copyright KaikeiBank Co.,Ltd. All rights reserved.

import logging
import os

from flask import Flask, Blueprint
from flask import g
from flask import request

from modules.large_category_page import large_category_router
from modules.small_category_page import small_category_router
from modules.list_cards_page import list_cards_router
from modules.post_card import post_card_router
from modules.put_card import put_card_router
from modules.get_any_data import get_any_router

# --- APIサーバインスタンスの設定
flask = Flask(__name__)

# --- ルーティング
flask.register_blueprint(large_category_router)
flask.register_blueprint(small_category_router)
flask.register_blueprint(list_cards_router)
flask.register_blueprint(post_card_router)
flask.register_blueprint(put_card_router)
flask.register_blueprint(get_any_router)

dbenv = {}
host_id = ""
is_local = False
log_level = 0

def initialize():
    """
    メイン処理
     - flaskの起動
    """

    # # 使用するグローバル変数を明示的に定義
    # global dbenv
    # global host_id
    # global is_local
    # global log_level

    # # DB接続環境変数を取得
    # dbenv["host_master"] = os.environ.get("DB_HOST")
    # dbenv["write_user"] = os.environ.get("DB_USER")
    # dbenv["write_password"] = os.environ.get("DB_PASS")
    # dbenv["read_user"] = os.environ.get("DB_USER")
    # dbenv["read_password"] = os.environ.get("DB_PASS")
    # dbenv["database"] = os.environ.get("DB_SCHEMA")


initialize()
