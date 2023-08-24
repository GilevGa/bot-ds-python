import disnake
from disnake.ext import commands
import random

class RandCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description="Выводит случайное число от 0 до 100")
        async def rand(ctx, *arg):
            await ctx.send(random.randint(0, 100))

            
def setup(bot: commands.Bot):
    bot.add_cog(RandCommand(bot))