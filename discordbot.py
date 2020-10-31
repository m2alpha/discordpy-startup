import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN'] # トークンキー
TEXT_CHANNEL = 770643077852299335 # テキストチャットのチャンネルID

client = discord.Client()

# こんにちはメッセージ

@client.event
async def on_message(message):
    if message.content.startswith("こんにちは"):
        if client.user != message.author:
            msg = "こんにちは " + message.author.name + "さん！"
            await client.send_message(message.channel, msg)

client.run(TOKEN)
