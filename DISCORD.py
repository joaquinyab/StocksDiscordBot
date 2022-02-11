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


bot = commands.Bot(command_prefix="!")




client = discord.Client()




@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')




@client.event
async def on_message(message):

    start_date = "2022-2-2"
    end_date = date.today()

    stock = message.content
    cryptoInfo = message.content

    if stock != 0 and stock.startswith("!"):

        stockOut = stock[1:]

        ticker = yf.download(stockOut, start_date, end_date)['Close'][0]
        

        await message.channel.send(ticker )


    elif cryptoInfo != 0 and cryptoInfo.startswith("$"):

        CryptoInfoOut = cryptoInfo[1:]

        await message.channel.send("https://"+CryptoInfoOut+".org")


client.run('TOKEN')



