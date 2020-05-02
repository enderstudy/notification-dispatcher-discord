#!/usr/bin/env python3.8

import discord
import os
from aiohttp import web

bot_id = os.environ['ES_DISPATCHER_DISCORD_API_ID']
dev_id = int(os.environ['ES_DEVELOPER_DISCORD_USER_ID'])
api_port = 3333
api_host = 'localhost'
class DispatcherDiscord(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop.create_task(DispatcherDiscord.start_api(self))

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

    async def dispatch_message(self, target, message):
        print(f"Received dispatch request for {target}.\nValidating target ID...")
        dispatch_target = await self.fetch_user(target)
        print("Dispatching requested message...")
        await dispatch_target.send(message)

    async def post_notify(self, req):
        data = await req.json()
        print(data)
        response = {"response":200}
        print(f"Sending to {data['id']}:\n{data['message']}")
        await self.dispatch_message(data['id'], data['message'])
        return web.json_response(response)
    
    async def start_api(self):
        api = web.Application()
        api.router.add_post('/notify', self.post_notify)
        runner = web.AppRunner(api)
        await runner.setup()
        site = web.TCPSite(runner, api_host, api_port)
        await site.start()


dispatcher = DispatcherDiscord()
dispatcher.run(bot_id)
