# 実行するPythonがあるパス
pythonpath = './modules'

# ワーカー数
workers = 2

# ワーカーのクラス
# worker_class = 'uvicorn.workers.UvicornWorker'

# IPアドレスとポート
bind = '0.0.0.0:5005'

# プロセスIDを保存するファイル名
pidfile = 'prod.pid'

reload = True

# Pythonアプリに渡す環境変数


# デーモン化する場合はTrue
daemon = False

# プロセスの名前
# proc_name = 'my_python_app'

# エラーログ
errorlog = '-'

# アクセスログ
accesslog = '-'