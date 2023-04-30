import discord
import re
from converter import Converter
from config import CONFIG


class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

    # 起動時に動作する処理
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    # メッセージ受信時に動作する処理
    async def on_message(self, message):
        # メッセージ送信者がBotだった場合は無視する
        if message.author == self.user:
            return

        # input: xxxx/++++
        pattern = r"日本\d{4}/\d{4}|アメリカ\d{4}/\d{4}"
        input_days: list = re.findall(pattern, message.content)
        if input_days:
            for input_day in input_days:
                area = "Asia/Tokyo" if "日本" in input_day else "America/Los_Angeles"
                time = re.search(r"\d{4}/\d{4}", input_day).group()
                my_converter = Converter(area, time)
                converted_time = my_converter.convert()

                await message.channel.send(converted_time)


bot = MyBot()
# Discordボットを起動
bot.run(CONFIG["TOKEN"])
