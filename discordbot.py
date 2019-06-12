from discord.ext import commands
from datetime import datetime
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('自作ボットのテスト中です')

@bot.command()
async def boss(ctx):
    #現在の時刻(分)を取得する。
    nowMinutes = int(datetime.now().strftime('%M'))
    outPut = ""
    print(nowMinutes)
    if nowMinutes > 55 or nowMinutes <= 5 :
        outPut += "以下のボスが次回(5分)出現します。"
        outPut +="\nドゥンドゥン : カニング廃棄物処理場"
        outPut +="\nロロとムムス : バウム木"
        outPut +="\n怒りのバフォメット : キャッスルリバース"
        outPut +="\nアクレオン : ラベンダー島"
        outPut +="\nイカル・マード : アイスクラウン"
    elif nowMinutes > 5 and 15 >= nowMinutes :
        outPut +="以下のボスが次回(15分)出現します。"
        outPut +="\nグリフォン : 冷たい心臓"
        outPut +="\nウレウス : ナズカル入口"
        outPut +="\n冷血なバフォメット : 雪の花峰"
    elif nowMinutes > 15 and 25 >= nowMinutes :
        outPut +="以下のボスが次回(25分)出現します。"  
        outPut +="\nグリフィーナ : トリニアン街道"
        outPut +="\nトトとググス : 赤い口笛の絶壁"
    elif nowMinutes > 25 and 35 >= nowMinutes :
        outPut +="以下のボスが次回(35分)出現します。"  
        outPut +="\nバヤールの門番 : 切り立った崖の要塞"
        outPut +="\nジャイアントタートル : ビーチウェイ”111″"
    elif nowMinutes > 35 and 40 >= nowMinutes :
        outPut +="\n以下のボスが次回(40分)出現します。"
        outPut +="\nアルファタートル : エルーア川辺"
    elif nowMinutes > 40 and 55 >= nowMinutes :
        outPut +="以下のボスが次回(55分)出現します。"
        outPut +="\nデブリンウォーリアー : ロイヤルロード南部"
        outPut +="\nペカノス	 : 傷ついた峡谷"
        outPut +="\nアマドン	 : ルデリーアリーナ"

    await ctx.send(outPut)

bot.run(token)
