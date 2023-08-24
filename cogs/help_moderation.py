import disnake
from disnake.ext import commands


class HMD_Command(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description="Команды для модерациий")
        async def help_moderation(ctx):
            embed =disnake.Embed(title='Список команд', description='Список доступных команд для модератора:')
            embed.add_field(name='nicks', value='Изменяет ник участнику', inline=False)
            embed.add_field(name='kick', value='Кикает участника', inline=False)
            embed.add_field(name='ban', value='Банит участника', inline=False)
            await ctx.send(embed=embed)
            
def setup(bot: commands.Bot):
    bot.add_cog(HMD_Command(bot))