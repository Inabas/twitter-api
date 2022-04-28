import json
import tweepy
import os
# import env
import date_util as dt
# ------------------------------------------------------------------

def lambda_handler():

  # # 環境変数を初期化
  # env.init()

  api = key_tweepy_proc()

  # メッセージ作成
  message = ""
  message += "AWS Lambda 投稿テスト\n"

  # メッセージに現在時刻を追加
  now = dt.getJstNow()
  message += now + "\n"

  # tweet実行
  result = api.update_status(message)
  print(result)

  return {
    'statusCode': 200,
    'body': json.dumps('Tweet is Success!'),
    'etc': print(result)
  }

# ------------------------------------------------------------------

# .envよりアクセスキーなど読み込み、tweepyの認証を設定する
def key_tweepy_proc():

  api_key = os.environ.get("API_KEY")
  api_secret = os.environ.get("API_SECRET")
  access_token = os.environ.get("ACCESS_TOKEN")
  access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

  auth = tweepy.OAuthHandler(api_key, api_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)

  return api
