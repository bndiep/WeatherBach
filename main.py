# import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
# allows HTTP requests from an API
import requests
# makes it easier to work with data that is returned
import json

keep_alive()
bot_token = os.environ['DISCORD_BOT_SECRET']
weather_api = os.environ['OPENWEATHER_API']

# provide a prefix for users to call
bot = commands.Bot(command_prefix='!')

def get_weather(zipcode: int):
  # make a 'GET' request that takes an arg of the URL we want to make a request to
  response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={weather_api}&units=imperial')

  json_data = json.loads(response.text)

  weather_description = json_data['weather'][0]['description']
  weather_temp = json_data['main']['temp']

  weather_report = f'I see {weather_description}. It is currently {weather_temp}ºF!'

  return(weather_report)

@bot.event
async def on_ready():
  print("I'm in")
  print(bot.user)

@bot.event
async def on_message(message):
  # prevents bot from responding to self in an endless loop
  # if message.author == bot.user:
  #   return
  await bot.process_commands(message)

# help command? help='Responds with the current weather given the user\'s zipcode'
@bot.command()
# function is named whatever the command is
async def weather(ctx, zipcode: int):
  weather_report = get_weather(zipcode)
  await ctx.send(weather_report)

@bot.command(name='testing')
async def call_test(ctx):
  await ctx.send('1, 2, 3!')

bot.run(bot_token)
# check status code to see if request was successful
# print(response.json())