import datetime

import asyncio
import discord
from discord.ext import commands


class Application(commands.Cog):
    """{_*Commands for taking an Application*_}"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def applymod(self, ctx, member: discord.Member = None):
        """`Apply for Moderator (Testing)`"""

        member = member or ctx.author

        def checkreact(reaction, user):
            return user.id == member.id and str(reaction.emoji) in ["✅", "❌"]

        applicationQuestions = [
            "What's your Minecraft IGN + Discord Username?",
            "How old are you? (If you feel uncomfortable saying this, just confirm if you're at least a teenager)",
            "What Time Zone do you live in? (So I know when you're online, and gives me a reason if you're not too active)",
            "Why do you want to be Moderator? Isn't it fun to play without any responsibilites?",
            "What will you do for the Discord Server?",
            "Anything else you want to say?",
        ]
        applicationAnswers = {}
        for question in applicationQuestions:
            answer = await GetMessage(self.bot, ctx, contentOne=question, timeout=250)

            if not answer:
                # They failed to input something as an answer
                await ctx.send(f"You failed to answer: `{question}`\nPlease be quicker answering next time!")
                return

            # We have a valid answer to a question, lets store it
            applicationAnswers[applicationQuestions.index(question)] = answer

        # We have finished asking questions, lets check they want to submit this before sending it off

        channel = self.bot.get_channel(709360360456454155)
        confirmation = await member.send("Are you sure you want to submit this application?")
        await confirmation.add_reaction("✅")
        await confirmation.add_reaction("❌")

        reaction, user = await self.bot.wait_for(
            "reaction_add", timeout=60.0, check=checkreact
        )
        if str(reaction.emoji) == "✅":
            async with member.typing():
                await member.send(
                    "Thank you for applying! Your application will be sent to the Owner soon"
                )

                # We need to sus out whether or not to split the application into separate
                # embeds or not due to embed ratelimits
                descriptionChunks = {}

                description = ""
                for key, value in applicationAnswers.items():
                    addition = f"{key+1}) {applicationQuestions[key]}\n{value}\n\n"

                    if (len(description) + len(addition)) > 1850 and len(addition) <= 1850:
                        # This is gonna be to big for 1 embed together, but its gucci on its own
                        # so lets split it and make 2 embeds

                        # Lets make the bigger of the two into a descriptionChunks and the other description
                        if len(description) > len(addition):
                            # the current description is bigger
                            descriptionChunks[description] = False
                            description = addition
                        else:
                            # the addition is bigger
                            descriptionChunks[addition] = False
                        continue

                    elif len(addition) > 1850:
                        # This line alone is to big for one embed description
                        if len(addition) < 2850:
                            # It can still technically fit into 1 embed
                            partOne = addition[:1850]
                            partTwo = addition[1850:]
                            descriptionChunks[partOne] = {'multipleEmbeds': False, 'fieldValue': partTwo}
                        else:
                            # Technically, it has to be less then 4k words or
                            # else we would not have been able to send ours
                            # and vice versa so make 2 embeds
                            partOne = addition[:1850]
                            partTwo = addition[1850:]
                            descriptionChunks[partOne] = False
                            descriptionChunks[partTwo] = False
                        continue

                    else:
                        # We should be safe to simply add this to our current
                        # description and carry on as we are
                        description += addition
                        continue

                else:
                    if description != "":
                        descriptionChunks[description] = False

                for key, value in descriptionChunks.items():
                    applicationEmbed = discord.Embed(
                        title="Application Answers",
                        description=key,
                        color=discord.Color.dark_orange(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    applicationEmbed.set_author(
                        name=f"Application taken by: {member.display_name}", icon_url=f"{member.avatar_url}"
                    )
                    applicationEmbed.set_footer(text=f"{member.display_name}")

                    if value != False:
                        # We need to add a field for the rest of the data
                        applicationEmbed.add_field(name='\uFEFF', value=value['fieldValue'])

                    await channel.send(embed=applicationEmbed)

        elif str(reaction.emoji) == "❌":
            await member.send("Application won't be sent")


async def GetMessage(
    bot, ctx, contentOne="Default Message", contentTwo="\uFEFF", timeout=100
):
    """
    This function sends an embed containing the params and then waits for a message to return

    Params:
     - bot (commands.Bot object) :
     - ctx (context object) : Used for sending msgs n stuff

     - Optional Params:
        - contentOne (string) : Embed title
        - contentTwo (string) : Embed description
        - timeout (int) : Timeout for wait_for

    Returns:
     - msg.content (string) : If a message is detected, the content will be returned
    or
     - False (bool) : If a timeout occurs
    """
    embed = discord.Embed(title=f"{contentOne}", description=f"{contentTwo}")
    sent = await ctx.send(embed=embed)
    try:
        msg = await bot.wait_for(
            "message",
            timeout=timeout,
            check=lambda message: message.author == ctx.author
            and message.channel == ctx.channel,
        )
        if msg:
            return msg.content
    except asyncio.TimeoutError:
        return False


def setup(bot):
    bot.add_cog(Application(bot))
