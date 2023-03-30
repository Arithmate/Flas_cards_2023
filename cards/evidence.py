from flask import Blueprint, request, session

blueprint = Blueprint("/evidence", __name__)

# GET:申告系はここにまとめる
@blueprint.route("/evidence", methods=["GET"])
def get():
    view = f"""
<html>
  <head>
    <link rel="stylesheet" href="static/style.css">
  </head>

  <body>
    <div class="wrapper">
    """

    terminal_id=""
    sori_id=""
    token=""
    company_id="" # TODO:リンクストレージを動かすためには、accounts2のDBの向き先をaccountsと同じにする必要がある。
    period_id=""
    if "terminal_id" in session:
        terminal_id = session['terminal_id']
    if "sori_id" in session:
        sori_id = session['sori_id']
    if "token" in session:
        token = session['token']
    if "company_id" in session:
        company_id = session['company_id']
    if "period_id" in session:
        period_id = session['period_id']

    view += f"""
        <label><<セッション情報>></label><br>
        <label>terminal_id={terminal_id}</label><br>
        <label>sori_id={sori_id}</label><br>
        <label>token={token}</label><br>
        <label>company_id={company_id}</label><br>
        <label>period_id={period_id}</label><br>
        <br>
        """

    view += """
      <form action="/evidence/register" method="get">
        <input type="submit" id="button1" value="画像登録"/>
      </form>
      <form action="/evidence/register_ocr" method="post" enctype="multipart/form-data">
        <input type="submit" id="button1" value="証憑画像CSVアップロード"/>
        <p><label>証憑種別：<select name="evidence_type">
          <option value="2">請求書</option>
          <option value="0">レシート</option>
          <option value="1">領収書</option>
          <option value="3">通帳</option>
          </select></label></p>
        <input type="file" name="file"/><br><br>
      </form>
      <form action="invoice/evidence/register" method="get">
        <input type="submit" id="button1" value="インボイス用画像登録（複数枚登録○）"/>
      </form>
      <form action="evidence/group" method="get">
        <input type="submit" id="button1" value="証憑画像グループ取得"/>
        <p><label>証憑画像グループID：<input type="text" name="evidence_group_id" size="40"></label></p>
        <p><label>証憑種別：<select name="evidence_type">
          <option value="2">請求書</option>
          <option value="0">レシート</option>
          <option value="1">領収書</option>
          <option value="3">通帳</option>
          </select></label></p>
      </form>
      <form action="/evidence/image" method="get">
        <input type="submit" id="button1" value="表示用画像取得" />
      </form>
      <form action="/evidence/thumbnail" method="get">
        <input type="submit" id="button1" value="サムネイル用画像取得" />
      </form>
      <form action="/companies/ocr_execution" method="post">
        <input type="submit" id="button1" value="OCR実行" />
      </form>
       <form action="/evidence/ocr_result" method="get">
        <input type="submit" id="button1" value="OCR結果" />
      </form>
      <form action="/sksv/companies/image_processing_status" method="get">
        <input type="submit" id="button1" value="画像処理ステータス" />
      </form>
      <br><br><br>
    </div>
  </body>
</html>
"""
    return view
