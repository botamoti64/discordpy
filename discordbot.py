from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='s>')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client() 

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def test(ctx):
    await ctx.send('テストだと思ったか？残念普通のコマンドだ(？)')
@bot.command()
async def syamu(ctx):
    await ctx.send('　ウイイイイイイイッッッッスどうも、シャムでーす。')
@client.event
async def on_message(message):
 if message.content == ('hello'):
    message.channel.send('hello')
    
bot.run(token)
