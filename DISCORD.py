from email import message
from logging import exception
import os
from datetime import date
from tracemalloc import start
from click import pass_context
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


bot = commands.Bot(command_prefix=".")


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
    ayuda = message.content

    if stock != 0 and stock.startswith("!"):

        stockOut = stock[1:]

        ticker = yf.download(stockOut, start_date, end_date)['Close'][0]
        

        await message.channel.send(ticker )


    elif cryptoInfo != 0 and cryptoInfo.startswith("$"):

        CryptoInfoOut = cryptoInfo[1:]

        await message.channel.send("https://"+CryptoInfoOut+".org")

    elif ayuda == "help":
        await message.channel.send("-----------------------------------🤖 𝐇𝐈 𝐌𝐘 𝐍𝐀𝐌𝐄 𝐈𝐒 𝐒𝐓𝐎𝐂𝐊𝐒𝐁𝐎𝐓 🤖------------------------------------\n\n ɪ ᴡɪʟʟ ꜱʜᴏᴡ ʏᴏᴜ ᴀʟʟ ᴍʏ ꜰᴜɴᴄᴛɪᴏɴᴀʟɪᴛɪᴇꜱ... \n\n【$】: 𝚠𝚛𝚒𝚝𝚒𝚗𝚐 $ + 𝚊𝚗𝚢 𝚌𝚛𝚢𝚙𝚝𝚘 𝚗𝚊𝚖𝚎 𝚒 𝚠𝚒𝚕𝚕 𝚊𝚞𝚝𝚘𝚖𝚊𝚝𝚒𝚌𝚊𝚕𝚕𝚢 𝚜𝚎𝚗𝚍 𝚢𝚘𝚞 𝚝𝚑𝚎 𝚘𝚏𝚒𝚌𝚒𝚊𝚕 𝚙𝚊𝚐𝚎 𝚘𝚏 𝚝𝚑𝚊𝚝 𝚌𝚛𝚢𝚙𝚝𝚘𝚌𝚞𝚛𝚛𝚎𝚗𝚌𝚢 𝚜𝚘 𝚢𝚘𝚞 𝚌𝚊𝚗 𝚕𝚎𝚊𝚛𝚗 𝚊𝚋𝚘𝚞𝚝 𝚒𝚝 \n\n【!】: 𝚠𝚛𝚒𝚝𝚒𝚗𝚐 ! + 𝚊𝚗𝚢 𝚜𝚝𝚘𝚌𝚔 𝚗𝚊𝚖𝚎 𝚠𝚒𝚕𝚕 𝚜𝚑𝚘𝚠 𝚢𝚘𝚞 𝚝𝚑𝚎 𝚌𝚞𝚛𝚛𝚎𝚗𝚝 𝚙𝚛𝚒𝚌𝚎 𝚘𝚏 𝚒𝚝 🤑")


client.run('TOKEN')



