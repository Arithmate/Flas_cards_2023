# 実行するPythonがあるパス
pythonpath = './modules'

# ワーカー数
workers = 2

# IPアドレスとポート
bind = '0.0.0.0:5006'

# プロセスIDを保存するファイル名
pidfile = 'prod.pid'

reload = True

# デーモン化する場合はTrue
daemon = False

# エラーログ
errorlog = '-'

# アクセスログ
accesslog = '-'