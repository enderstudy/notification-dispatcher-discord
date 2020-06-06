#!/usr/bin/env python3.8

import discord
import os
from aiohttp import web

bot_id = os.environ['ES_DISPATCHER_DISCORD_API_ID']
dev_id = int(os.environ['ES_DEVELOPER_DISCORD_USER_ID'])
api_port = os.environ['ES_DISPATCHER_API_PORT']
api_host = os.environ['ES_DISPATCHER_API_HOST']
class DispatcherDiscord(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop.create_task(DispatcherDiscord.start_api(self))

    async def on_connect(self):
        print('Connected to Discord; proceeding with with login...')

    async def on_ready(self):
        print(f'Dispatcher {self.user} ready.')

    async def dispatch_message(self, target, message):
        print(f"Received dispatch request for {target}.\nValidating target ID...")
        dispatch_target = await self.fetch_user(target)
        print("Dispatching requested message...")
        await dispatch_target.send(message)

    async def post_notify(self, req):
        # Check that the request content_type is json
        # Return 400 if content_type is not JSON
        # Check that the request is valid JSON
        # (try/except json.loads(req.content)) or the aiohttp equivalent
        # Return 400 if it is invalid JSON
        # Check that the request contains a nonzero number of notification jobs
        # Return 400 if the request contains no notification jobs
        # (check array length at specified level) *** consult spec
        # For each notification job, check that it has the required fields
        # (consult spec)
        # Return 400 if all jobs fail this check
        # Return 207 if request contains passing and failing jobs
        # Dispatch all passing jobs
        data = await req.json()
        print(data)
        response = {"response":200}
        print(f"Sending to {data['id']}:\n{data['message']}")
        await self.dispatch_message(data['id'], data['message'])
        return web.json_response(response)
    
    async def start_api(self):
        print(f"Starting Dispatcher API on {api_host}:{api_port}")
        api = web.Application()
        api.router.add_post('/notify', self.post_notify)
        runner = web.AppRunner(api)
        await runner.setup()
        site = web.TCPSite(runner, api_host, api_port)
        await site.start()


dispatcher = DispatcherDiscord()
dispatcher.run(bot_id)
