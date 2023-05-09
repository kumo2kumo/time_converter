# global commands are cached and only update every hour
# url = f'https://discord.com/api/v8/applications/{APP_ID}/commands'
import requests

# while guild commands update instantly
# they're much better for testing
APP_ID = "xxx"
GUILD_ID = "xxx"
url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{GUILD_ID}/commands'
BOT_TOKEN = "xxx"

json = {
    'name': 'time',
    'description': 'time_converter',
    'options': [
        {
            "name": "area",
            "description": "your_location",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "日本",
                    "value": "Asia/Tokyo"
                },
                {
                    "name": "アメリカ",
                    "value": "America/Los_Angeles"
                },
            ]
        },
        {
            "name": "time",
            "description": "monthday/hourmin(4dig/4dig)",
            "type": 3,
            "required": True
        }
    ]
}

response = requests.post(url, headers={
    'Authorization': f'Bot {BOT_TOKEN}'
}, json=json)

print(response.json())
