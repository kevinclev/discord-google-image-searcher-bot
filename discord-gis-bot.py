import os
import discord

from discord.ext import commands
from google_images_search import GoogleImagesSearch

intents = discord.Intents.default()
intents.members = True

# Discord api token for bot
discord_token = os.environ.get('DISCORD_TOKEN')

gcs_developer_key = os.environ.get('GCS_DEVELOPER_KEY')
gcs_cx = os.environ.get('GCS_CX')

bot = commands.Bot(command_prefix='!')

gis = GoogleImagesSearch(gcs_developer_key, gcs_cx)

@bot.command()
async def imageme(ctx, *, query: str):
    _search_params = {
    'q': query,
    'num': 1,
    'safe': 'off'
    }

    gis.search(search_params=_search_params)
    
    for image in gis.results():
       await ctx.send(image.url)

@bot.command()
async def repeat(ctx, *, message: str):
    await ctx.send(message)

bot.run(discord_token)