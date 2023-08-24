import random
from setting import config
from setting import info_server
import disnake  # Подключаем библиотеку
from disnake.ext import commands


bot = commands.Bot
bot = commands.InteractionBot()
#РАЗРЕШЕНИЯ
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix = config['prefix'], intents=intents)
help_command=None,
command_sync_flags=commands.CommandSyncFlags.all(),


# С помощью декоратора создаём первую команду

@bot.command(name='ping', description='Показывает пинг бота')
async def ping(ctx):
    ctx.send(f'Пинг бота сейчас: {bot.latency * 1000} ms')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} and ID: {bot.user.id}")

@bot.command()
async def rand(ctx, *arg):
    await ctx.reply(random.randint(0, 100))
@bot.command()
async def bio(ctx, *, bio_text):
    await ctx.send(f"Your bio has been set to: {bio_text}")

@bot.command()
async def helps(ctx):
    embed =disnake.Embed(title='Список команд', description='Список доступных команд:')
    embed.add_field(name='$rand', value='Случайное число', inline=False)
    embed.add_field(name='$hello', value='Поздороваться с ботом', inline=False)
    embed.add_field(name='$aboutme', value='Показать информацию о себе', inline=False)
    embed.add_field(name='$ping', value='Показывает пинг бота', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def help_moderatoin(ctx):
    embed =disnake.Embed(title='Список команд', description='Список доступных команд для модератора:')
    embed.add_field(name='$nicks', value='Изменяет ник участнику', inline=False)
    embed.add_field(name='$kick', value='Кикает участника', inline=False)
    embed.add_field(name='$ban', value='Банит участника', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def nicks(ctx, member: disnake.Member, new_nickname: str):
    await member.edit(nick=new_nickname)
    await ctx.send(f'Никнейм пользователя {member.mention} изменен на {new_nickname}.')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 1000):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f"Очищено **{amount}** сообщений")

@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: disnake.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = disnake.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Участник был замучен {member.mention} по причине {reason}")
    await member.send(f"Вы получили наказания на сервере {guild.name} по причине {reason}") 

@bot.command(description="Bans a member")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: disnake.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} was banned!")

@bot.command(description="Kicks a member")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: disnake.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} was kicked!")

@bot.command(description="Unbans a member")
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} was unbanned.")
            return


@bot.command(description="Показывает информацию о пользователе")
async def user_info(ctx):
    user = ctx.author

    embed=disnake.Embed(title="USER INFO", description=f"Here is the info we retrieved about {user}", colour=user.colour)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="NAME", value=user.name, inline=True)
    embed.add_field(name="NICKNAME", value=user.nick, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="STATUS", value=user.status, inline=True)
    embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
    await ctx.send(embed=embed)
    
@bot.command()
@commands.has_role(info_server['ID_STAFF'])
async def warn(ctx, member: disnake.Member, *, about: str):
    if member:
        embed = disnake.Embed(color = 0x537cda, description = f'Участник **{member.name}** получил предупреждение от **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
        await ctx.send(embed = embed)
    else:
        embed = disnake.Embed(color = 0x537cda, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
        await ctx.send(embed = embed)
        
#SLASH COMMAND

bot.load_extension("cogs.activ")
bot.load_extension("cogs.bio")
bot.load_extension("cogs.clear")
bot.load_extension("cogs.help_moderation")
bot.load_extension("cogs.helps")
bot.load_extension("cogs.nicks")
#bot.load_extension("cogs.ping")  # НЕИСПРАВНОСТЬ
bot.load_extension("cogs.rand")
bot.load_extension("cogs.userinfo")
bot.load_extension("cogs.warn") 


#BUTTONS
bot.run(config['token'])





