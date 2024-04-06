import disnake
from disnake.ext import commands
import random


intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'Бот {bot.user} подключен к Discord!')


@bot.slash_command(name="камень", description="Выбрать камень в игре Камень, ножницы, бумага")
async def rock(ctx):
    await play(ctx, "камень")


@bot.slash_command(name="ножницы", description="Выбрать ножницы в игре Камень, ножницы, бумага")
async def scissors(ctx):
    await play(ctx, "ножницы")


@bot.slash_command(name="бумага", description="Выбрать бумагу в игре Камень, ножницы, бумага")
async def paper(ctx):
    await play(ctx, "бумага")


async def play(ctx, choice):
    choices = ['камень', 'бумага', 'ножницы']
    bot_choice = random.choice(choices)

    out = f"Вы выбрали: {choice}. Бот выбрал: {bot_choice}.\n"

    if choice == bot_choice:
        out += "Ничья!"
    elif (choices.index(bot_choice) + 1) % 3 == choices.index(choice):
        out += "Вы победили!"
    else:
        out += "Бот победил!"

    await ctx.send(out)


token = ''
bot.run(token)
