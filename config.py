"""CONFIG"""
#################
# Manager Part: #
#################

# Bot Token.
bot_token = ""
# Bot prefix.
bot_prefix = "!"
# Commande à envoyer en MP au bot (!start token_here).
start_command = "start"
# Bot commands.
list_command = "list"
help_command = "secret" # DO NOT ENTER "help" !
# ID de l'owner du bot
owner_id = ""
# Un nom d'utilisateur à MP en cas d'erreur (l'erreur sera print)
support_username = ""

owner_id = [int(owner_id)]
whitelist = [owner_id[0]]



# Streaming URL POUR LE MANAGER:
streaming_url = "https://www.twitch.tv/twitch"



"""Selfbot Settings"""
# Prefix du Selfbot.
prefix = "&"
# Temps de supression des messages.
deltime = 20
# Nom du Selfbot
selfbot_name = "Latency Selfbot"
# Competing RPC:
name = "☄"
details = None
state = "☄"
assets = {
    "large_image": "mp:attachments/1135264530188992562/1205872002238382111/PNjYcIL.png?ex=65ec67d1&is=65d9f2d1&hm=5fb7b7ed67a2ad93e4cd3786634a407085c1a61c38308f9fb9de4a511a5b7805&=&format=webp&quality=lossless",
    "large_text": None,
    "small_image": "mp:attachments/1135264530188992562/1206622218847518821/zQk1BeA.png?ex=65e5e802&is=65d37302&hm=a3d6b67b79094358729e44689449efa871943d408fdc319f49dfd1ba8dfa8705&=&format=webp&quality=lossless&width=419&height=419",
    "small_text": None
}