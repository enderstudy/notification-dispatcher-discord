# notification-dispatcher-discord
Dispatches Enderstudy notifications via Discord

# What does it do?
* It listens to a main server for notifications which must be dispatched.
* It then attempts to dispatch qualifying notifications via Discord.

# How does it listen?
* It maintains a constant, currently undefined connection with a main server.

# How does it validate notification signals?
Basically:
* signal must contain properly formed data structure.
* signal data structure must denote dispatching via Discord.

# How does it dispatch notifications?
* Forms message content from signal data structure.
* Forms request for delivery via Discord API.
* Dispatches notification asynchronously via Discord API.

## What's in a notification signal?
A notification signal processed by this application *must* include:
* *a destination identifier*: a user or team ID.
* *related resource identifier*: ID of the originating resource or asset
* *notification type identifier*: further describes signal; used in presenting the notification.
* delivery method identifier: used to determine whether the signal should be processed.