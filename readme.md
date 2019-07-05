# 概要
- 遅延情報を取得して、電車が遅れている場合にはSlackの特定チャネルへ通知する。

# ファイルの構成
- functions
  - DelayInfo.py
    - 遅延情報を抽出して文字列で返す
  - lambda_function.py
    - メイン処理
  - PostRequest.py
    - 指定したURLに指定した文字列のPostリクエストを送る
