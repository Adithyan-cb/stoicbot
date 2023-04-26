import requests
import discord
# bot token and channel id
BOT_TOKEN = "MTA5NTkzMTI5MzYwMDA1NTMxOA.GAilCN.HR8AmnNnQ9xVDWFCjnLhUxepjDhJHcJOwEectU"
CHANNEL_ID = "1095935659811799131"

# getting the quotes from the API
URL = "https://api.themotivate365.com/stoic-quote"




# creating bot
client = discord.Client()

@client.event
async def on_ready():
    print("stoicbot is online")

# creating response
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content == "quote":
        response = requests.get(URL)
        quotes = response.json()
        author = quotes['author']
        quote = quotes['quote']
        snd_quote = f"{quote} --> {author}"
        await message.channel.send(snd_quote)

#running the bot
client.run(BOT_TOKEN)