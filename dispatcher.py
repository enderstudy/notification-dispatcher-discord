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
        await message.channel.send("Object successfully transferred to /dev/null.")
        print(f"Fetching dev user object: {dev_id}")
        dev_dm_id = await self.fetch_user(int(dev_id))
        print(f"Found object for dev user {dev_dm_id.name}.")
        await dev_dm_id.send(f"{message.author.mention}: {message.content}")

        request = {'id': 204254057202712576, 'message': 'Your post about furries was just downvoted!'}
        await dispatch_message(request[id], request[message])

    async def dispatch_message(self, target, message):
        print(f"Received dispatch request for {request[id]}.\nValidating target ID...")
        dispatch_target = await self.fetch_user(request[id])
        print("Dispatching requested message...")
        await dispatch_target.send(request[message])
        print("w00t!")

# In the absence of an API to receive dispatch requests, demonstrate DM notifications when a user post receives a reaction.
#    async def on_reaction_add(reaction, user):
dispatcher = DispatcherDiscord()
dispatcher.run(bot_id)