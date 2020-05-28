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


@bot.command()
async def tsc(ctx):
    await ctx.send('使いたい機能を実行する際は以下のコマンドを入力してください\n ■ブルプロクラフトレシピ /bpre [item No]\n　■ブルプロクラフト品リスト /bpli')

@bot.command()
async def bpre(ctx, arg):
    """該当アイテムのレシピを表示します。"""
    await ctx.send(arg+'番のアイテムが選択されました。(テスト)')
                   
@bot.command()
async def bpli(ctx):
    """Adds two numbers together."""
    await ctx.send('動作テスト')
                   
bot.run(token)
