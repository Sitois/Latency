import sys, os
import discord
from discord.ext import commands
from colorama import Fore, Style, Back
parent_dir = os.path.abspath('./')
sys.path.append(parent_dir)
import config
import asyncio

class Templates_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.id == self.bot.user.id:
          if ctx.content.startswith(f"{config.prefix}use"):
                template = ctx.content.split()[1]
                if template.lower() == "python":
                    await self.bot.change_presence(status=discord.Status.idle,
                                                   activity=discord.Activity(type=discord.ActivityType.playing,
                                                                             name="Visual Studio Code",
                                                                             details=f"Editing {self.bot.user.name}.py",
                                                                             assets={"large_image": "mp:attachments/1135264530188992562/1198617576553599057/3jMZG0a.png?ex=65f6ed9b&is=65e4789b&hm=3b169ca046fd4347a4c78a84e5216f1f874569ada17251e93aa44b194b5bf5e2&=&format=webp&quality=lossless",
                                                                                     "large_text": "Editing a PYTHON file.",
                                                                                     "small_image": "mp:attachments/1135264530188992562/1198617586389225592/aBjaPbQ.png?ex=65f6ed9d&is=65e4789d&hm=97d36113d02a7a076b119042f9f1c5da5e13a8b411db8b32decbbeea41b8dcbc&=&format=webp&quality=lossless",
                                                                                     "small_text": "Visual Studio Code"},
                                                                             state=f"Workspace: Latency")
                                                  )
                    await ctx.edit(content="👨‍💻 Template \"Python\".")
                    await asyncio.sleep(config.deltime)
                    await ctx.delete()
                elif template.lower() == "default":
                    await self.bot.change_presence(status=discord.Status.idle,
                                                   activity=discord.Activity(type=discord.ActivityType.competing,
                                                                             name=config.name,
                                                                             details=config.details,
                                                                             assets=config.assets,
                                                                             state=config.state)
                                                  )
                    await ctx.edit(content="🔁 Template \"Default\".")
                    await asyncio.sleep(config.deltime)
                    await ctx.delete()
                else:
                    await ctx.edit(content="Aucune tempates trouvé.")
                    await asyncio.sleep(config.deltime)
                    await ctx.delete()