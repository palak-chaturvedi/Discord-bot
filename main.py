import discord
from discord import embeds
import json
import random
import time
import gogo_scraper
from discord.ext import commands, tasks
import asyncio
from itertools import cycle
from quiz import Quiz
import discord
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL


client = commands.Bot(command_prefix='.')
client.remove_command("help")

status = cycle(

    ['Try .help', 'Prefix - .'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def battle(ctx, member: discord.Member):
    turn = 0
    mem = member.mention
    user = ctx.message.author.mention
    users = await get_bank_data()
    health_1 = await update_health(ctx.author)
    health_2 = await update_health(member)
    weapons_1 = []
    weapons_2 = []

    try:
        items_1 = users[str(ctx.author.id)]["weapon_bag"]

        weapons_1 = [li['item'] for li in items_1]

    except:
        weapons_1 = []
    try:
        items_2 = users[str(member.id)]["weapon_bag"]

        weapons_2 = [li['item'] for li in items_2]

    except:
        weapons_2 = []

    weapons_2 = ' '.join(weapons_2)
    weapons_1 = ' '.join(weapons_1)

    if user == mem:
        await ctx.send(f"You can't fight yourself {user}")
    else:
        await ctx.send(f"{mem} vs {user}, who will win?")
        while health_1 > 0 and health_2 > 0:
            print(turn)

            if turn == 0:
                await ctx.send(f"{user}: `punch heal surrender {weapons_1}` ")

                def check(m):
                    return m.content == "punch" or m.content == "lightningbeam" or m.content == "rasengan"or m.content == "sharingan" or m.content == "shadowclone" or m.content == "gentlefist" or m.content == "hasengeki" or m.content == "paperbomb" or m.content == "stars" or m.content == 'heal' or m.content == 'surrender' and m.author == ctx.message.author

                response = await client.wait_for('message', check=check)
                if "punch" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_2 > 0:
                        dmg = 5
                        embed = discord.Embed(title=f"{user} punches {member}",
                                              )
                        url = "https://c.tenor.com/DNAVRBItRtQAAAAC/naruto-punch.gif"
                        embed.set_image(url=url)
                        await ctx.send(embed=embed)
                        health_2 = health_2 - dmg

                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_2 <= 0:
                            await ctx.send(f"**{user} has won the battle**")
                            break
                    elif health_2 <= 0:
                        await ctx.send(f"**{user} has won the battle**")

                        break
                    turn = turn + 1
                if "rasengan" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_2 > 0:
                        dmg = 25

                        health_2 = health_2 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_2 <= 0:
                            await ctx.send(f"**{user} has won the battle**")
                            break
                    elif health_2 <= 0:
                        await ctx.send(f"**{user} has won the battle**")

                        break
                    turn = turn + 1
                if "stars" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_2 > 0:
                        dmg = 10

                        health_2 = health_2 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_2 <= 0:
                            await ctx.send(f"**{user} has won the battle**")
                            break
                    elif health_2 <= 0:
                        await ctx.send(f"**{user} has won the battle**")

                        break
                    turn = turn + 1
                if "paperbomb" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_2 > 0:
                        dmg = 50

                        health_2 = health_2 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_2 <= 0:
                            await ctx.send(f"**{user} has won the battle**")
                            break
                    elif health_2 <= 0:
                        await ctx.send(f"**{user} has won the battle**")

                        break
                    turn = turn + 1

                if "shadowclone" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_2 > 0:
                        dmg = 50

                        health_2 = health_2 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_2 <= 0:
                            await ctx.send(f"**{user} has won the battle**")
                            break
                    elif health_2 <= 0:
                        await ctx.send(f"**{user} has won the battle**")

                        break
                    turn = turn + 1
                if "lightningbeam" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_2 > 0:
                        dmg = 50

                        health_2 = health_2 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_2 <= 0:
                            await ctx.send(f"**{user} has won the battle**")
                            break
                    elif health_2 <= 0:
                        await ctx.send(f"**{user} has won the battle**")

                        break
                    turn = turn + 1
                if "sharingan" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_2 > 0:
                        dmg = 50

                        health_2 = health_2 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_2 <= 0:
                            await ctx.send(f"**{user} has won the battle**")
                            break
                    elif health_2 <= 0:
                        await ctx.send(f"**{user} has won the battle**")

                        break
                    turn = turn + 1
                if "gentlefist" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_2 > 0:
                        dmg = 50

                        health_2 = health_2 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_2 <= 0:
                            await ctx.send(f"**{user} has won the battle**")
                            break
                    elif health_2 <= 0:
                        await ctx.send(f"**{user} has won the battle**")

                        break
                    turn = turn + 1
                if "hasengeki" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_2 > 0:
                        dmg = 50

                        health_2 = health_2 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_2 <= 0:
                            await ctx.send(f"**{user} has won the battle**")
                            break
                    elif health_2 <= 0:
                        await ctx.send(f"**{user} has won the battle**")

                        break
                    turn = turn + 1

                if "heal" in response.content.lower():
                    if health_1 >= 5:
                        await ctx.send(f"{user} already has **{health_1}** health, they lose a turn")
                    else:
                        health_1 = health_1 + 5
                        await ctx.send(f"{user} now has **{health_1}** health")
                    turn = turn+1

                if "surrender" in response.content.lower():
                    await ctx.send(
                        f"{user} has surrendered with **{health_1}** health. {mem} has claimed victory with **{health_2}** health remaining")
                    health_1 = health_1 - 20
                    health_2 = health_2 - 10
                    break


            elif turn == 1:
                await ctx.send(f"{mem}: `punch heal surrender {weapons_2}`")

                def check(o):
                    return o.content == "punch" or o.content == "sword" or o.content == "paperbomb" or  o.content == "lightningbeam" or o.content == "rasengan"or o.content == "sharingan" or o.content == "shadowclone" or o.content == "gentlefist" or o.content == "hasengeki" or o.content == "stars" or o.content == 'heal' or o.content == 'surrender'and o.author == discord.Member

                response = await client.wait_for('message', check=check)
                if "punch" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 5

                        health_1 = health_1 - dmg
                        await ctx.send(f"{user} is down to **{health_1}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "sword" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 25

                        health_1 = health_1 - dmg
                        await ctx.send(f"{user} is down to **{health_1}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "stars" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 10

                        health_1 = health_1 - dmg
                        await ctx.send(f"{user} is down to **{health_1}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "paperbomb" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 50

                        health_1 = health_1 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "rasengan" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 50

                        health_1 = health_1 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "shadowclone" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 50

                        health_1 = health_1 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "lightblade" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 50

                        health_1 = health_1 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "hisengeki" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 50

                        health_1 = health_1 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "sharingan" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 50

                        health_1 = health_1 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "gentlefist" in response.content.lower():  # turn == 0 is here since it doesn't work
                    # sometimes
                    if health_1 > 0:
                        dmg = 50

                        health_1 = health_1 - dmg
                        await ctx.send(f"{mem} is down to **{health_2}** health")
                        if health_1 <= 0:
                            await ctx.send(f"**{mem} has won the battle**")
                            break
                    elif health_1 <= 0:
                        await ctx.send(f"**{mem} has won the battle**")

                        break
                    turn = turn - 1
                if "heal" in response.content.lower():
                    if health_2 >= 20:
                        await ctx.send(f"{mem} already has **{health_2}** health, they lose a turn")
                    else:
                        health_2 = health_2 + 5
                        await ctx.send(f"{mem} now has **{health_2}** health")
                    turn = turn - 1
                if "surrender" in response.content.lower():
                    await ctx.send(
                        f"{mem} has surrendered with **{health_2}** health. {user} has claimed victory with **{health_1}** health remaining")
                    health_1 = health_1 - 20
                    health_2 = health_2 - 10
                    break



        await update_health(ctx.author, health_1, "health")
        await update_health(member,health_2,"health")


@client.command()
async def hug(ctx, member: discord.Member):
    hug_gif = ["https://c.tenor.com/7xJoTToAJC8AAAAM/hug-love.gif",
               "https://c.tenor.com/5tkkWFegYvUAAAAM/hug-couple.gif",
               "https://c.tenor.com/I9U3UFzzk1EAAAAM/hug-love.gif",
               "https://c.tenor.com/wqCAHtQuTnkAAAAM/milk-and-mocha-hug.gif"]
    user = ctx.author.name
    url = random.choice(hug_gif)
    embed = discord.Embed(title=f"{user} hugs {member}")
    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()
async def push(ctx, member: discord.Member):
    user = ctx.author.name
    push_gif = ["https://c.tenor.com/R71xcA_f7V4AAAAM/push-wall.gif", "https://c.tenor.com/R-lcs_3Y0l0AAAAM/push.gif",
                "https://c.tenor.com/SGeVr5iFKREAAAAM/cute-angry.gif",
                "https://c.tenor.com/KNIPpcQb6woAAAAM/kids-kiss.gif"]
    url = random.choice(push_gif)
    embed = discord.Embed(title=f"{user} pushed {member.name}",
                          )

    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()
async def dance(ctx):
    user = ctx.author.name
    dance_gifs = ["https://c.tenor.com/W06knTv2yOUAAAAM/jetha-dance.gif",
                  "https://c.tenor.com/jYqfbfE5wU4AAAAM/yay-yes.gif",
                  "https://c.tenor.com/fJh-W38iA3oAAAAM/dance-kid.gif"]
    url = random.choice(dance_gifs)
    embed = discord.Embed(title=f"{user} is dancing",
                          )

    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()
async def slap(ctx, member: discord.Member):
    user = ctx.author.name
    slap_gifs = ["https://c.tenor.com/vr7tTAEuj1QAAAAM/baka-slap.gif",
                 "https://c.tenor.com/PTONt_7DUTgAAAAM/batman-slap-robin.gif",
                 "https://c.tenor.com/Sp7yE5UzqFMAAAAM/spank-slap.gif",
                 "https://c.tenor.com/mMGM1FfaXLgAAAAM/slap-cat.gif"]
    url = random.choice(slap_gifs)
    embed = discord.Embed(title=f"{user} slapped {member.name}",
                          )

    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()
async def pat(ctx, member: discord.Member):
    user = ctx.author.name
    pat_gifs = ["https://c.tenor.com/DCMl9bvSDSwAAAAM/pat-head-gakuen-babysitters.gif","https://c.tenor.com/GiI1f_yr4CcAAAAM/mialek-stray-souls.gif","https://c.tenor.com/f5asRSsfl-wAAAAM/good-boy-pat-on-head.gif"]

    embed = discord.Embed(title=f"{user} pats {member.name}",
                          )

    embed.set_image(url="https://c.tenor.com/Zd3o8HgqWKYAAAAC/milk-and-mocha-hug.gif")
    await ctx.send(embed=embed)


@client.command()
async def kick(ctx, member: discord.Member):
    user = ctx.author.name
    kick_gifs = ["https://c.tenor.com/5iVv64OjO28AAAAM/milk-and-mocha-bear-couple.gif","https://c.tenor.com/Jv9L6Rrml9QAAAAM/cat-kick.gif","https://c.tenor.com/SddY3UqUHOAAAAAM/kick-cartoon.gif"]

    embed = discord.Embed(title=f"{user} kick {member.name}",
                          )
    embed.set_image(url=random.choice(kick_gifs))
    await ctx.send(embed=embed)

@client.command()
async def clap(ctx):
    user = ctx.author.name
    clap_gifs=["https://c.tenor.com/Q5LEaA7QrXEAAAAM/tom-and-jerry-jerry-mouse.gif","https://c.tenor.com/6C5_s1rkeOsAAAAM/vadim-bun.gif"]
    embed = discord.Embed(title=f"{user} is clapping",
                          )
    embed.set_image(url=random.choice(clap_gifs))

    await ctx.send(embed=embed)


@client.command()
async def checkroles(ctx, member: discord.Member):
    a = member.roles
    print(a[0].name)


@client.command()
async def addrole(ctx):
    global name_id
    embed = discord.Embed(title=f"Get roles for this server.",
                          description="React on this message to get your role.\n 1. Uzumaki: React with 🍃 to be an "
                                      "uzumaki \n 2. Uchica : React with ⚡ to be an uchiha \n 3. Hyuga : React with 👁 "
                                      "to be an hyuga \n\n\n Please choose your roles wisely. They cannot be changed "
                                      "following the rules. Your progress and weapons will be based on your "
                                      "role.\n\nHappy Journey ",
                          colour=0x71368a)
    name = await ctx.send(embed=embed)
    name_id = name.id
    print(name_id)
    return name_id


@client.event
async def on_raw_reaction_add(payload):
    global name_id

    guild = client.get_guild(payload.guild_id)

    Uzumaki = discord.utils.get(guild.roles, name="Uzumaki")

    Uchiha = discord.utils.get(guild.roles, name="Uchiha")
    Hyuga = discord.utils.get(guild.roles, name="Hyuga")

    if payload.message_id == name_id:
        print("yess")
        def checkroles(member: discord.Member):
            a = member.roles
            roles = []
            for role in a:
                roles.append(role.name)

            if "Uzumaki" in roles:
                return False
            if "Uchiha" in roles:
                return False
            if "Hyuga" in roles:
                return False

            return True

        member = payload.member
        print(member)
        decide = checkroles(member)
        print(decide)
        if (decide):

            if payload.emoji.name == '🍃':
                print(f'Reacted with emoji {payload.emoji.name}')
                await payload.member.add_roles(Uzumaki)

            if payload.emoji.name == '⚡':
                print(f'Reacted with emoji {payload.emoji.name}')
                await payload.member.add_roles(Uchiha)

            if payload.emoji.name == '👁️':
                print(f'Reacted with emoji {payload.emoji.name}')
                await payload.member.add_roles(Hyuga)


@client.command()
async def beat(ctx, member: discord.Member):
    beat_gif = ["https://c.tenor.com/nd7nyGjayWoAAAAM/anime-mad.gif",
                "https://c.tenor.com/bbAQ2wzoecoAAAAM/spank-tom-and-jerry.gif",
                "https://c.tenor.com/EegpVQqEsEQAAAAM/bear-bears.gif",
                "https://c.tenor.com/18zJA41z5T4AAAAM/we-are-going-to-beat-you-to-death-cat.gif"]

    user = ctx.author.name

    embed = discord.Embed(title=f"{user} beats {member}",
                          )
    url = random.choice(beat_gif)
    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()
async def hello(ctx):
    await ctx.send("Hii😃")


@client.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")


@client.command()
async def help(ctx):
    embeding = discord.Embed(title="This is a bot designed by Palak#0457",
                             colour=0x206694,
                             description="1. Use  .help for help 🥰. \n\n 2. use.ping for ping🥱 \n\n 3. use .clap .slap .punch .beat .hug .push .battle + <member> and .dance to perform desired action \n\n 4. use .shop .buy .weapon_shop .buy_weapon .sell .eat <item_name> to increase your progress and health \n\n 5. your progress will decrease everytime your health touches zero \n\n 6. use .join to add bot in voice channel .play<url> to play url \n\n 7. Use .findAnime '<anime_name>' to find anime from gogoanime site \n\n 8. Use .getEpisode '<anime_name>' '<episode no.>' to get the desired episode \n\n 9. use .alert 'anime_name' 'channel_name' to add alerts on a specific channel.")

    await ctx.send(embed=embeding)


@client.command()
async def foo(ctx, arg):
    await ctx.send(arg)


@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


@client.command(aliases=["-", "sub"])
async def subtract(ctx, a: int, b: int):
    await ctx.send(a - b)


@client.command(aliases=["*", "mul"])
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)


@client.command(aliases=["/", "div"])
async def divide(ctx, a: int, b: int):
    await ctx.send(a / b)


def to_upper(argument):
    return argument.upper()


@client.command()
async def up(ctx, *, content: to_upper):
    await ctx.send(content)


@client.command()
async def createprofile(ctx, member: discord.Member = None):
    userName = ""
    userAge = ""
    questions = [
        "Please input your name/nickname:",
        "Please input your age:"
    ]
    await ctx.send(
        "Yo will be receiving two questions. One involving your name and the other your age.")

    async def askQuestion(question):
        await ctx.author.send(question)
        print("Waiting for reply...")
        userReply = await client.wait_for('message')
        print("User replied")
        return userReply.content

    userName = await askQuestion(questions[0])
    userAge = await askQuestion(questions[1])
    e = discord.Embed(title=str(userName) + "'s Profile", description=f"""
    Age: `{str(userAge)}`
    """)
    await ctx.send(embed=e)


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


####################################################################
####################################################################
# Main code starts :)

mainshop = [{"name": "Food", "price": 50, "health": 10},
            {"name": "Meal", "price": 100, "health": 100},

            ]

uzumakishop = [{"name": "Shadowclone", "price": 1000, "health": 80},
              {"name": "Stars", "price": 100, "health": 20},
              {"name": "Paperbomb", "price": 1000, "health": 25},
              {"name": "Rasengan", "price": 1000, "health": 50}]
uchihashop = [{"name": "Sharingan", "price": 1000, "health": 80},
              {"name": "Stars", "price": 100, "health": 20},
              {"name": "Paperbomb", "price": 1000, "health": 50},
              {"name": "Lightblade", "price": 1000, "health": 25}]
hyugashop = [{"name": "Gentlefist", "price": 1000, "health": 80},
              {"name": "Stars", "price": 100, "health": 20},
              {"name": "Paperbomb", "price": 1000, "health": 25},
              {"name": "Hasengeki", "price": 1000, "health": 50}]


@client.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance', color=discord.Color.red())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name='Bank Balance', value=bank_amt)
    await ctx.send(embed=em)


@client.command(aliases=['hel'])
async def health(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    health = users[str(user.id)]["health"]

    em = discord.Embed(title=f'{ctx.author.name} Health', color=discord.Color.blue())
    em.add_field(name="Your Health", value=health)
    await ctx.send(embed=em)


@client.command()
async def beg(ctx):
    beg_gif=["https://c.tenor.com/6KWWOtjSg0cAAAAM/milk-and-mocha-please.gif","https://c.tenor.com/0Ik1bWBf320AAAAM/cat-please-please.gif"]
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    embed = discord.Embed(title=f"{ctx.author.mention} Got {earnings} coins!!",
                          )
    url = random.choice(beg_gif)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)


@client.command(aliases=['wd'])
async def withdraw(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} coins')


@client.command(aliases=['dp'])
async def deposit(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, -1 * amount)
    await update_bank(ctx.author, amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} coins')


@client.command(aliases=['sm'])
async def send(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, -1 * amount, 'bank')
    await update_bank(member, amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} coins')


@client.command(aliases=['rb'])
async def rob(ctx, member: discord.Member):
    rob_gif = ["https://c.tenor.com/ra8wM8NJn2MAAAAM/rob-when-the-bread-timer-go-off-robert-petrov.gif","https://c.tenor.com/khLn9wuWeOkAAAAM/spongebob-meme.gif"]
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)

    if bal[0] < 100:
        await ctx.send('It is useless to rob him :(')
        return

    earning = random.randrange(0, bal[0])

    await update_bank(ctx.author, earning)
    await update_bank(member, -1 * earning)

    embed = discord.Embed(title=f"{ctx.author.mention} You robbed {member} and got {earning} coins",
                          )
    url = random.choice(rob_gif)
    embed.set_image(url=url)
    await ctx.send(embed=embed)



@client.command()
async def slots(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    final = []
    for i in range(3):
        a = random.choice(['X', 'O', 'Q'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author, 2 * amount)
        await ctx.send(f'You won :) {ctx.author.mention}')
    else:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(f'You lose :( {ctx.author.mention}')


@client.command()
async def shop(ctx):
    em = discord.Embed(title="Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        health = item["health"]
        em.add_field(name=name, value=f"Rs{price} | Health🔼 : {health}")

    await ctx.send(embed=em)


@client.command()
async def weapon_shop(ctx):
    em = discord.Embed(title="Weapon Shop")
    Nrole = discord.utils.find(lambda r: r.name == 'Uzumaki',
                              ctx.message.guild.roles)
    Srole = discord.utils.find(lambda r: r.name == 'Uchiha',
                              ctx.message.guild.roles)
    Hrole = discord.utils.find(lambda r: r.name == 'Hyuga',
                              ctx.message.guild.roles)

    print(ctx.author)
    print(Nrole)
    if Nrole in ctx.author.roles:
        for item in uzumakishop:
            name = item["name"]
            price = item["price"]
            health = item["health"]
            em.add_field(name=name, value=f"Rs{price} | Health🔻 : {health}")

    if Srole in ctx.author.roles:
        for item in uchihashop:
            name = item["name"]
            price = item["price"]
            health = item["health"]
            em.add_field(name=name, value=f"Rs{price} | Health🔻 : {health}")

    if Hrole in ctx.author.roles:
        for item in hyugashop:
            name = item["name"]
            price = item["price"]
            health = item["health"]
            em.add_field(name=name, value=f"Rs{price} | Health🔻 : {health}")



    await ctx.send(embed=em)


@client.command()
async def buy(ctx, item, amount=1):
    buy_gif = ["https://c.tenor.com/9q0utjnEeDkAAAAM/kikiapp-kikicat.gif","https://c.tenor.com/CFrESZGteiwAAAAM/cat-typing.gif","https://c.tenor.com/P0YuaFVi_dMAAAAM/want-futurama.gif"]
    await open_account(ctx.author)

    res = await buy_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return
    embed = discord.Embed(title=f"You just bought {amount} {item}",
                          )
    url = random.choice(buy_gif)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@client.command()
async def buy_weapon(ctx, item, amount=1):
    buy_gif = ["https://c.tenor.com/9q0utjnEeDkAAAAM/kikiapp-kikicat.gif","https://c.tenor.com/CFrESZGteiwAAAAM/cat-typing.gif","https://c.tenor.com/P0YuaFVi_dMAAAAM/want-futurama.gif"]

    await open_account(ctx.author)

    res = await buy_this_weapon(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return

    embed = discord.Embed(title=f"You just bought {amount} {item}",
                          )
    url = random.choice(buy_gif)
    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title="Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

    await ctx.send(embed=em)


@client.command()
async def weapon_bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["weapon_bag"]
    except:
        bag = []

    em = discord.Embed(title="Weapon Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

    await ctx.send(embed=em)


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "wallet")

    return [True, "Worked"]


async def buy_this_weapon(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    Nrole = discord.utils.find(lambda r: r.name == 'Uzumaki',
                               user.guild.roles)
    Srole = discord.utils.find(lambda r: r.name == 'Uchiha',
                               user.guild.roles)
    Hrole = discord.utils.find(lambda r: r.name == 'Hyuga',
                               user.guild.roles)

    print(Nrole)
    if Nrole in user.roles:
        print("yes")
        for item in uzumakishop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                price = item["price"]
                break
    if Srole in user.roles:
        print("yes")
        for item in uchihashop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                price = item["price"]
                break
    if Hrole in user.roles:
        print("yes")
        for item in hyugashop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                price = item["price"]
                break


    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["weapon_bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["weapon_bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["weapon_bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["weapon_bag"] = [obj]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "wallet")

    return [True, "Worked"]


@client.command()
async def sell(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1] == 3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    sell_gif=["https://c.tenor.com/9xge6Jr4lnUAAAAS/tired-the-mandalorian.gif","https://c.tenor.com/bjRu-zpj6XYAAAAM/money-donald-duck.gif"]

    embed = discord.Embed(title=f"You just sold {amount} {item}.",
                          )
    url = random.choice(sell_gif)
    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()
async def eat(ctx, item, amount=1):
    await open_account(ctx.author)
    eat_gif = ["https://c.tenor.com/Y_qbpKEMRPsAAAAM/anime-eating.gif","https://c.tenor.com/Y_qbpKEMRPsAAAAM/anime-eating.gif","https://c.tenor.com/7NuUEfEvHWoAAAAM/yato.gif"]
    res = await eat_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1] == 3:
            await ctx.send(f"You don't have {item} in your bag.")
            return
    embed = discord.Embed(title=f"You just ate {amount} {item}",
                          )
    url = random.choice(eat_gif)
    embed.set_image(url=url)
    await ctx.send(embed=embed)



async def sell_this(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.7 * item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost, "wallet")

    return [True, "Worked"]


async def eat_this(user, item_name, amount, health=None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if health == None:
                health = item["health"]
            break

    if name_ == None:
        return [False, 1]

    users = await get_bank_data()

    bal = await update_health(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_health(user, health, "health")

    return [True, "Worked"]


@client.command(aliases=["lb"])
async def leaderboard(ctx, x=1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    em = discord.Embed(title=f"Top {x} Richest People",
                       description="This is decided on the basis of raw money in the bank and wallet",
                       color=discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed=em)


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
        users[str(user.id)]["progress"] = 0
        users[str(user.id)]["health"] = 50

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open('mainbank.json', 'r') as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode='wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)
    bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank']

    return bal


async def update_health(user, change=0, mode='health'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change
    if (users[str(user.id)][mode] > 100):
        users[str(user.id)][mode] = 100

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)
    bal_h = users[str(user.id)]['health']

    return bal_h


# async def get(ctx, member: discord.Member):
#     users = await get_bank_data()
#     health = users[str(member.id)]
#     return health

players = {}



# command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in
@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()


# command to play sound from a youtube URL
@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing')

# check if the bot is already playing
    else:
        await ctx.send("Bot is already playing")
        return


# command to resume voice if it is paused
@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')


# command to pause voice if it is playing
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')


# command to stop voice
@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')


# command to clear channel messages
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been cleared")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']



@client.command()
async def text_to_owo(ctx,text:str):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    def last_replace(s, old, new):
        li = s.rsplit(old, 1)
        return new.join(li)

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))

    await ctx.send(text)

alerts = {}

@client.command(name='findAnime', help='Find anime based on search query. use gogoTitle to specify anime in the other '
                                    'commands')
async def findAnime(ctx, anime_name: str, base_url: str = gogo_scraper.BASE_URL):
    """
    Uses Gogoanime's (limited) search functionality to find the exact anime or anime the user wants to get info about.
    This is required because the other functions in this bot require the user to input the exact title used in Gogoanime.
    :param anime: Search query
    :param base_url: Base Gogoanime URL. Useful if the current default URL gets taken down
    :return: Iteratively outputs search results to discord chat
    """

    search = gogo_scraper.search(anime_name, "https://gogoanime2.org/")

    if (search is None) or (len(search) == 0):
        await ctx.send(f'Could not find anything.')
        return

    for res in search:
        anime = res
        output = f'''\n
                    Here is an anime I found:\n
                    Title: {anime['name']}
                    Released: {anime['released']}
                    link: {anime['link']}
                    gogoTitle: {anime['gogoTitle']}
                '''
        await ctx.send(output)

        await ctx.send('\nIs this the right anime? (Type "yes" to stop command, everything else shows the next result)')
        msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
        msg = str(msg.content).lower()

        if msg == 'yes' or msg == 'yeah' or msg == 'yup':
            break
        else:
            await ctx.send('Showing next result...')


@client.command(name='latestEpisode', help='Get latest episode of input anime. Please input the exact name'
                                        'which could be found using the "findAnime" command')
async def showLatestEpisode(ctx, anime: str, base_url: str = gogo_scraper.BASE_URL):
    """
    Gets the latest episode of the input anime
    :param ctx: Discord Context
    :param anime: Exact Gogoanime title/link
    :param base_url: Base Gogoanime URL. Useful if the current default URL gets taken down
    :return: Link and episode number of latest episode, or None if anime or episode was not found
    """
    latest = gogo_scraper.getLatestEpisode(anime, "https://gogoanime2.org/")
    latest_ep = latest['num']

    output = f'''\n
                Latest episode: \n
                Episode number: {latest_ep}
                Episode link: {latest["link"]}

            '''
    await ctx.send(output)


@client.command(name='getEpisode', help='Find whether a given episode is available. Please input the exact name'
                                     'which could be found using the "findAnime" command')
async def getEpisode(ctx, anime: str, ep_num: int, base_url: str = gogo_scraper.BASE_URL):
    """
    Check whether a particular eppisode is available
    :param ctx: Discord Context
    :param anime: Exact Gogoanime title/link
    :param ep_num: Required episode number
    :param base_url: Base Gogoanime URL. Useful if the current default URL gets taken down
    :return: Outputs to discord chat as to whether that specific episode is available
    """
    episode = gogo_scraper.getEpisode(anime, ep_num, "https://gogoanime2.org/")

    if episode is not None:
        await ctx.send(f'I was able to find the episode: {episode}')
    else:
        await ctx.send(f'Episode could not be found')


async def checkForNewEpisode(ctx, anime, ep, timeout, channel):
    """
    Task function, that acts as the inner loop which checks for the arrival of a new episode of a given anime
    This funciton is never called by the user directly.
    :param ctx: Discord Context
    :param anime: Exact Gogoanime title/link
    :param ep: Current latest episode number
    :param timeout: For what interval should the bot check for new episodes
    :param channel: To which channel should the bot output alert messages
    :return: None
    """
    try:
        while True:
            episode = gogo_scraper.getEpisode(anime, ep)
            if episode is not None:
                output = f'''\n
                        New episode of {anime} has been released \n
                        Episode number: {ep}
                        Link: {episode}
                        '''
                await channel.send(output)
                print(f'New episode has been found for {anime}')
                ep += 1
            else:
                print(f'New episode (ep={ep}) has not yet been found for {anime}')

            await asyncio.sleep(timeout)

    except asyncio.CancelledError:
        print(f'Alert for {anime} is cancelled')
        raise


@client.command(name='addAnimeAlert',
             help='Create an alert whenever a new episode of the provided anime is released on Gogoanime')
async def alert(ctx, anime: str, timeout: int = 100, channel_name: str = 'anime_alerts',
                base_url: str = gogo_scraper.BASE_URL):
    """
    Function to add a new anime alert. Creates a new task for each alert by making use of checkForNewEpisode()
    :param ctx: Discord Bot
    :param anime: Exact Gogoanime title/link
    :param timeout: For what interval should the bot check for new episodes
    :param channel_name: To which channel should the bot output alert messages
    :param base_url: Base Gogoanime URL. Useful if the current default URL gets taken down
    :return: None
    """
    guild = ctx.guild
    channel = discord.utils.get(guild.channels, name=channel_name)

    # Create a new alerts channel if it already does not exist
    if channel is None:
        try:
            await guild.create_text_channel(channel_name)
            channel = discord.utils.get(guild.channels, name=channel_name)

        except:
            await ctx.send(f'Could not create {channel_name} channel. Please create it manually or give permission to'
                           f' me.')
            return

    if anime in alerts:
        print('An alert for this anime already exists')
        await ctx.send("An alert for this anime already exists")
        return

    lastEpisode = gogo_scraper.getLatestEpisode(anime, "https://gogoanime2.org/")
    if lastEpisode is None:
        print('This anime is either not a valid gogoanime anime title, or no episodes exist. Cannot create alerts')
        await ctx.send(
            'This anime is either not a valid gogoanime anime title, or no episodes exist. Cannot create alerts')
        return

    await channel.send(f'Watching for new episodes of {anime}')
    latest_ep = lastEpisode['num']
    output = f'''\n
                        Latest episode of {anime} is: \n
                        Episode number: {latest_ep}
                        Link: {lastEpisode['link']}
                    '''
    await channel.send(output)

    nextEpisodeNumber = latest_ep
    nextEpisodeNumber += 1

    task = client.loop.create_task(checkForNewEpisode(ctx, anime, nextEpisodeNumber, timeout, channel))
    alerts[anime] = {"task": task, "channel": channel}


@client.command(name='stopAnimeAlert', help='Stop sending alerts for new episodes of the provided anime')
async def stopEpisodeWatch(ctx, anime: str):
    if anime in alerts:
        task = alerts[anime]
        task['task'].cancel()

        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=task['channel'])

        if channel is not None:
            await channel.send(f'Stopping alerts for new episodes of {anime}')

        print(f'Stopping alerts for new episodes of {anime}')
        await ctx.send(f'Stopping alerts for new episodes of {anime}')
        del alerts[anime]

    else:
        print('Could not find task')
        await ctx.send('Could not find task to stop')



client.run("ODk5NjAxNzQxNDE3NDQ3NDI2.YW1JaA.43EjF_eeY-wYoAR9MO7RMvK0rcQ")
