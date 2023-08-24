import disnake
from disnake.ext import commands


class ClearCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description="Очищает указанное количество сообщений")
        @commands.has_permissions(manage_messages=True)
        async def clear(ctx, amount: int = 1000):
            await ctx.channel.purge(limit = amount)
            await ctx.send(f"Очищено **{amount}** сообщений")
            
def setup(bot: commands.Bot):
    bot.add_cog(ClearCommand(bot))