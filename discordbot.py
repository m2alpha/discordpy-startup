import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN'] # トークンキー
TEXT_CHANNEL = 767123336869576728 # テキストチャットのチャンネルID

client = discord.Client()

text_chat = discord.Object(id=TEXT_CHANNEL)

# こんにちはメッセージ

@client.event
async def on_message(message):
    if message.content.startswith("こんにちは"):
        if client.user != message.author:
            msg = "こんにちは " + message.author.name + "さん！"
            await client.send_message(message.channel, msg)

client.run(TOKEN)
