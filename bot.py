import discord
import responses
from discord.ext import commands
intents = discord.Intents.default()
intents.typing = False
intents.message_content = True

client = discord.Client(command_prefix='!', intents=intents)

@client.command()
async def send_bind(ctx):
    # Send an image
    with open('BINDMAP.png', 'rb') as image:
        await ctx.send(file=discord.File(image))

    # Send an image and store the message object
    sent_message = await ctx.send('Which bomb site would you like? React with 🅰️ or 🅱️')

    # Add reactions to the sent message
    await sent_message.add_reaction('🅰️')
    await sent_message.add_reaction('🅱️')


@client.event
async def on_raw_reaction_add(payload):
    # Check if the reaction is added by someone other than the bot
    if not payload.member.client:
        channel = await client.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        # Check if the bot sent the message and it contains an image
        if message.author == client.user and message.attachments:
            image_attachment = message.attachments[0]

            # Check which reaction was added
            if payload.emoji.name == '🅰️':
                await send_another_image(channel, 'ASITEBIND.png')
                await sent_message.add_reaction('1️⃣')
            elif payload.emoji.name == '🅱️':
                sent_message = await send_another_image(channel, 'BSITEBIND.png')
                await sent_message.add_reaction('1️⃣')
                await sent_message.add_reaction('2️⃣')

async def send_another_image(channel, image_path):
    # Send another image based on the selected reaction
    with open(image_path, 'rb') as image:
        await channel.send(file=discord.File(image))

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

    
def run_discord_bot():
    TOKEN = 'MTEyODgyMTYyNjA4NDAxMjIxMw.GJKD3x.1BC3Uwm0I-1LkNuEC5jiCTAq8G70lfKBj97O3g'
    client = discord.Client(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message=str(message.content)
        channel = str(message.channel)
        print(f'{username} said : "{user_message}" ({channel})')
        if user_message[0] == '?':
           user_message = user_message[1:]
           await send_message(message, user_message, is_private=True)
        else: await send_message(message,user_message, is_private=False)

    
    client.run(TOKEN)

    
