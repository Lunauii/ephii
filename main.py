import os
from keep_alive import keep_alive
import discord
from discord.ext import commands

import io
import aiohttp

import random

client = discord.Client()
client = commands.Bot(command_prefix='l?', help_command=None)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="in the sweet winter snow~ | l?help"))
    
    
    #Remove comments from below code to enter input mode.
    #This is to manually input messages to the directed channel, however, all preceeding commands will not work during input mode.

    #while True:
        #channel = client.get_channel(708953020829925409)
        #bop = input("")
        #await channel.send(bop)

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use l?help (command) for extended information on a command.", color = ctx.author.color)

    em.add_field(name = "Utility", value = "`no moderation commands added yet.`")
    em.add_field(name = "Fun", value = "`8ball`, `bonk`, `roll`, `rate`")
    em.add_field(name = "Informaion", value = "`status`, `help`")

    await ctx.send(embed = em)

## <-- THIS IS THE TEMPLATE FOR ADDING HELP DESCRIPTIONS FOR COMMANDS-->
#@help.command()
#async def command(ctx):
    #em = discord.Embed(title = "command", description = "command desc", color = ctx.author.color)

    #em.add_field(name = "**Syntax**", value = "`add syntax here`")

    #await ctx.send(embed = em)

@client.command()
async def test2arg(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))

@client.command(aliases=['hug'])
async def _hug(ctx):
  wholesome = ['You deserve this hug!',
                'Keep being you!',
                "You'll always be an amazing person!",
                'Hehe, get hugged!',
                '```py\nhug = warm\nif hug = warm\n    give @a hugs\n```',
                "I-I'm only doing this because I'm cold right now, o-okay??",
                'Fiiine. I guess you **are** my little pogchamp. Cmere you...']
  async with aiohttp.ClientSession() as session:
    async with session.get("https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500") as resp:
        if resp.status != 200:
            return await ctx.send('Could not download file...')
        data = io.BytesIO(await resp.read())
        await ctx.send(random.choice(wholesome), file=discord.File(data, 'hug.gif'))
@help.command()
async def hug(ctx):
    em = discord.Embed(title = "hug", description = "Sends a hug to the channel!", color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "`l?hug`")

    await ctx.send(embed = em)


@client.command()
async def bonk(ctx, members: commands.Greedy[discord.Member], *, reason ='no reason'):
    bonked = ", ".join(x.name for x in members)
    await ctx.send('<:LeafClub:750987107446816810>\n{} just got bonked for {}!'.format(bonked, reason))
@help.command()
async def bonk(ctx):
    em = discord.Embed(title = "bonk", description = "Bonk someone.", color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "`l?bonk <member> [reason]`")

    await ctx.send(embed = em)
  

@client.command(aliases=['status','changelog','clogs'])
async def changelogs(ctx):
    await ctx.send('Currently online running ``0.8.1209.0`` of LumiBot\nChangelogs for ``release 0.8.1209.0``:\n**Added** support for an indefinite run time for this bot.\n**Reworked** the old help command. Now the help command is passable to look at!\npatted noctush more\n*Bot made by Laphi#3668 and Shiroko#0001*\n*Lumia 2020-2021*')
@help.command(aliases=['status','changelog','clogs'])
async def changelogs(ctx):
    em = discord.Embed(title = "changelogs", description = "Read about the latest release.", color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "`l?changelogs`")
    em.add_field(name = "**Aliases**", value = "`status`, `changelog`, `clogs`")

    await ctx.send(embed = em)
    

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely',
                 'You may rely on it',
                 'As I see it, yes.',
                 'Most likely',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.',
                 'ur mom']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
@help.command(aliases=['8ball'])
async def _8ball(ctx):
    em = discord.Embed(title = "8ball", description = "Shake an 8ball!", color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "`l?8ball [question]`")

    await ctx.send(embed = em)


@client.command()
async def roll(ctx, *, dice):
    d20 = range(1, 20)  # num possibilities
    dicePerNum = 1  #how many dice to roll per value of 1
    num_dice = int(dice)
    for i in range(num_dice):
      diceGen = random.sample(d20, dicePerNum)  
      await ctx.send((f'You rolled a %s') % (diceGen))
@help.command()
async def roll(ctx):
    em = discord.Embed(title = "roll", description = "Roll a d20.", color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "`l?roll [amount of dice]`")

    await ctx.send(embed = em)


@client.command()
async def rate(ctx, *, arg):
    rating = ['1',
              '2',
              '3',
              '4',
              '5',
              '6',
              '7',
              '8',
              '9',
              '10']
    await ctx.send(f'I rate {arg} a {random.choice(rating)} out of 10.'.format(arg, rating))
@help.command()
async def rate(ctx):
    em = discord.Embed(title = "rate", description = "Make this bot rate something!", color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "`l?rate [reason]`")

    await ctx.send(embed = em)

keep_alive()
TOKEN = os.environ['TOKEN']
client.run(TOKEN)
