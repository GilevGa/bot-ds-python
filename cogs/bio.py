import disnake
from disnake.ext import commands


class BioCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description="Команда находится в стадии разработки")
        async def bio(ctx, *, bio_text):
            await ctx.send(f"КОМАНДА НЕ ДОСТУПНА")
            
def setup(bot: commands.Bot):
    bot.add_cog(BioCommand(bot))