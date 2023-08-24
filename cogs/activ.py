import disnake
from disnake.ext import commands


class ActivCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description="Changes bots activity")
        async def activ(ctx, *, activity):
            await bot.change_presence(activity=disnake.Game(name=activity))
            await ctx.send(f"Тепеь играет в {activity}")
            
            
def setup(bot: commands.Bot):
    bot.add_cog(ActivCommand(bot))