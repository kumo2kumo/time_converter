# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。
from discordbot import MyBot
from config import CONFIG

if __name__ == '__main__':
    bot = MyBot()
    # Discordボットを起動
    bot.run(CONFIG["TOKEN"])
