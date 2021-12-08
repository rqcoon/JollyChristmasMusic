import discord
from discord import FFmpegPCMAudio
from discord.ext import commands,tasks
from asyncio import run_coroutine_threadsafe as rct

DISCORD_TOKEN='sex'
bot = commands.Bot(command_prefix='_')
sacred_file="assets/sound.mp3"

@bot.event
async def on_ready():
    print('balls')

def play_next(ctx, n):
    if n:
        audio = 'assets/sound.mp3'
        voice = ctx.author.voice.channel
        source = discord.FFmpegPCMAudio(audio)
        ctx.voice_client.play(source, after=lambda e: play_next(ctx, 1))
    else:
        rct(msg.delete())

@bot.command(name='begin')
async def on_message(ctx):
    audio = 'assets/sound.mp3'
    channel = ctx.author.voice.channel
    client = await channel.connect()

    source = discord.FFmpegPCMAudio(audio)
    ctx.voice_client.play(source, after=lambda e: play_next(ctx,1))

bot.run(DISCORD_TOKEN)
