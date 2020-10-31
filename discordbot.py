from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if ctx.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if ctx.content == '/panda':
        await ctx.channel.send('ぶぅもぁああああ！ぱんだ～')

@bot.command()
async def ping(ctx):
    await ctx.send('ぶぅもぁああああ！ぱんだ～')

async def panda(ctx):
    await ctx.send('TEST')

bot.run(token)
