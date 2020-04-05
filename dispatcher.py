#!/usr/bin/env python3.8

import discord
import os

bot_id = os.environ['ES_DISPATCHER_DISCORD_API_ID']

class DispatcherDiscord(discord.Client):
    async def on_connect(self):
        print('Connected to Discord; proceeding with with login...')

    async def on_ready(self):
        print(f'Dispatcher {self.user} ready.')

dispatcher = DispatcherDiscord()
dispatcher.run(bot_id)