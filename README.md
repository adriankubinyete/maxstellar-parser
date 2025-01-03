## what
this bot will read maxstellar's biome macro message outputs on a discord server<br>
and ping specific roles when specific biomes happens<br>

## specifically, what
when the bot gets online, start reading every discord message sent (on every server your bot is on)<br>
if the message:
- is sent from a bot<br>
- contains an embed<br>
- embed has description<br>
- description starts with "Biome Started -"<br>
- biome on description is one of the configured biomes in biome dict<br>
<br>
we parse it, check what biome its announcing, and ping that specific biome role id<br>
everything else: just ignore<br>

## why
because maxstellar's biome macro doesnt allow you to set pings for each specific biome.<br>
as far as im aware, it only does one @everyone ping, ONLY for glitch biome.<br>
and in a biome hunting server context, individual biome pings is needed.<br>
maxstellar if youre reading this, make a way to config role_id pings for each biome!! :D

## how to use

- you need to configure server members intent (i forgot to disable that, too lazy to update) AND message contents intent on your discord bot, in discord's developer portal<br>
- edit the config variables in .env.example<br>
- rename .env.example to .env<br>
- install python dependencies with `pip install -r <path_to_requirements.txt>/requirements.txt`<br>
- run application with `py <path_to_main.py>/__main__.py`<br>
<br>
if everything is configured properly, it should say something like 1 module/cog loaded<br>
if it errors out and it mentions logging: you probably set up the wrong log path<br>
if it errors out and it mentions intents: your bot is probably misconfigured in discord's deveoper portal (intents part)<br>

## TLDR quickstart

```bash
# edit .env.example variables
# rename .env.example to .env
# install python dependencies with the following:
pip install -r requirements.txt
# run bot with the following: 
py __main__.py
```
