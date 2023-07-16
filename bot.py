import discord
import responses
from discord.ext.commands import Bot
intents = discord.Intents.default()
intents.typing = False
intents.message_content = True

bot = Bot(command_prefix='!', intents=intents)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def lineups(ctx):
    # Send an image
    with open('BINDMAP.png', 'rb') as image:
        await ctx.send(file=discord.File(image))

    # Send an image and store the message object
    sent_message = await ctx.send('Which bomb site would you like? React with 🅰️ or 🅱️')

    # Add reactions to the sent message
    await sent_message.add_reaction('🅰️')
    await sent_message.add_reaction('🅱️')




async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

    
def run_discord_bot():
    TOKEN = 'MTEyODgyMTYyNjA4NDAxMjIxMw.GJKD3x.1BC3Uwm0I-1LkNuEC5jiCTAq8G70lfKBj97O3g'
    bot = Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')
    
    
    @bot.command()
    async def lineups(ctx):
    # Send an image
        await ctx.send("https://i.imgur.com/UH9nylK.png")

    # Send an image and store the message object
        sent_message = await ctx.send('Which bomb sites line ups are you looking for? React with 🅰️ or 🅱️')

    # Add reactions to the sent message
        await sent_message.add_reaction('🅰️')
        await sent_message.add_reaction('🅱️')
        


    @bot.listen('on_raw_reaction_add')
    async def raw_reac_add(payload):
        
    # Check if the reaction is added by someone other than the bot
        channel = await bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        
        if payload.user_id != bot.user.id:
            if payload.emoji.name == '🅰️':
                await channel.send("https://i.imgur.com/fCQhciZ.png")
                sent_message = await channel.send("You selected A Site.")
                await sent_message.add_reaction('1️⃣')
                await sent_message.add_reaction('2️⃣')
            

            elif payload.emoji.name == '🅱️':
                await channel.send("https://i.imgur.com/WZsWmbF.png")
                sent_message = await channel.send("You selected B Site.")
                await sent_message.add_reaction('1️⃣')
              
        
            elif payload.emoji.name == '1️⃣':
    
                if message.content == "You selected A Site.":
                        await channel.send("https://i.imgur.com/pP1jRP7.jpg")
                elif message.content == "You selected B Site.":
                    await channel.send("https://i.imgur.com/NRfFSvI.jpg")

            elif payload.emoji.name == '2️⃣':
                
                if message.content == "You selected A Site.":
                        await channel.send("https://i.imgur.com/WKA7Y4J.jpg")
                elif message.content == "You selected B Site.":
                    await channel.send("https://i.imgur.com/dTHtbSp.jpg")
    
    
                 

    
    bot.run(TOKEN)

    
