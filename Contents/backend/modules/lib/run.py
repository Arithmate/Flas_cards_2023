# Copyright KaikeiBank Co.,Ltd. All rights reserved.

import logging
import os

import lib.log as Log
import lib.threadLocal as TL
import pyutility.utility as util
from flask import Flask
from flask import g
from flask import request
from modules.companies.accounts import companies_accounts_router


# --- APIサーバインスタンスの設定
flask = Flask(__name__)

# --- ルーティング
flask.register_blueprint(companies_router)


dbenv = {}
host_id = ""
is_local = False
log_level = 0


@flask.before_request
@Log.logger
def before_req() -> None:
    """
    beforeフィルタ
     - ログ出力
     - メンテナンスチェック
     - ロックアウト処理
    """

    global dbenv

    g.is_local = is_local
    g.aws_bucket_prefix = os.environ.get("AWS_BUCKET_PREFIX")
    g.aws_bucket_traceback_prefix = os.environ.get("AWS_BUCKET_TRACEBACKPREFIX")
    idReplacedPath, ids = util.separationIdInUrl(request.path)
    param = ",".join(map(str, ids))
    log_level = int(os.environ.get("LOG_LEVEL"))
    api_name = request.method + " " + idReplacedPath
    TL.setApiName(api_name)
    http_method = request.method
    api_name = idReplacedPath
    client_ip_address = ""
    load_balancer_ip_address = ""
    host_id = ""

    if g.is_local:
        client_ip_address = request.remote_addr
    else:
        if request.headers.get("X-Forwarded-For") != None:
            try:
                client_ip_address = request.headers.get("X-Forwarded-For").split(",")[0]
            except:
                client_ip_address = "XXX.XXX.XXX.XXX"

        load_balancer_ip_address = request.remote_addr

    # ログ設定
    Log.start(log_level, client_ip_address, load_balancer_ip_address, http_method, api_name, param, is_local, host_id)

    # DB設定
    TL.setDbInstance(DB(dbenv))


@flask.after_request
@Log.logger
def after_req(response) -> None:
    """
    afterフィルタ
     - ログ出力
    """
    # 処理がある場合は、下記に記載する

    # ENDログ
    Log.end(response.status_code)

    return response


@flask.route("/favicon.ico")
def favicon():
    # Web画面アクセス時のfaviconでの404を抑制するために空文字返却
    return ""


def initialize():
    """
    メイン処理
     - flaskの起動
    """

    # 使用するグローバル変数を明示的に定義
    global dbenv
    global host_id
    global is_local
    global log_level

    is_success = True
    error_message = ""

    # DB接続環境変数を取得
    dbenv["host_master"] = os.environ.get("DB_HOST")
    dbenv["write_user"] = os.environ.get("DB_USER")
    dbenv["write_password"] = os.environ.get("DB_PASSWORD")
    dbenv["read_user"] = os.environ.get("DB_USER")
    dbenv["read_password"] = os.environ.get("DB_PASSWORD")
    dbenv["database"] = os.environ.get("DB_SCHEMA")

    # ローカル実行
    if os.getenv("LOCAL", "0") == "1":
        is_local = True

    # AWS初回設定
    awsenv = {}
    awsenv["bucket_name"] = os.environ.get("AWS_BUCKET_NAME")
    aws = AWS(awsenv)

    # ログレベルを取得(コンテナ起動後に環境変数を変更することが出来ないため、起動時に取得する)
    log_level = int(os.environ.get("LOG_LEVEL"))

    if log_level <= 2:
        # flaskのデフォルトログ出力をカット
        l = logging.getLogger()
        l.addHandler(logging.FileHandler("/dev/null"))

    # host_idファイルの存在チェック
    try:
        host_id = open("/etc/ecs/instance-id", "r").read()
    except:
        host_id = ""

    # 初期設定
    Validation.bucket_prefix = os.environ.get("AWS_BUCKET_PREFIX")


initialize()


