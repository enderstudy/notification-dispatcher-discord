#!/usr/bin/env python3.8

import discord
import os
import threading
from flask import Flask, request, jsonify, json

bot_id = os.environ['ES_DISPATCHER_DISCORD_API_ID']
dev_id = int(os.environ['ES_DEVELOPER_DISCORD_USER_ID'])

class DispatcherDiscord(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bg_api = self.loop.create_task(self.run_flask())

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

        dispatch_request = {'id': 204254057202712576, 'message': 'Your post about furries was just downvoted!'}
        await self.dispatch_message(dispatch_request['id'], dispatch_request['message'])

    async def dispatch_message(self, target, message):
        print(f"Received dispatch request for {target}.\nValidating target ID...")
        dispatch_target = await self.fetch_user(target)
        print("Dispatching requested message...")
        await dispatc0h_target.send(message)
        print("w00t!")

# Let's shoehorn flask back in here and watch as nothing works

    api = Flask(__name__)

    @api.route("/notify", methods=["POST"])
    async def notify(self):
        data = json.loads(request.data)
        print(data)
        await dispatcher.dispatch_message(data['id'], data['message'])

    async def run_flask(self):
        print("Running Flask...")
        await api.run(host='127.0.0.1', port=3333, daemon=True).start()

dispatcher = DispatcherDiscord()
dispatcher.run(bot_id)