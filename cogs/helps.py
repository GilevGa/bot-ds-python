import disnake
from disnake.ext import commands


class HelpsCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description="Список доступных команд")
        async def helps(ctx):
            embed =disnake.Embed(title='Список команд', description='Список доступных команд:')
            embed.add_field(name='rand', value='Случайное число', inline=False)
            embed.add_field(name='hello', value='Поздороваться с ботом', inline=False)
            embed.add_field(name='Bio', value='Показать информацию о себе', inline=False)
            embed.add_field(name='ping', value='Показывает пинг бота', inline=False)
            await ctx.send(embed=embed)
            
def setup(bot: commands.Bot):
    bot.add_cog(HelpsCommand(bot))