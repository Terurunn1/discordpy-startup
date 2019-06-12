from discord.ext import commands
from datetime import datetime
import os
import traceback
import discord
import asyncio
import re

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "!眠たい":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん 寝ましょう")  # f文字列（フォーマット済み文字列リテラル）

    elif message.content == "!投票":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたは右利きですか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "!おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('大吉', '吉', '凶', '大凶')), inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "!ダイレクトメッセージ":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんにダイレクトメッセージ")
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
