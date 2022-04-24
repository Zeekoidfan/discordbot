import discord
import os
import random
import json
import pickle
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer

intents = json.loads(open('intents.json').read())
words = []
classes = []
documents = []
ignore = ['?', '!', '.', ',']

for intent in intents['General']:
    for pattern in intent['patterns']:
        world_list = nltk.word_tokenize(pattern)
        words.append(world_list)
        documents.append((world_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(documents)

client = discord.Client()


@client.event
async def on_ready():
    print('awjnjkawfjaw'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!BOB'):
        await message.channel.send('Hellowworld')


client.run(os.getenv('DiscordToken'))
