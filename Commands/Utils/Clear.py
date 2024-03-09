import sys, os
import discord
from discord.ext import commands
from colorama import Fore, Style, Back
parent_dir = os.path.abspath('./')
sys.path.append(parent_dir)
import config
import asyncio

class Clear_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.id == self.bot.user.id:
          if ctx.content.startswith(f"{config.prefix}clear"):
            num_messages = ctx.content.split()
            try:
                num_messages = int(num_messages[1])
            except:
                await ctx.edit(content="❌ Insérez une valeur valide !")
                await asyncio.sleep(3)
                await ctx.delete()
                return
            num_messages = num_messages + 1
            if num_messages <= 0:
                await ctx.edit(content="❌ Insérez une valeur valide !")
                await asyncio.sleep(3)
                await ctx.delete()
                return

            await ctx.delete()

            num_messages = num_messages - 1
            async for message in ctx.channel.history(limit=num_messages).filter(lambda m: m.author.id == self.bot.user.id):
                await message.delete()
                await asyncio.sleep(0.6)

            await ctx.channel.send(f"> 🚮 {num_messages} messages ont été supprimés.", delete_after=1)