import disnake
from disnake.ext import commands


class UserinfoCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description="Показывает информацию о пользователе")
        async def userinfo(ctx, member: disnake.Member):
            user =  member
            

            embed=disnake.Embed(title="USER INFO", description=f"Here is the info we retrieved about {user}", colour=user.colour)
            embed.add_field(name="NAME", value=user.name, inline=True)
            embed.add_field(name="NICKNAME", value=user.nick, inline=True)
            embed.add_field(name="ID", value=user.id, inline=True)
            embed.add_field(name="STATUS", value=user.status, inline=True)
            await ctx.send(embed=embed) 
            
def setup(bot: commands.Bot):
    bot.add_cog(UserinfoCommand(bot))