import cryptocompare
import discord
from discord.ext import commands
import random
import os
import json
import praw
from keep_alive import keep_alive




client = commands.Bot(command_prefix=".")


cryptocompare.cryptocompare._set_api_key_parameter("23bd2a1120d4c12fc96639ad0f3241fdc0d1b0850e889af9cb4678b6c7856475")




hlp = ('To view live cryptocurrency prices use the "." prefix  followed by the name of the cryptocurrency you want to see for example type   ".bitcoin"   to see the live value of bitcoin The prices are only shown in USD AND EUROS you can also type ".inspiration" for Inspirational Quotes')


Inspirational_quotes = ['“Success is not final; failure is not fatal: it is the courage to continue that counts.” – Winston Churchill',
'“Play by the rules, but be ferocious.” – Phil Knight','“Business opportunities are like buses, there’s always another one coming.” – Richard Branson','“Every problem is a gift—without problems we would not grow.” – Anthony Robbins','“You only have to do a few things right in your life so long as you don’t do too many things wrong.” – Warren Buffett','“Success usually comes to those who are too busy to be looking for it.” – Henry David Thoreau','“And the day came when the risk to remain tight in a bud was more painful than the risk it took to blossom.” – Anaïs Nin','“There’s no shortage of remarkable ideas, what’s missing is the will to execute them.” – Seth Godin','“I owe my success to having listened respectfully to the very best advice, and then going away and doing the exact opposite.” – G.K. Chesterton','“I don’t know the word ‘quit.’ Either I never did, or I have abolished it.” – Susan Butcher']



btc = cryptocompare.get_price('BTC', currency=['USD','EUR'])
eth = cryptocompare.get_price('ETH', currency=['USD', 'EUR'])
dog = cryptocompare.get_price('DOGE', currency=['USD','EUR'])
itc = cryptocompare.get_price('LTC', currency=['USD','EUR'])
binance = cryptocompare.get_price('BNB', currency=['USD','EUR'])
es = cryptocompare.get_price('eos', currency=['USD','EUR'])
xp = cryptocompare.get_price('XRP', currency=['USD','EUR'])
eth_classic = cryptocompare.get_price('ETC', currency=['USD','EUR'])
crdno = cryptocompare.get_price('ADA', currency=['USD','EUR'])


Listss = cryptocompare.get_coin_list(format=True)
  

xchanges = cryptocompare.get_exchanges()

history_hour = cryptocompare.get_historical_price_hour('BTC', currency = 'USD')



@client.command()
async def history(ctx):
  await ctx.send(history_hour)


@client.command()
async def exchanges(ctx):
  await ctx.send(xchanges)

@client.command()
async def list(ctx):
  await ctx.send(Listss)

@client.command()
async def bitcoin(ctx):
    await ctx.send(btc)

@client.command()
async def etherium(ctx):
    await ctx.send(eth)

@client.command()
async def dogecoin(ctx):
    await ctx.send(dog)

@client.command()
async def litecoin(ctx):
    await ctx.send(itc)

@client.command()
async def binance_coin(ctx):
    await ctx.send(binance)

@client.command()
async def eos(ctx):
    await ctx.send(es)

@client.command()
async def xrp(ctx):
    await ctx.send(xp)

@client.command()
async def ethereum_classic(ctx):
    await ctx.send(eth_classic)

@client.command()
async def cardano(ctx):
    await ctx.send(crdno)

@client.command()
async def HELP(ctx):
  await ctx.send(hlp)

@client.command()
async def inspiration(ctx):
  await ctx.send(random.choice(Inspirational_quotes))




keep_alive()

client.run("ODQxNzU0MjQ3ODk3MTUzNTM3.YJrWuw.76sQ9ZQulo_7if6TEWhoaBA-fRw")