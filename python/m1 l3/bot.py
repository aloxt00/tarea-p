import discord
from bot_logic import gen_pass
from bot_logic import flip_coin
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("hola! :)")
    elif message.content.startswith('$bye'):
        await message.channel.send("bye bye")
    elif message.content.startswith('$contra'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$gira_la_moneda'):
        await message.channel.send(flip_coin)
    else:
        await message.channel.send(message.content)

#client.run("MTI0Mjk4ODg4MjUwOTY5NzA2NQ.GcdoXK.ogmzG2vqoyuXoAnPn4j3L7m2OHUVImZAtzp9Uk")