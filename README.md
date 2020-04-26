# notification-dispatcher-discord
Dispatches Enderstudy notifications via Discord

# What does it do?
* It listens to a main server for notifications which must be dispatched.
* It then attempts to dispatch qualifying notifications via Discord.

# How does it listen?
* It maintains an HTTP server and awaits requests containing dispatch objects.

# How does it validate signals?
Basically:
* signal must contain properly formed data structure.
* signal objects must be destined for a *deliverable* Discord ID.

# How does it handle signal errors?
* Only the objects within the signal which are invalid or otherwise undeliverable will be rejected.
* Information regarding the rejected objects is delivered within a 207 reponse.

# How does it dispatch notifications?
* Forms message content from signal object.
* Forms request for delivery via Discord API.
* Dispatches notification asynchronously via Discord API.

## What's in a notification signal?
A notification signal processed by this application *must* include:
* *a destination identifier*: a user or team ID.
* *a related resource identifier*: ID of the originating resource or asset.
* *a notification type identifier*: further describes signal; used in processing the notification.
