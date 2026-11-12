# This is the code for the Discord bot on my server, The Potato Kingdom.
# Requirements (pip install):
# discord.py
# Also create a file called "token.txt" in the same directory as this file to run it using your own token
# (use the Discord developer portal to generate the token)
# And a file called "welcome.txt" which has the ID for the welcome channel in your test server (e.g. 724810199180771358)
# (turn on developer mode in settings, right click your #welcome channel and select Copy ID)

import os

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

import random
import json

f = open('token.txt', 'r')
token_thing = f.read()
f.close()
TOKEN = token_thing

bot = commands.Bot(command_prefix="!", intents=discord.Intents().all())

f = open('welcome.txt', 'r')
WELCOME_CHANNEL = f.read()
f.close()

print('welcome is', WELCOME_CHANNEL)

s = open('stats.txt', 'r')
stats = json.loads(s.read())
s.close()

def check_channel(ctx):
	if ctx.channel.name == "bot-commands" or ctx.channel.name == "spam":
		return True
	else:
		return False

def save_stats():
	s = open('stats.txt', 'w')
	s.write(json.dumps(stats))
	s.close()
	
def get_stats(id):
	return stats[str(id)]
	
def create_stat(id):
	stats[str(id)] = {"potatoes": 0}
	
def get_total():
	n = 0
	for i in stats:
		n += stats[i]['potatoes']
		
	return n

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord! Yeet')
	await bot.change_presence(activity=discord.Game('return to potato'))

@bot.command(
	help="Uses some crazy logic to determine if pong is actually the correct value or not.",
	brief="Prints pong back to the channel."
)
async def ping(ctx):
	await ctx.channel.send("Pong!")
	
@bot.command(
	help="Use your imagination.",
	brief="Use your imagination."
)
async def imagine(ctx):
	await ctx.channel.send("dragon deez nuts across your face")
	
@bot.command(
	help="...",
	brief="..."
)
async def deez(ctx):
	await ctx.channel.send("Nuts.")
	
@bot.command(
	help="...",
	brief="..."
)
async def joe(ctx):
	await ctx.channel.send("Mama.")
	
@bot.command(
	help="I'm green",
	brief="I'm green"
)
async def imgreen(ctx):
	await ctx.channel.send("I would eat up a lime.")
	await ctx.channel.send("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Lime_-_whole_and_halved.jpg/235px-Lime_-_whole_and_halved.jpg")

@bot.command(
	help="Eat it",
	brief="Eat it"
)
async def potato(ctx):
	stuff = ["You ate a potato! :potato:",
		"You ate a sweet potato! :sweet_potato:",
		"You ate a potato with a fork! :potato: :fork_and_knife:",
		"You ate a potato with a spoon! :potato: :spoon:",
		"You ate a baked potato!",
		"You ate a hot potato! :fire: :potato:",
		"You ate an AI slop potato :robot:",
		"You ate a mashed potato. :potato:"
	]
		
	thing = random.choice(stuff)
	thing += " **+1 Potato**"
    
	if not str(ctx.author.id) in stats:
		create_stat(ctx.author.id)

	# add to stats
	if random.randint(1, 15) == 1:
		thing = "Nooo! You ate a poisonous potato. :face_vomiting: **-1 Potato**"
		stats[str(ctx.author.id)]["potatoes"] -= 1
	elif random.randint(1, 10) == 1:
		thing = "You ate a :sparkles: GOLDEN POTATO :sparkles:. Wow you got lucky **+2 Potatoes**"
		stats[str(ctx.author.id)]["potatoes"] += 2 # Another one.
	else:
		stats[str(ctx.author.id)]["potatoes"] += 1
	
	save_stats()
	
	await ctx.channel.send(thing)
	if thing == 'You ate a baked potato!':
		await ctx.channel.send('https://static.wikia.nocookie.net/minecraft_gamepedia/images/e/e0/Baked_Potato_JE4_BE2.png/revision/latest?cb=20190430222641')

def with_commas(number):
	return f"{number:,}"

@bot.command(
	help="View how many potatoes you ate and more.",
	brief="View how many potatoes you ate and more.",
	name="potatostats",
	aliases=["ps", "potatoes"]
)
async def baoidjfosidjfodij(ctx):
	if not(str(ctx.author.id) in stats):
		await ctx.channel.send('You have eaten **0** potatoes.')
		await ctx.channel.send('https://cdn.discordapp.com/attachments/696098718981816484/1074885299940892771/download_74.png')
	else:
		thing = get_stats(ctx.author.id)["potatoes"]
		
		if thing == 1:
			asdfjkl = '**' + with_commas(thing) + ' potato**'
		else:
			asdfjkl = '**' + with_commas(thing) + ' potatoes**'
			
		await ctx.channel.send('You have eaten ' + asdfjkl + '. :potato:')
		await ctx.channel.send('Total server-wide: **' + with_commas(get_total()) + '** :potato:')
		
@bot.command(
	help="Don't eat it",
	brief="Don't eat it",
)
async def banana(ctx):
	stuff = ['Ew, that tasted disgusting.',
			 'That was the coolest banana you\'ve eaten in your life.',
			 'This banana made you return to monke.',
			]
	
	await ctx.channel.send("You ate a banana! :banana: " + random.choice(stuff))

@bot.command(
	help="Eat it",
	brief="Eat it"
)
async def hotfood(ctx):
	await ctx.channel.send("Hot Food. We sit down to eat, and the potato's a bit hot. So I only put a little bit on my fork and I blow. *puff-puff* 'Til it's cool. Just cool. Then into the mouth. *hawlp* *click* Noice. And there's my brother, he's doing the same. *puff-puff* 'Til it's cool. Just cool. Into the mouth. *hawlp* *click* Noice! There's my mum, she's doing the same. *puff puff* 'Til it's cool. Just cool. Into the mouth. *hawlp* *click* Noice! But my dad. My dad, what does he do? He stuffs a great big chunk of potato into his mouth and then that really does it. His eyes pop out. He flaps his hands. He blows, he puffs, he yells, he bobs his head up and down. He spits bits of potato all over his plate and he turns to us and he goes, \"Watch out, everybody! The potato's really hot!\"")

@bot.command(
	help="The worse version of hot food",
	brief="The worse version of hot food"
)
async def friedfood(ctx):
	await ctx.channel.send("We sit down to YEET :joy::100: and the potato's :potato: a bit HOT :fire::joy::rofl::skull:, so I only put a little bit :pinching_hand: on my fork :fork_and_knife: and I blow :cloud: puff :loud_sound: puff :wind_blowing_face:, 'til it's cool :sunglasses:, just cool :cool:, into the mouth :lips: *hawlp* :astonished: *click* :point_up_2: NOICE :ok_hand::joy::rofl::thinking::grin:. And there's my brother :boy:, he's doing the same :potato: :cloud: puff :loud_sound: puff :wind_blowing_face:, 'til it's cool :snowflake:, just cool :ice_cube:, into the mouth :lips:, *hawlp* :astonished: *click* :point_up_2: NOICE :ok_hand::joy::rofl::thinking::grin:. There's my mum :woman:, she's doing the same :potato:, 'til it's cool :gem:, just cool :v:, into the mouth :lips: *hawlp* :astonished: *click* :point_up_2: NOICE :ok_hand::joy::rofl::thinking::grin:. But my dad :man:, my dad, what does he do? He stuffs :stuffed_flatbread: a great :grin: :b:ig chunk :poop: of potato :sweet_potato::potato: into his mouth :lips: and that really does it :boom:. His eyes :eyes: pop :balloon: out :outbox_tray:. He flaps :door: his hands :raised_hand::raised_back_of_hand:. He blows :wind_blowing_face: he puffs :cloud: he yells :loudspeaker: he bobs his head :skull: up :chart_with_upwards_trend: and down :chart_with_downwards_trend:. He spits :wind_blowing_face: bits :pinching_hand: of potato :potato: all over his plate :fork_knife_plate: and he turns :point_left: to us :flag_us: and he goes :goal:, \"Watch out :outbox_tray: everybody! The potato's :potato: really :boom: HOT! :fire::rocket::sparkles::rofl::joy:\"")

@bot.command(
	help="The worse version of hot food",
	brief="The worse version of hot food"
)
async def coldfood(ctx):
	await ctx.channel.send("Cold Food. We sit down to _BRRRRRRRRRR_ **AHHHH IT'S SO COLD** __HELPP!!!!!!!!!!!__ :cold_face::cold_sweat::ice_cube::snowflake::gem:")

@bot.command(
	help="LOL i'm so random!!!1",
	brief="Prints a random number",
	name="randomnumber"
)
async def lolrandom(ctx, *args):
	if len(args) == 0:
		await ctx.channel.send(random.randint(0, 10))
	elif len(args) == 1:
		await ctx.channel.send(random.randint(0, int(args[0])))
	else:
		await ctx.channel.send(random.randint(int(args[0]), int(args[1])))

@bot.command(
	help="Displays approximately how long ago Bongs uploaded his latest video",
	brief="Displays approximately how long ago Bongs uploaded his latest video",
	name="whenlastvideo",
	aliases=["whenlatestvideo", "whenlastvid", "whenlatestvid"]
)
async def asdfjklasdfjkl(ctx):
	y = random.randint(100, 10000000)

	await ctx.channel.send("Bongs uploaded his latest video **" + str(f'{y:,}') + "** years ago :cry:")

@bot.command(
	help="hi",
	brief="Displays Minecraft player heads",
	name="head"
)
async def playerhead(ctx, *args):
	if len(args) == 0:
		await ctx.channel.send("Usage: !head <player name>")
	elif len(args[0]) > 20:
		await ctx.channel.send("**:x: Username is too long!**")
	elif len(args[0]) < 3:
		await ctx.channel.send("**:x: Username is too short!**")
	else:
		await ctx.channel.send("https://minotar.net/helm/" + str(args[0]) + "/128")

@bot.command(
	help="Get free candy!!!!1",
	brief="Get free candy!!!!1",
)
async def freecandy(ctx):
	things = [
		['Nope.', 'https://media1.giphy.com/media/Ju7l5y9osyymQ/200.gif'],
		['Get in.', 'https://i.kym-cdn.com/entries/icons/facebook/000/004/473/free-candy.jpg'],
		['Sorry, all I\'ve got is this.', 'http://www.familyvacationhub.com/wp-content/uploads/2016/06/ready-candy-bar-create-your-own-candy-bar-hersheys-chocolate-world-320x240.jpg'],
	]

	random_thing = random.choice(things)
	
	await ctx.channel.send(random_thing[0])
	await ctx.channel.send(random_thing[1])

@bot.command(
	help="Do some quick maffs(TM)",
	brief="Do some quick maffs(TM)",
	name="1+1"
)
async def quickmath(ctx):
	numberthing = random.randint(0, 10)
	
	if numberthing == 2:
		if random.randint(0, 1) == 0:
			await ctx.channel.send("Uhhhh... it's... sorry, I'm too busy programming the potato and eating the computer.")
		else:
			await ctx.channel.send("Uhhhh... it's... sorry, I'm too busy cleaning the lawn and mowing my room.")
	else:
		await ctx.channel.send(str(numberthing))
		
@bot.command(
	help="rules",
	brief="rules"
)
async def rules(ctx):
	if ctx.author.id == 639259314074157077:
		await ctx.message.delete() # delete me typing !rules
		await ctx.channel.send("https://media.discordapp.net/attachments/757438612173357097/850224226070036480/20200923_080750.png")
		
		def turn_thing_into_rules(thing, color):
			embed=discord.Embed(color=color)
		
			stuff = thing.split('\n')
			for rule in stuff:
				if rule.startswith('[nobullet]'):
					embed.add_field(name='', value=rule[len('[nobullet]'):], inline=False)
				else:
					embed.add_field(name='', value='• ' + rule, inline=False)
				
			return embed
		
		part1 = '''Don't intentionally try to start drama, maliciously bait, and/or personally attack other server members. We're trying to preserve a peaceful and friendly environment, therefore any attempts to create a toxic atmosphere will be punished accordingly.
Any form of discrimination will not be tolerated. This includes discrimination against a certain race, country, religion, sexuality, gender and/or group.
Do NOT send other members, nor anyone’s personal information; regardless if it has been said by them before, even if you are granted permission.
Topics on committing crime, such as piracy, acts of violence, doxxing, etc will not be tolerated and will result in an instant mute or ban depending on the severity.
Do not bring your personal drama into the server with you. If you're having any type of argument with someone that especially seems personal in nature, leave it in DMs until the conflict is resolved.
Keep controversial or sensitive topics (for example, controversial topics relating to politics, religion, controversial figures, etc.) out of the server.
This is an NSFW-free server. Do not discuss any NSFW topics nor post NSFW material on this server. NSFW includes content such as nudity, intense profanity, gore, obscenity, or other potentially disturbing subject matter. If you are unsure, ask any mod in DMs and we'll gladly help you understand.
Joking is allowed but make sure it is in the bounds of the rules, covering up offensive remarks, hate speech, NSFW, or any of the likes with jokes will be dealt with the same as if you are not joking.'''

		part2 = '''Please keep your messages and content relevant and on-topic with the channel.
Memes are allowed in #general, though please keep it on-topic and relevant. Any content being posted that deviates too far from the topic at that time should be posted in its respective channel.
Spamming is strictly prohibited outside #botspam. Any form of blatant self-promoting, superfluous images/gifs, excessive bot commands and reactions will be dealt with accordingly.
Self promotion should only be in #promo and no conversations should occur there, to leave space for the promotional content.'''

		part3 = '''[nobullet]There might be a time you will interact with other users in a voice channel, so make sure to follow these etiquettes and guidelines to have a great time!
Be respectful
Don't be extremely loud or purposely annoy others
Reduce background noise (if possible)
Take turns speaking
Courtesy, language, and online decency applies here.'''

		part4 = '''[nobullet]Follow Discord TOS (this includes following the age guideline in your country)
https://discord.com/terms
https://discord.com/guidelines'''

		other = '''Staff reserve the right to persecute anyone if they see fit. This includes people who are being a nuisance and try to start fights. This is a catch-all rule designed to circumvent people who become belligerent but still technically follow the rules above.
Do not use alts for malicious purposes or attempt to circumvent punishments. You are not allowed to try to avoid punishments with alts or otherwise try to free yourself from your offenses.
Don't backseat moderate. If you feel as though a member is breaking a rule of the server or is acting inappropriately in any fashion, ping a moderator and they'll deal with the issue.
Use your common sense, do not find loopholes, you are still going to get punished.
Have a potato :potato:'''
		
		await ctx.channel.send("**:one: Courtesy, language, and online decency:**")
		await ctx.send(embed=turn_thing_into_rules(part1, discord.Color.orange()))
		
		await ctx.channel.send("**:two: Channels and content:**")
		await ctx.send(embed=turn_thing_into_rules(part2, discord.Color.gold()))
		
		await ctx.channel.send("**:three: Voice channel etiquette:**")
		await ctx.send(embed=turn_thing_into_rules(part3, discord.Color.green()))
		
		await ctx.channel.send("**:four: Discord Terms and Guidelines:**")
		await ctx.send(embed=turn_thing_into_rules(part4, discord.Color.blue()))
		
		await ctx.channel.send("**:five: Other:**")
		await ctx.send(embed=turn_thing_into_rules(other, discord.Color.blurple()))
		
		
	else:
		await ctx.channel.send("Sorry, only Bongs can run this >:)")

@bot.command(
	help="Da ba dee, da ba die!!!",
	brief="Generates random misheard lyrics for the song I'm Blue"
)
async def imblue(ctx):
	first_words = [
	{
		"word":"dee",
		"p":"n"
	},
	{
		"word":"bleed",
		"p":"v"
	},
	{
		"word":"green",
		"p":"a"
	},
	{
		"word":"beat",
		"p":"v"
	},
	{
		"word":"need",
		"p":"v"
	},
	{
		"word":"yeet",
		"p":"v"
	},
	{
		"word":"meme",
		"p":"n"
	},
	{
		"word":"geek",
		"p":"n"
	},
	{
		"word":"dream",
		"p":"n"
	},
	{
		"word":"eat",
		"p":"v"
	},
	{
		"word":"heat",
		"p":"v"
	},
	{
		"word":"pee",
		"p":"v"
	},
	{
		"word":"tree",
		"p":"n"
	},
	{
		"word":"believe",
		"p":"v",
		"twoSyllables":True
	},
	{
		"word":"diseased",
		"p":"n",
		"twoSyllables":True
	},
	{
		"word":"deceased",
		"p":"n",
		"twoSyllables":True
	},
	{
		"word":"indeed",
		"p":"n",
		"twoSyllables":True
	}
	]

	second_words = [
	{
		"word":"dye",
		"p":"n"
	},
	{
		"word":"die",
		"p":"v"
	},
	{
		"word":"guy",
		"p":"n"
	},
	{
		"word":"fly",
		"p":"v"
	},
	{
		"word":"pie",
		"p":"n"
	},
	{
		"word":"mine",
		"p":"n"
	},
	{
		"word":"guy",
		"p":"n"
	},
	{
		"word":"diet",
		"p":"n"
	},
	{
		"word":"diamond",
		"p":"n"
	},
	{
		"word":"lie",
		"p":"n"
	},
	{
		"word":"dime",
		"p":"n"
	},
	{
		"word":"why",
		"p":"all"
	},
		{
		"word":"guide",
		"p":"n"
	}
	]

	stuff = {
	"n":[
		"I'm a",
		"up a",
		"apple",
		"I'm in",
		"on a"
	],
	"v":[
		"I will",
		"I would",
		"I can",
		"I could",
		"I will",
		"imma",
		"I must"
	],
	"a":[
		"I am"
	],
	"all":[
		"da ba",
		"cobble"
	]
	}

	lyric = ""

	first = random.choice(first_words)
	first_phrase = ""

	second = random.choice(second_words)
	second_phrase = ""

	if "twoSyllables" in first:
		if first["p"] == "n":
			first_phrase = "I'm"
		else:
			first_phrase = "I"
	else:
		first_phrase = random.choice(stuff[first["p"]])
		if random.random() <= 0.1:
			first_phrase = random.choice(stuff["all"])

	second_phrase = random.choice(stuff[second["p"]])
	if random.random() <= 0.1:
		second_phrase = random.choice(stuff["all"])
	
	lyric = first_phrase.capitalize() + " " + first["word"] + " " + second_phrase + " " + second["word"]
	
	await ctx.channel.send(lyric)

@bot.event
async def on_member_join(member):
	await bot.get_channel(int(WELCOME_CHANNEL)).send(f"**Hey {member.mention}, welcome to Bongs237's server!**\nHere's a free potato: :potato:")

@bot.event
async def on_message(message):
	if message.content.lower() == "i like potatoes" or message.content.lower() == "i like potatos" or message.content.lower() == "i love potatoes" or message.content.lower() == "i love potatos":
		if random.randint(0, 1) == 0:
			await message.channel.send("Same!")
		else:
			await message.channel.send("Based")
	elif message.content.lower() == 'i like bananas':
		await message.channel.send('Bananas are cool')
	elif message.content.lower() == 'pogtato' and int(message.author.id) != 830846246062391307: # make sure it's not potatobot that's saying it
		await message.channel.send('pogtato')
	elif message.content.lower() == "i'm not a dirt block" or message.content.lower() == "im not a dirt block":
		await message.channel.send('After all')
		
	rickroll = [
		'never gonna give you up',
		'never gonna let you down',
		'never gonna run around and desert you',
		'never gonna make you cry',
		'never gonna say goodbye',
		'never gonna tell a lie and hurt you'
	]
	
	if message.content.lower() in rickroll and int(message.author.id) != 830846246062391307:
		index = rickroll.index(message.content.lower()) + 1
		if index < len(rickroll):
			await message.channel.send(rickroll[index].capitalize())

	# INCLUDES THE COMMANDS FOR THE BOTS. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
	await bot.process_commands(message)

bot.run(TOKEN)

