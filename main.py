#Made by Cmaeron A. Showard
#This bot checks for a string in a message and then sends a response message.

import re
import logging
import discord

logging.basicConfig(level=logging.INFO)
client= discord.Client()

@client.event
async def on_ready():
	logging.info("I AM ALIVE, MY NAME IS {0.user}".format(client))
	await client.change_presence(status =discord.Status.idle, activity = discord.Game('Ready to help you'))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	pattern_re = re.compile(r'grinding', re.IGNORECASE)
	pattern_re2 = re.compile(r'grind', re.IGNORECASE)
	if re.search(pattern_re, message.content):
		logging.info('Message recieved')
		await message.add_reaction('\U0001F44D')
		await message.channel.send("The grind doesn't stop!")

	if re.search(pattern_re2,message.content):
		logging.info('Message recived')
		await message.add_reaction('\U0001F44D')
		await message.channel.send("The grind doesn't stop!")

client.run('TOKEN')