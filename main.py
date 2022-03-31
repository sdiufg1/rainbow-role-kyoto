import discord
import asyncio
import random
import os



serverid = 959079750473768990
rainbowrolename = "zz"
delay = 5


client = discord.Client()
colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

async def rainbowrole(role):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("role detecté")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("probleme je peut pas edit le role.")
                    pass
                await asyncio.sleep(delay)
    print('le role avec le nom "' + rainbowrolename +'" a pas étais trouver')
    print("creation du role..")
    try:
        await client.get_guild(serverid).create_role(reason="création du rainbow role", name=rainbowrolename)
        print("role crée!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("j'ai pas pu crée le role assure toi que j'ai les perm !")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))

@client.event
async def on_ready():
    print("Je suis en ligne")
    client.loop.create_task(rainbowrole(rainbowrolename))

client.run(os.environ['token'])