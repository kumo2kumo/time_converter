from discordbot import MyBot
from config import CONFIG

if __name__ == '__main__':
    bot = MyBot()
    # Discordボットを起動
    bot.run(CONFIG["TOKEN"])
