import sys, os
import asyncio
import discord
from discord.ext import commands
parent_dir = os.path.abspath('./')
sys.path.append(parent_dir)
import config


class General_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.id == self.bot.user.id:
          if ctx.content.startswith(f"{config.prefix}general"):
            await ctx.edit(content=f"""☄ __**{config.selfbot_name} :**__ ☄

🏮| __**Général:**__
 `{config.prefix}clear`: Clear les messages.
 `{config.prefix}use python / default`: Utilise la Template choisi.""")
            await asyncio.sleep(config.deltime)
            await ctx.delete()