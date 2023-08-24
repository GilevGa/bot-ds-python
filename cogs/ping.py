import disnake
from disnake.ext import commands


class PingCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description='Показывает пинг бота')
        async def ping(ctx):
            ctx.send(f'Пинг бота сейчас: {round(bot.latency * 1000)} ms')

               
def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))