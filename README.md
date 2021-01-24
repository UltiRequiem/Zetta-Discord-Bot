# Loli Bot
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/) [![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-green.svg)](https://github.com/EliazBobadilla/Python-UltiExtension-Pack-VSCode/commits/main)
This bot will be a moderation bot that will be focused on being **stable** rather than having new features.

### It will always be open source.

- Suport Server: https://discord.gg/n5kUSmwUMw

**The recommended platform to upload your bot is [Repl.it](https://repl.it)**

 Discord.py bot with commands extension

Basic template for a discord bot with the commands extension and [cogs](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html)

### Pre-Setup

If you don't already have a discord bot, click [here](https://discordapp.com/developers/), accept any prompts then click "New Application" at the top right of the screen.  Enter the name of your bot then click accept.  Click on Bot from the panel from the left, then click "Add Bot."  When the prompt appears, click "Yes, do it!" 

![Left panel](https://i.imgur.com/hECJYWK.png)

Then, click copy under token to get your bot's token. Your bot's icon can also be changed by uploading an image.

![Bot token area](https://i.imgur.com/da0ktMC.png)

### Setup

Create a file named `.env`

Add `DISCORD_BOT_SECRET=<your bot token>`

Your .env file should look something like this:

```
DISCORD_BOT_SECRET=<Bot token>
```

After adding your bot token to your .env file, navigate to line 10 in `main.py`. Change  `487258918465306634` to your user id. To get your id, ensure developer mode is enabled (Settings->Appearance->Advanced->Developer Mode) then right-click on yourself and click copy id.

When you hit start everything should startup fine.

### Uptime

So now, all you have to do to keep your bot up is setup something to ping the site your bot made every 5 minutes or so.

Go to [uptimerobot.com](https://uptimerobot.com/) and create an accout if you dont have one.  After verifying your account, click "Add New Monitor".

+ For Monitor Type select "HTTP(s)"
+ In Friendly Name put the name of your bot
+ For your url, put the url of the website made for your repl.
+ Select any alert contacts you want, then click "Create Monitor" 
![Uptime robot example](https://i.imgur.com/Qd9LXEy.png)

Your bot should now be good to go, with near 100% uptime.
