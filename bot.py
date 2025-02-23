import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import responses

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def send_response(ctx, command_name):
    response_data = responses.get_response(command_name)
    if isinstance(response_data, discord.Embed):
        await ctx.send(embed=response_data)
    else:
        await ctx.send(response_data)

for command_name in responses.get_all_commands():
    async def command_template(ctx, cmd=command_name):
        await send_response(ctx, cmd)

    bot.command(name=command_name)(command_template)

if TOKEN:
    bot.run(TOKEN)
else:
    print("ERROR: DISCORD_BOT_TOKEN not found in .env file!")

