#!/usr/bin/env python3.8

import discord
import os

bot_id = os.environ['ES_DISPATCHER_DISCORD_API_ID']
dev_id = int(os.environ['ES_DEVELOPER_DISCORD_USER_ID'])

class DispatcherDiscord(discord.Client):
    async def on_connect(self):
        print('Connected to Discord; proceeding with with login...')

    async def on_ready(self):
        print(f'Dispatcher {self.user} ready.')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await message.channel.send("DidahDiddit")
        print(f"Fetching dev user object: {dev_id}")
        dev_dm_id = await self.fetch_user(int(dev_id))
        print(f"Found object for dev user {dev_dm_id.name}.")
        await dev_dm_id.send("Didahdahdit")


# In the absence of an API to receive dispatch requests, demonstrate DM notifications when a user post receives a reaction.
#    async def on_reaction_add(reaction, user):
print(dev_id, bot_id)
dispatcher = DispatcherDiscord()
dispatcher.run(bot_id)