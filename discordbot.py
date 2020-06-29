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
    """BOTの説明用コマンド"""
    viewrecipes();
    await ctx.send('使いたい機能を実行する際は以下のコマンドを入力してください\n ■ブルプロクラフトレシピ /bpre [item No]\n ■ブルプロクラフト品リスト /bpli')

@bot.command()
async def bpre(ctx, arg):
    """該当アイテムのレシピを表示します。"""
    await ctx.send(arg+'の作成には以下の素材が必要です。\nトリックエルダーの爪：１個\n湧水石：50個')
                   
@bot.command()
async def bpli(ctx):
    """ブルプロのクラフト対象アイテムリストを表示します。"""
    await ctx.send('動　作テスト')
                 
    
def viewrecipes():
    print('Hello')

    @client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def poll(ctx, about = "question", *args):
    emojis = ["1⃣","2⃣","3⃣","4⃣"]

    cnt = len(args)
    message = discord.Embed(title=":speech_balloon: "+about,colour=0x1e90ff)
    if cnt <= len(emojis):
        for a in range(cnt):
            message.add_field(name=f'{emojis[a]}{args[a]}', value="** **", inline=False)
        msg = await ctx.send(embed=message)
        #投票の欄
        for i in range(cnt):
            await msg.add_reaction(emojis[i])
    else:
        await ctx.send("すまないが項目は4つまでなんだ...")
    
bot.run(token)
