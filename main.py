import discord
from discord.ext import commands
from discord.ext.commands import Bot


bot: Bot = commands.Bot(command_prefix='/')


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
