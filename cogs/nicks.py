import disnake
from disnake.ext import commands


class NicksCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description="изменяет никнейм пользователя")
        async def nicks(ctx, member: disnake.Member, new_nickname: str):
            await member.edit(nick=new_nickname)
            await ctx.send(f'Никнейм пользователя {member.mention} изменен на {new_nickname}.')
            
def setup(bot: commands.Bot):
    bot.add_cog(NicksCommand(bot))