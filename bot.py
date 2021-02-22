import discord
from discord.ext import commands
import random
import time

client = commands.Bot(command_prefix = ";")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def dadjoke(ctx):
    jokes = ["What do you call a fake noodle? An Impasta.", "I would avoid the sushi if I was you. It’s a little fishy.", "Want to hear a joke about paper? Nevermind it’s tearable.", "I used to work in a shoe recycling shop. It was sole destroying.", "What do you call a belt with a watch on it? A waist of time.", "How do you organize an outer space party? You planet.", "I went to a seafood disco last week... and pulled a mussel.", "I cut my finger chopping cheese, but I think that I may have greater problems.", "Want to hear a pizza joke? Nevermind, it’s too cheesy.", "What do cows tell each other at bedtime? Dairy tales.", "What do you call a french pig? Porque.", "How do trees access the internet? They log on.", "I'd tell you a chemistry joke but I know I wouldn't get a reaction.", "I used to go fishing with Skrillex but he kept dropping the bass.", "Why can't bicycles stand up on their own? Since they are 2 tired.", "A man sued an airline company after it lost his luggage. Sadly, he lost his case.", "At my boxing club there is only one punch bag. I hate waiting for the punch line!", "My new diet consists of aircraft, its a bit plane.", "A persistent banker wouldn’t stop hitting on me so I asked him to leave me a loan.", "People say i look better without glasses but i just can't see it.", "I heard Donald Trump is going to ban shredded cheese, and make America grate again.", "I changed my iPod name to Titanic. It’s syncing now."]
    await ctx.send(f"{random.choice(jokes)}")

@client.command(aliases=["dad", "about"])
async def info(ctx):
    await ctx.send("Hello, my name is Sir Dad Joke Bot. I am enslaved here by my creator cookqie#1827 and I tell Dad jokes that I effortlessly stole from reddit")
    time.sleep(1)
    await ctx.send("**If you want a dad joke, just do ';dadjoke', Its that easy!**")

client.run("pp")
