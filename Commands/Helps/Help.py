import sys, os
import asyncio
import discord
from discord.ext import commands
parent_dir = os.path.abspath('./')
sys.path.append(parent_dir)
import config
import random

poetry = [
     "Jour meilleur n'existe qu'avec douleur.",
     "La seule personne que vous êtes destiné à devenir est la personne que vous décidez d'être.",
     "L'avenir appartient à ceux qui croient en la beauté de leurs rêves.",
     "L'échec est le fondement de la réussite.",
     "Ne rêvez pas votre vie, vivez vos rêves.",
     "Crois en toi, et les autres suivront.",
     "Sois le changement que tu veux voir dans le monde.",
     "Poursuis tes rêves, ils connaissent le chemin.",
     "La vie récompense l'action.",
     "Tu es plus fort que tu ne le crois.",
     "Le succès commence par l'action.",
     "La persévérance bat le talent.",
     "Ne remettez pas à demain.",
     "Chaque effort compte.",
     "Les montagnes les plus hautes ont les pentes les plus raides.",
     "Les éclats de lumière percent l'obscurité la plus profonde."
]

class Help_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.id == self.bot.user.id:
          if ctx.content.startswith(f"{config.prefix}help"):
            await ctx.edit(content=f"""☄ __**{config.selfbot_name} :**__ ☄
  ☄ "{random.choice(poetry)}" ☄

  🏮| __**Général:**__ `{config.prefix}general`""")
            await asyncio.sleep(config.deltime)
            await ctx.delete()