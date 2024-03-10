import subprocess
try:
    import platform
    import sys
    import os
    import asyncio
    import json
    import ctypes
    import time
    import asyncio
    import config
    from Commands import *
    from colorama import Fore, Style, Back
    import discord
    from discord.ext import commands
    from discord.ext.tasks import loop
    import requests
except ImportError:
    import platform
    import sys
    if sys.platform == 'win32':
     subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    else:
     subprocess.check_call([sys.executable, "-m", "pip3", "install", '-r' , 'requirements.txt'])
    import os
    import asyncio
    import json
    import ctypes
    import time
    import asyncio
    import config
    from Commands import *
    from colorama import Fore, Style, Back
    import discord
    from discord.ext import commands
    from discord.ext.tasks import loop
    import requests

os.system('cls' if os.name == 'nt' else 'clear')

def set_terminal_title(title):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif system == 'Darwin':
        subprocess.run(['osascript', '-e', f'tell application "Terminal" to set custom title of front window to "{title}"'])
    elif system == 'Linux':
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

try:
   set_terminal_title("| Latency Manager |")
except Exception as e:
   print(f"Error while trying to change the terminal name: {e}")


repo_owner = "Sitois"
repo_name = "Latency"
latency_version = "v1.0"

print(Fore.LIGHTCYAN_EX + f""" /$$                   /$$                                            
| $$                  | $$                                            
| $$        /$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$$   /$$$$$$$ /$$   /$$
| $$       |____  $$|_  $$_/   /$$__  $$| $$__  $$ /$$_____/| $$  | $$
| $$        /$$$$$$$  | $$    | $$$$$$$$| $$  \ $$| $$      | $$  | $$
| $$       /$$__  $$  | $$ /$$| $$_____/| $$  | $$| $$      | $$  | $$
| $$$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$
|________/ \_______/   \___/   \_______/|__/  |__/ \_______/ \____  $$
                                                             /$$  | $$
                                                            |  $$$$$$/
                                                             \______/     {latency_version}""", Style.RESET_ALL)

def check_latest_version(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)
    
    if response.status_code == 200:
        release_info = response.json()
        latest_version = release_info['tag_name']
        return latest_version
    else:
        return None

def call_check_repo():
    global latency_version
    global repo_owner
    global repo_name
    current_version = latency_version
    
    latest_version = check_latest_version(repo_owner, repo_name)
    if latest_version:
        if not latest_version == current_version:
            print(Fore.BLUE, "[INFO]", f"Une nouvelle version ({latest_version}) est disponible: https://github.com/{repo_owner}/{repo_name}/releases/tag/{latest_version}")
            print(f" Vous utilisez actuellement la version {current_version}", Style.RESET_ALL)

try:
    call_check_repo()
except Exception as e:
    print(f"Error while trying to check the last Latency version: {e}")

print(Fore.LIGHTYELLOW_EX, "[#]", Fore.YELLOW, "Démarrage du manager...")




prefix = config.prefix

owner_id = config.owner_id
whitelist = config.whitelist




tokens_list = []

intents_main_bot = discord.Intents.default()
intents_main_bot.dm_messages = True

intents_secondary_bot = discord.Intents.default()
intents_secondary_bot.messages = True
intents_secondary_bot.members = True
intents_secondary_bot.presences = True



class MainBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.secondary_bots = {}

    async def update_presence(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            activity = discord.Activity(type=discord.ActivityType.streaming, name=f"⌘ {len(tokens_list)} Connected !", url=config.streaming_url, application_id=self.bot.user.id)
            await self.bot.change_presence(activity=activity, status=discord.Status.dnd)
            await asyncio.sleep(120)
    
    @commands.command(name="wl", hidden=True)
    async def wl(self, ctx, *, message):
        if ctx.author.id in owner_id:
              split_message = message
              try:
                  whitelist.append(int(split_message))
              except:
                  await ctx.send("Ce n'est pas une ID valide !")
                  return
              await ctx.send(f"<@{split_message.strip()}> a bien été ajouté à la wl !")
    
    @commands.command(name="bl", hidden=True)
    async def bl_command(self, ctx, user_id: int):

        if ctx.author.id in owner_id:
            if user_id in whitelist:
                whitelist.remove(user_id)
                await ctx.send(f"<@{user_id}> a bien été supprimé de la whitelist !")
            else:
                await ctx.send(f"{user_id} n'est pas dans la whitelist.")
            
    @commands.command(name=config.list_command, hidden=True)
    async def list_command(self, ctx):
        if ctx.author.id in owner_id:
            users_list = [f"<@{user_id}>," for user_id in whitelist]
            owners_list = [f"<@{owner_id}>," for owner_id in owner_id]

            users_str = '\n'.join(users_list)
            owners_str = '\n'.join(owners_list)

            embed = discord.Embed(
                title="🌠| Info:",
                color=0xFF0000,
                description=fr"""> 🌈 __Users__: {users_str}
> 🚀 __Owners__: {owners_str}"""
            )
            embed.set_image(url="https://media.discordapp.net/attachments/1135264530188992562/1194342119989575832/MGflOC7.jpg?ex=65b000c7&is=659d8bc7&hm=c64b7087090c66bcea992d538bab97f208a880191863ee3b2f3b41cd739d1902&=&format=webp&width=744&height=419")

            await ctx.send(embed=embed)

    @commands.command(name="owner", hidden=True)
    async def owner_command(self, ctx, user_id: int):

        if ctx.author.id in owner_id:
            if user_id not in owner_id:
                owner_id.append(user_id)
                await ctx.send(f"{user_id} a bien été ajouté à la liste des owners !")
            else:
                await ctx.send(f"{user_id} est déjà dans la liste des owners.")

    @commands.command(name="clear", hidden=True)
    async def clear_command(self, ctx, num_messages: int):
        if ctx.author.id in owner_id:
            if 0 < num_messages <= 100:
                await ctx.message.delete()
                await ctx.channel.purge(limit=num_messages)
                await ctx.send(f"🚮| {num_messages} messages ont été supprimés.", delete_after=3)
            else:
                await ctx.send("❗ Le nombre de messages à supprimer doit être compris entre 1 et 100.")

    @commands.command(name="restart", hidden=True)
    async def restart_command(self, ctx):
        if ctx.author.id in owner_id:
            def restart_selfbot():
             python = sys.executable
             os.execl(python, python, *sys.argv)
            await ctx.send("🔄️ Manager redémarré (patientez quelques secondes...).")
            restart_selfbot()

    @commands.command(name="stop", hidden=True)
    async def stop_command(self, ctx):
        if ctx.author.id in owner_id:
            await ctx.send("🔴 Manager stoppé.")
            await self.bot.close()
            exit()


    @commands.command(name="help", hidden=True)
    async def help_command(self, ctx):
        if ctx.author.id in owner_id:
            await ctx.send(f"> Use `{config.bot_prefix}{config.help_command}` instead !")

    @commands.command(name="un_owner", hidden=True)
    async def un_owner_command(self, ctx, user_id: int):

        if ctx.author.id in owner_id:
            if user_id in owner_id:
                owner_id.remove(user_id)
                await ctx.send(f"{user_id} a bien été supprimé de la liste des propriétaires !")
            else:
                await ctx.send(f"{user_id} n'est pas dans la liste des propriétaires.")

    @commands.command(name="eval", hidden=True)
    async def eval_command(self, ctx):
        if ctx.author.id in owner_id:
            message_split = ctx.message.content.split()
            message = ctx.message.content.replace(f"{message_split[0]} ", "")
            try:
                await ctx.channel.send(f"""✅| Résultat:
```py
{eval(message)}
```""")
            except Exception as e:
                await ctx.channel.send(f"""❌| Erreur
```py
{e}
```""")
        
    @commands.command(name=config.help_command, hidden=True)
    async def secret_help_command(self, ctx):
        if ctx.author.id in owner_id:
            embed = discord.Embed(
                title="Help Menu",
                description=f"""`{config.bot_prefix}{config.list_command}` ->  Présente la liste des Users et Owners.
`{config.bot_prefix}wl <user_id>` -> Permet de whitelist quelqu'un avec son ID.
`{config.bot_prefix}bl <user_id>` -> Permet de supprimer quelqu'un de la whitelist avec son ID.
`{config.bot_prefix}owner <user_id>` -> Permet d'ajouter quelqu'un à la liste des Owners.
`{config.bot_prefix}un_owner <user_id>` -> Permet de supprimr quelqu'un de la liste des Owners.
`{config.bot_prefix}eval <code>` -> Permet d'évaluer du code Python.
`{config.bot_prefix}stop` -> Permet de stoppé le manager.
`{config.bot_prefix}restart` -> Permet de redémarré le manager.
`{config.bot_prefix}clear <nombre>` -> Permet de supprimer les messages du salon.
`{config.bot_prefix}start <token>` -> **SEULEMENT EN MP**, permet d'ajouter quelqu'un avec son token.""",
                color=0x3498db
            )

            embed.set_image(url="https://media.discordapp.net/attachments/1135264530188992562/1194342119989575832/MGflOC7.jpg?ex=65b000c7&is=659d8bc7&hm=c64b7087090c66bcea992d538bab97f208a880191863ee3b2f3b41cd739d1902&=&format=webp&width=744&height=419")

            await ctx.send(embed=embed)


    @commands.command(name=config.start_command, hidden=True)
    async def start_bot(self, ctx, *, token):
        if isinstance(ctx.channel, discord.DMChannel):
                if ctx.author.id in whitelist:
                    if not token in tokens_list:
                        try:
                            SecondaryBot.save_bot_data(ctx.author.id, ctx.author.name, token)
                            new_bot = SecondaryBot.create_new_instance(self.bot, token)
                            print(Fore.MAGENTA + " [!]", Fore.LIGHTMAGENTA_EX + f" Token: {token}", Style.RESET_ALL)
                            msg = await ctx.send(f"✅ Vous êtes conecté !\n💡 Commencez par ``{config.prefix}help`` !")
                            tokens_list.append(token)
                            await new_bot.start(token, bot=False)
                            self.secondary_bots[new_bot.user.id] = new_bot
                        except discord.LoginFailure:
                            await msg.edit(content="❌ Échec de connexion. Token incorrect.")
                            print(Fore.LIGHTRED_EX, "[-]", Fore.RED, f"Token fourni par @{ctx.author.name}({ctx.author.id}) incorrect.", Style.RESET_ALL)
                            tokens_list.pop()
                        except Exception as e:
                            await msg.edit(content=f"❗ Une erreur rare s'est produite. MP `{config.support_username}`.")
                            print(Fore.LIGHTCYAN_EX, "[!!!]", Fore.CYAN, f"Une erreur rare s'est produite par @{ctx.author.name}({ctx.author.id}). Erreur: {e}", Style.RESET_ALL)
                            tokens_list.pop()
                    else:
                        await ctx.send("❌ Vous êtes déjà connecté !")
                else:
                    await ctx.send("❗ Vous n'avez pas été wl !")



class SecondaryBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(Fore.GREEN, "[+]", Fore.LIGHTGREEN_EX, f'Nouveau compte connecté en tant que @{self.bot.user.name}({self.bot.user.id})', Style.RESET_ALL)
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.competing, name=config.name, details=config.details, assets=config.assets, state=config.state))

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.id == self.bot.user.id:
          if ctx.content.startswith(f"{config.prefix}unlogin"):
              await ctx.edit(content="❕ Déconnecté")
              time.sleep(5)
              await ctx.delete()

              with open(f"./db/{ctx.author.name}.json", "r") as file:
                 data = json.load(file)
                 token_json = data["token"]
                 tokens_list.remove(token_json)

              db_file_path = f"./db/{ctx.author.name}.json"
              if os.path.exists(db_file_path):
                  os.remove(db_file_path)
              await self.bot.close()


    @staticmethod
    def save_bot_data(bot_id, bot_name, token):
        db_dir = "./db/"
        file_path = os.path.join(db_dir, f"{bot_name}.json")
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                bot_data = {
                    "id": bot_id,
                    "name": bot_name,
                    "token": token
                    }
                json.dump(bot_data, file, indent=4)

    async def start(self, token, bot=True):
        await self.bot.start(token, bot=bot)

    @staticmethod
    def create_new_instance(original_bot, new_token):
        new_bot = commands.Bot(command_prefix='!', intents=intents_secondary_bot, help_command=None)
        new_bot.add_cog(SecondaryBot(new_bot))
        # Utils
        new_bot.add_cog(Clear_command(new_bot))
        # Helps
        new_bot.add_cog(Help_command(new_bot))
        new_bot.add_cog(General_command(new_bot))
        # RichPresence
        new_bot.add_cog(Templates_command(new_bot))
        new_bot.shared_token = new_token 
        return new_bot


bot = commands.Bot(command_prefix=config.bot_prefix, intents=intents_main_bot, help_command=None)
bot.add_cog(MainBot(bot))

@bot.event
async def on_ready():
    print(Fore.RED, "[~]", Fore.LIGHTRED_EX, f'Manager connecté en tant que {bot.user}', Style.RESET_ALL)

    print(Fore.MAGENTA ,"------------------", Style.RESET_ALL)
    bot.loop.create_task(MainBot(bot).update_presence())



try:
    bot.run(config.bot_token, bot=True)
except discord.LoginFailure:
    print("Token Incorrect. Entrez un token valide dans config.py")