import discord
import asyncio
import traceback
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@client.event
async def on_ready():
    asyncio.ensure_future(greeting_gm())

async def greeting_gm():
    await client.send_message(channel, 'おはよう')
    await asyncio.sleep(10)

client.run(token)
