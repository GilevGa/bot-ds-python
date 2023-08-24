import disnake
from disnake.ext import commands


class WarnCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        @bot.slash_command(description="Выдаёт предупреждение пользователю")
        async def warn(ctx, member: disnake.Member, *, about: str):
            if member:
                embed = disnake.Embed(color = 0x537cda, description = f'Участник **{member.name}** получил предупреждение от **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
                await ctx.send(embed = embed)
            else:
                embed = disnake.Embed(color = 0x537cda, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
                await ctx.send(embed = embed)
            
def setup(bot: commands.Bot):
    bot.add_cog(WarnCommand(bot))