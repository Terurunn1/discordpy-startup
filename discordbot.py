from discord.ext import commands
from datetime import datetime
import os
import traceback
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@client.event
async def on_ready():
    await greeting_gm() #この中のwhile Trueを延々とループするために

async def greeting_gm():
    while True:
        nowMinutes = int(datetime.now().strftime('%M'))
        outPut = ""
        print(nowMinutes)
        if 0 == nowMinutes :
            outPut += "以下のボスが次回(5分)出現します。"
            outPut +="\nドゥンドゥン : カニング廃棄物処理場"
            outPut +="\nロロとムムス : バウム木"
            outPut +="\n怒りのバフォメット : キャッスルリバース"
            outPut +="\nアクレオン : ラベンダー島"
            outPut +="\nイカル・マード : アイスクラウン"
        elif 12 == nowMinutes :
            outPut +="以下のボスが次回(15分)出現します。"
            outPut +="\nグリフォン : 冷たい心臓"
            outPut +="\nウレウス : ナズカル入口"
            outPut +="\n冷血なバフォメット : 雪の花峰"
        elif 25 == nowMinutes :
            outPut +="以下のボスが次回(25分)出現します。"  
            outPut +="\nグリフィーナ : トリニアン街道"
            outPut +="\nトトとググス : 赤い口笛の絶壁"
        elif 30 == nowMinutes :
            outPut +="以下のボスが次回(35分)出現します。"  
            outPut +="\nバヤールの門番 : 切り立った崖の要塞"
            outPut +="\nジャイアントタートル : ビーチウェイ”111″"
        elif 35 == nowMinutes :
            outPut +="\n以下のボスが次回(40分)出現します。"
            outPut +="\nアルファタートル : エルーア川辺"
        elif 50 == nowMinutes :
            outPut +="以下のボスが次回(55分)出現します。"
            outPut +="\nデブリンウォーリアー : ロイヤルロード南部"
            outPut +="\nペカノス	 : 傷ついた峡谷"
            outPut +="\nアマドン	 : ルデリーアリーナ"
        await client.send_message(general, outPut)
        await client.sleep(60)


bot.run(token)
