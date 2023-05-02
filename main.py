# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。
import  os
from discordbot import MyBot
from config import CONFIG
from boto.s3.connection import S3Connection

if __name__ == '__main__':
    bot = MyBot()
    # Discordボットを起動
    token = S3Connection(os.environ['TOKEN'])
    bot.run(token)
