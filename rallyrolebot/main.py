import threading


import discord
from discord.ext import commands, tasks

import config
import data

from cogs import *

if __name__ == "__main__":
    config.parse_args()
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    default_prefix = config.CONFIG.command_prefix

    def prefix(bot, ctx):
        guildId = ctx.guild.id
        return data.get_prefix(guildId) or default_prefix

    bot = commands.Bot(command_prefix=prefix, intents=intents)
    bot.add_cog(role_cog.RoleCommands(bot))
    bot.add_cog(channel_cog.ChannelCommands(bot))
    bot.add_cog(rally_cog.RallyCommands(bot))
    bot.add_cog(defaults_cog.DefaultsCommands(bot))
    bot.add_cog(purchase_cog.PurchaseCommands(bot))
    bot.add_cog(update_cog.UpdateTask(bot))
    bot.run(config.CONFIG.secret_token)
