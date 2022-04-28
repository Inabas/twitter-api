import json
import tweepy
import os
# import env
import date_util as dt
# ------------------------------------------------------------------

def lambda_handler(event, context):

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

  return {
    'statusCode': 200,
    'body': json.dumps('Tweet is Success!'),
    'etc': print(result)
  }

# ------------------------------------------------------------------

# .envよりアクセスキーなど読み込み、tweepyの認証を設定する
def key_tweepy_proc():

  consumer_key = os.environ.get("CONSUMER_KEY")
  consumer_secret = os.environ.get("CONSUMER_SECRET")
  access_token = os.environ.get("ACCESS_TOKEN")
  access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)

  return api
