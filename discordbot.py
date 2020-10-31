from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
TEXT_CHANNEL = 767123336869576728

text_chat = discord.Object(id=TEXT_CHANNEL)
bot2 = commands.Bot

@bot2.event
async def on_message(message):
    if message.content.startswith("こんぱんだ"):
        if bot2.user != message.author:
            msg = "こんぱんだ " + message.author.name + "さん！"
            await bot2.send_message(message.channel, msg)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    if message.content.startswith("こんぱんだ"):
        if bot.user != message.author:
            msg = "こんぱんだ " + message.author.name + "さん！"
            await bot.send_message(message.channel, msg)
    
@bot.command()
async def panda(ctx):
    await ctx.send('ぶぅもぁああああ！ぱんだ～')

bot.run(token)
