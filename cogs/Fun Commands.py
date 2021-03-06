import discord
from discord.ext import commands
from discord import Spotify
import time
import typing
import asyncio
import random
from aiohttp import ClientSession
import datetime
import time
import aiohttp
import os
import sys
import discord.utils
from discord import Game
import json
import requests
import pendulum

class Fun(commands.Cog):

    """{_*Fun Commands*_}"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def coinflip(self, ctx):
        """
        `Flip a coin`
        """
        responses = ["Heads", "Tails"]
        rancoin = random.choice(responses)
        await ctx.send(rancoin)
        
    @commands.command()
    async def meme(self, ctx):
        fetch = await ctx.send("Fetching Meme:", delete_after=0.5)
        await asyncio.sleep(1)
        req = requests.get("https://apis.duncte123.me/meme")
        meme = req.json()
        embed = discord.Embed(color=discord.Color.dark_blue(), timestamp=datetime.datetime.utcnow())
        embed.set_image(url=meme['data']['image'])
        embed.add_field(name="Quality Meme", value=f"{meme['data']['title']}")
        embed.set_footer(text=f"{meme['data']['url']}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['playb'])
    @commands.guild_only()
    async def playball(self, ctx):
        """
        `Have a chance at winning a basketball game`
        """

        woah = ['🏀 W 🏀\nNice, you dominated bruh', '❌ L ❌\nI mean it was close...', '➗ Tie ➗\nDamn bruh, you tied with the other team']

        outcome = random.choice(woah)
        
        positions = ['Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center']
        
        game = ['✅ Your shot\'s wet like water', '❌ You really just missed a wide open layup', '❌ You just got posterized 🤦🏽', '✅ Bruh, you just posterized that {random.choice(positions)}', '✅ You just made a mid-range fadeaway', '❌ You bricked that three', '✅ You swished that three bruh']
        
        var2 = random.choice(game)

        embed = discord.Embed(colour=discord.Colour.dark_orange(), title=f'{ctx.author.display_name}\'s Basketball Game')

        msg = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        embed2 = discord.Embed(colour=discord.Colour.dark_orange(), title=f"{ctx.author.display_name}\'s MidGame Stats:", description=f"**>**{var2}**<**")
        await msg.edit(embed=embed2)

        await asyncio.sleep(3)

        embed3 = discord.Embed(description=f'Outcome\n**>**{outcome}**<**', color=0x919234)
        await msg.edit(embed=embed3)

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        """`Adds two numbers together`"""
        embed = discord.Embed(description="")
        embed.add_field(name="Answer:", value=left + right)
        await ctx.send(embed=embed)

    @commands.command()
    async def embed(self, ctx, *, reason):
        """`Converts your message into an embed`"""
        embed = discord.Embed(title="", description=f"{reason}")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def hug(self, ctx, member: discord.Member):
        """`Hug somebody`"""
        embed = discord.Embed(description="**{1}** just hugged **{0}**".format(member.name, ctx.message.author.name), color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def bottles(self, ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
        """
        `{} bottles of {} on the wall!`
        """
        await ctx.send("{} bottles of {} on the wall!".format(amount, liquid))
    
    @commands.command()
    @commands.guild_only()
    async def punch(self, ctx, members: commands.Greedy[discord.Member], *, reason="No reason"):
        """
        `Punch somebody for whatever reason`
        """
        punched = ", ".join(x.name for x in members)
        embed = discord.Embed(description="**{}** just got punched for **{}**".format(punched, reason), color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx, members: commands.Greedy[discord.Member], *, reason="No reason"):
        """
        `Slap somebody for whatever reason`
        """
        slapped = ", ".join(x.name for x in members)
        embed = discord.Embed(description="**{}** just got slapped for **{}**".format(slapped, reason), color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.guild_only()
    async def hit(self, ctx, members: commands.Greedy[discord.Member], *, reason="No reason"):
        pass

    @commands.command()
    async def spotify(self, ctx, user: discord.Member=None):
        user = user or ctx.author
        for activity in user.activities:
            if isinstance(activity, Spotify):
                em = discord.Embed(color=discord.Color.dark_green())
                em.title = f'{user.name} is listening to: {activity.title}'
                em.set_thumbnail(url=activity.album_cover_url)
                em.description = f"**Song Name**: {activity.title}\n**Song Artist**: {activity.artist}\n**Song Album**: {activity.album}\n**Song Length**: {pendulum.duration(seconds=activity.duration.total_seconds()).in_words(locale='en')}"
                await ctx.send(embed=em)
                break
        else:
            embed = discord.Embed(description=f"{user.name} isn't listening to Spotify right now", color=discord.Color.dark_red())
            await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def iq(self, ctx):
        """
        `Tells you your IQ`
        """
        x = random.randint(1, 200)
        embed = discord.Embed(title="What's your IQ?🤨", description=f"Your IQ is {x}", color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    async def gay(self, ctx):
        """
        `Says how gay you are`
        """
        number = random.randint(1,100)
        embed = discord.Embed(title="Gay Rater", description=f'You are {number}% gay! 🏳️‍🌈 🏳️‍🌈 🏳️‍🌈', color=random.randint(0x000000, 0xffffff))
        await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def thot(self, ctx):
        """
        `Determines how much of a thot you are`
        """
        number = random.randint(1,100)
        embed = discord.Embed(title="Thotties be lurking 😏", description=f'You are {number}% of a thot!', color=random.randint(0x000000, 0xffffff))
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['bo'])
    @commands.guild_only()
    async def blackout(self, ctx, *, message):
        """`Blacks out your message (Testing)`"""
        msg = message.replace(" ", "||")

        await ctx.send(msg)


    @commands.command()
    @commands.guild_only()
    async def penis(self, ctx):
        """
        `Says the size of your penis`
        """
        try:
            responses = ['Your penis: 8=D',
                        'Your penis: 8==D',
                        'Your penis: 8===D',
                        'Your penis: 8====D',
                        'Your penis: 8=====D',
                        'Your penis: 8======D',
                        'Your penis: 8=======D',
                        'Your penis: 8========D',
                        'Your penis: 8=========D',
                        'Your penis: 8==========D']
            embed = discord.Embed(title="What's your penis size?", description=f'{random.choice(responses)}', color=random.randint(0x000000, 0xffffff))
            await ctx.channel.send(embed=embed)
        except Exception as error:
            raise(error)

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def hack(self, ctx, member:discord.Member = None):
        """
        `Hack somebody`
        """
        if not member:
            await ctx.send("Please mention a member")
            return

        passwords=['imnothackedlmao','sendnoodles63','ilovenoodles','icantcode','christianmicraft','server','icantspell','hackedlmao','WOWTONIGHT','69']
        fakeips=['154.2345.24.743','255.255. 255.0','356.653.56','101.12.8.6053','255.255. 255.0']

        embed = discord.Embed(title=f"**Hacking: {member}** 0%...", color=random.randint(0x000000, 0xffffff))
        m = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        embed = discord.Embed(title=f"**Hacking: {member}** 19%", color=random.randint(0x000000, 0xffffff))
        await m.edit(embed=embed)
        await asyncio.sleep(2)
        embed = discord.Embed(title=f"**Hacking: {member}** 34%", color=random.randint(0x000000, 0xffffff))
        await m.edit(embed=embed)
        await asyncio.sleep(2)
        embed = discord.Embed(title=f"**Hacking: {member}** 55%", color=random.randint(0x000000, 0xffffff))
        await m.edit(embed=embed)
        await asyncio.sleep(2)
        embed = discord.Embed(title=f"**Hacking: {member}** 67%", color=random.randint(0x000000, 0xffffff))
        await m.edit(embed=embed)
        await asyncio.sleep(2)
        embed = discord.Embed(title=f"**Hacking: {member}** 84%", color=random.randint(0x000000, 0xffffff))
        await m.edit(embed=embed)
        await asyncio.sleep(2)
        embed = discord.Embed(title=f"**Hacking: {member}** 99%", color=random.randint(0x000000, 0xffffff))
        await m.edit(embed=embed)
        await asyncio.sleep(2)
        embed = discord.Embed(title=f"**Hacking: {member}** 100%", color=random.randint(0x000000, 0xffffff))
        await m.edit(embed=embed)
        await asyncio.sleep(2)
        embed = discord.Embed(title=f"{member} info ", description=f"*Email `{member}@gmail.com` Password `{random.choice(passwords)}`  IP `{random.choice(fakeips)}`*", color=random.randint(0x000000, 0xffffff))
        embed.set_footer(text="You've totally been hacked 😏")
        await m.edit(embed=embed)
        await asyncio.sleep(3)

    @commands.command()
    @commands.guild_only()
    async def insta(self, ctx, username):
        """
        `Check out your/someone else's Insta`
        """
        url = f'https://apis.duncte123.me/insta/{username}'
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                data = r['user']
                username = data["username"]
                followers = data["followers"]["count"]
                following = data["following"]["count"]
                uploads = data["uploads"]["count"]
                biography = data["biography"]
                private = data["is_private"]
                verified = data["is_verified"]

                embed = discord.Embed(title=f'Insta Details: {username}')
                embed.add_field(name='Bio', value=biography + '\u200b', inline=False)
                embed.add_field(name='Private Status', value=private, inline=False)
                embed.add_field(name='Verified Status', value=verified, inline=False)
                embed.add_field(name='Followers', value=followers, inline=False)
                embed.add_field(name='Following', value=following, inline=False)
                embed.add_field(name='Posts', value=uploads, inline=False)
                await ctx.send(embed=embed)

    @insta.error
    async def insta_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description=f'❌ Please make sure to include the username\n```!insta <instagramhandle>```', color=discord.Color.dark_red())
            embed.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
            await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def fact(self, ctx):
        """
        `Says a random fact`
        """
        url = f'https://uselessfacts.jsph.pl/random.json?language=en'
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                fact = r['text']
                embed = discord.Embed(title=f'Random Fact', colour=random.randint(0x000000, 0xffffff), timestamp=ctx.message.created_at)

                embed.add_field(name='***Fun Fact***', value=fact, inline=False)
                await ctx.send(embed=embed)
                
    @commands.command(aliases=['8ball'])
    @commands.guild_only()
    async def _8ball(self, ctx, *, question):
        """
        `Ask a question and you'll receive a response`
        """
        responses = ['Of course',
                     'For sure',
                     '100%',
                     'Hell yeah',
                     'YES',
                     'Obviously, duh',
                     '-_-',
                     'Probably',
                     'I dont even understand',
                     'You tell me',
                     'Hell nahh to the nah nahh nahhh',
                     'Bad question',
                     'Is that even English?',
                     'Do I look like Albert Einstein?',
                     'Bruh.',
                     'Yeah probably not.',
                     'WHATT???']
        embed = discord.Embed(description=f'{ctx.author} asked: {question}\nAnswer: {random.choice(responses)}', color=random.randint(0x000000, 0xffffff))
        embed.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description=f'❌ Please make sure to include the question\n```!8ball <yourquestion>```', color=discord.Color.dark_red())
            embed.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
            await ctx.channel.send(embed=embed)

    @commands.command(aliases=['chat'])
    @commands.guild_only()
    async def letschat(self, ctx, *, question):
        """
        `Have a conversation with the bot`
        """
        responses = ['Hi there sorry if my chat is a bit off',
                    'I am just a test bot!',
                    'Yes',
                    'No',
                    'Sorry what was that?',
                    'I am still learning to improve',
                    'My creator is dumb and doesnt know how to program',
                    'Lmao',
                    'Whats your name? Mine isnt Andrew',
                    'Im doing great',
                    'Im not feeling the best',
                    'You are ugly',
                    'I like to play basketball',
                    'Flight is the best basketball player on the Earth',
                    'No cap',
                    'Cap',
                    'Are you dumb?',
                    'Congrats']
        embed = discord.Embed(description=f'{ctx.author} said: {question}\nAnswer: {random.choice(responses)}', color=random.randint(0x000000, 0xffffff))
        embed.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)

    @letschat.error
    async def letschat_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description=f'❌ Please make sure to include what you want to say\n```!letschat/chat <blabla>```', color=discord.Color.dark_red())
            embed.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
            await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
