import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv(dotenv_path=".config")
token = os.getenv("TOKEN")

class OpenTicket(commands.Bot):

    async def setup_hook(self):
        await self.load_extension("cogs.commands.sendselection")
        await self.load_extension("cogs.commands.helpform")
        await self.load_extension("cogs.commands.closeticket")

    async def on_ready(self):
        print("Bot is ready...")
        await bot.tree.sync()
        print("Commands have been synchronized")

intents = discord.Intents.all()
bot = OpenTicket(command_prefix="!", intents=intents)
bot.run(token=token)