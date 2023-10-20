import discord
from discord.ext import commands
import responses

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = # Replace with your bot token
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        # Process the message and check if it's a private message
        is_private = isinstance(message.channel, discord.DMChannel)
        user_message = message.content

        # Respond to the message
        await send_message(message, user_message, is_private)

    bot.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot()

