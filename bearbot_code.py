import discord
from discord.ext.commands import Bot
import random
import asyncio
from discord.utils import get
#------imports------

TOKEN = 'NTUxNTYxNTIyMjY3MTYwNTk2.D1yxqA.Ls636ozXvpIfraK5hWyXXCjJ_2M'
BOT_PREFIX = ("bearbot ", "Bearbot ")
client = Bot(command_prefix=BOT_PREFIX)
#------tokens------

RESPONSE_LIST = ["Hell yeah!!!!", "Hell no!!!!", "Fuck yeah!!!!", "Fuck no!!!!"]
BEAR_IMG = ["babybear.jpg", "unitbear.jpg", "bearface.jpg", "cub.jpg", "polarkiss.jpg",
            "familee.jpg", "stand.jpg", "sit.jpg", "wet.jpg", "baby.jpg", "hug.jpg"]
POSI_MSG = ["I think you're great!!!!", "I'm proud of you!!!!", "Keep it up!!!!",
            "You're loved!!!!", "You're doing great!!!!",
            "Don't forget to drink some water!!!!", "You're amazing!!!!",
            "Make sure you get some sleep!!!!", "I care about you!!!!",
            "It's *unbearable* to see you sad!!!! Cheer up!!!! I love you!!!!",
            "I love you a lot!!!!", "I believe in you!!!!", ]
OMEGAVERSE = [" is an alpha!!!!", " is an omega!!!!", " is a beta!!!!"]
TIKTOK = ["https://youtu.be/drLbsdaSft8", "https://youtu.be/jwOew-ycjP0",
          "https://youtu.be/2mi3lD8KzRo", "https://youtu.be/Tj-tQD0hngU" ]
PEGSCALE = [" gets pegged!!!!", " pegs!!!!", " does not peg or get pegged!!!!"]
TWUNKSCALE = [" is a bear!!!!", " is a cub!!!!", " is an otter!!!!", " is a twink!!!!",
              " is a chub!!!!", " is a twunk!!!!", " is a hunk!!!!"]
VERSESCALE = [" is a bottom!!!!", " is a verse!!!!", " is a top!!!!", " is a proud bottom!!!!",
              " is a proud verse!!!!", " is a proud top!!!!", " is a bottom in denial!!!!",
              " is a verse in denial!!!!", " is a top in denial!!!!", " is a bottom leaning verse!!!!",
              " is a top leaning verse!!!!", " is a service top!!!!", " is a power bottom!!!!"]
ABBASCALE = [" listens to abba!!!!", " does not listen to abba!!!!", " is a hardcore abba stan!!!!",
             " listens to abba but is ashamed of it!!!!", " does not know who abba is!!!!",
             " is currently listening to abba!!!!"]
BEARFACTS = ["Bears can live as long as 30 years in the wild!!!!",
             "Bears are bowlegged, giving them better grip & balance!!!!",
             "Bears can run up to 40 miles per hour!!!!",
             "Only the polar bear is a true carnivore!!!!",
             "A hibernating bear's heart rate can drop to 8 bpm!!!!",
             "Black bears are not always black, often being reddish brown, light brown or even white!!!!",
             "Unlike many mammals, bears can see in colour!!!!",
             "Pandas have an extra 'thumb' just for holding bamboo!!!!",
             "Around 98% of grizzly bears in the USA are in Alaska!!!!",
             "The word bear is Old English, derived from the Proto-Indo-European bher, meaning bright brown!!!!",
             "For many years, scientists thought the panda was actually a relative of the raccoon!!!!",
             "Much like dogs, bear claws are non-retractable!!!!",
             "The Ursa Major (Great Bear) constellation is the third-largest constellation, containing the Big Dipper!!!!",
             "A panda's eye is a vertical slit, allowing it to see by day and night!!!!",
             "Baloo from the Jungle Book is a sloth bear!!!!",
             "A grizzly's bite is estimated to be able to crush a bowling ball!!!!"]
             
             
#------lists------

@client.command(pass_context=True)
async def say(ctx, *args):
    args = args + tuple('!!!!')
    msg = ' '.join(args)
    return await client.say(msg)

@client.command(pass_context=True,
                name = 'is',
                aliases = ["am", "do", "does", "are",
                           "will", "can", "should", "could", "did", "have"])
async def question_yn(context):
    await client.say(random.choice(RESPONSE_LIST))

@client.command(pass_context=True,
                name='i',
                aliases = ['I', 'ily', 'ILY', 'we'])
async def love(context):
    await client.say('i love you too!!!!')

@client.command(pass_context=True,
                name = 'Bearpost',
                aliases = ['bearpost'])
async def bearpost(ctx):
    bear_img = random.choice(BEAR_IMG)
    with open(bear_img, 'rb') as picture:
              await client.send_file(ctx.message.channel, picture)

@client.command(pass_context=True,
                name = 'Posipost',
                aliases = ['posipost'])
async def posipost(ctx):
    posi_msg = random.choice(POSI_MSG)
    await client.say(posi_msg)

@client.command(pass_context=True,
                name = 'Omegaverse',
                aliases = ['omegaverse'])
async def omegaverse(ctx, *, message):
    if 'me' in message:
        message = ctx.message.author.mention
    else:
        message = message
    await client.say(message + random.choice(OMEGAVERSE))

@client.command(pass_context=True,
                name = 'Default',
                aliases = ['default'])
async def default(ctx):
    await client.say('https://youtu.be/s_DRwFLPuLw')

@client.command(pass_context=True,
                name = 'Tiktok',
                aliases = ['tiktok'])
async def tiktok(ctx):
    await client.say(random.choice(TIKTOK))

@client.command(pass_context=True,
                name = 'Pegscale',
                aliases = ['pegscale'])
async def pegscale(ctx, *, message):
    if 'me' in message:
        message = ctx.message.author.mention
    else:
        message = message
    await client.say(message + random.choice(PEGSCALE))

@client.command(pass_context=True,
                name = 'Validate',
                aliases = ['validate'])
async def validate(ctx, *, message):
    if 'me' in message:
        message = ctx.message.author.mention
    else:
        message = message
    await client.say(message + " is " + str(random.randint(0,100)) + "% valid!!!!")

@client.command(pass_context=True,
                name = 'Twunkscale',
                aliases = ['twunkscale'])
async def twunkscale(ctx, *, message):
    if 'me' in message:
        message = ctx.message.author.mention
    else:
        message = message
    await client.say(message + random.choice(TWUNKSCALE))

@client.command(pass_context=True,
                name = 'Versescale',
                aliases = ['versescale'])
async def versescale(ctx, *, message):
    if 'me' in message:
        message = ctx.message.author.mention
    else:
        message = message
    await client.say(message + random.choice(VERSESCALE))

@client.command(pass_context=True,
                name = 'Abbascale',
                aliases = ['abbascale', 'ABBAscale'])
async def abbascale(ctx, *, message):
    if 'me' in message:
        message = ctx.message.author.mention
    else:
        message = message
    await client.say(message + random.choice(ABBASCALE))

@client.command(pass_context=True,
                name = 'Bearfacts',
                aliases = ['bearfacts'])
async def bearfacts(ctx):
    await client.say(random.choice(BEARFACTS))

#------commands------

client.run(TOKEN)



