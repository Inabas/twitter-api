from datetime import datetime, timedelta

def getJstNow():
  jst_now = datetime.utcnow() + timedelta(hours=9)
  return jst_now.strftime('%Y年%m月%d日 %H:%M:%S')