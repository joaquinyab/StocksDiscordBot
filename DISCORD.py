from email import message
from logging import exception
import os
from datetime import date
from tracemalloc import start
import requests
from tokenize import Token
import requests
from bs4 import BeautifulSoup
import discord
from dotenv import load_dotenv
from discord.ext import commands
import yfinance as yf
import datetime as dt


load_dotenv()


client = commands.Bot(command_prefix=" $ ")

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):

    start_date = "2022-2-2"
    end_date = date.today()



    stock = message.content


    #stock = message.content

    
    if stock != 0:
        ticker= yf.download(stock,start_date,end_date)['Close'][0]




        await message.channel.send(ticker)

    #except message.content == 0:

    #elif message.channel == 0:
     #   await message.channel.send("error cargandodatos de #" + stock)


client.run('TOKEN')



