
import discord
import random
import time
from discord.ext import commands

roles=["top","support","adc","jungla","mid"]
nombres=["Adrian","Cinthy","Dany","Nico","Lu"]
random.shuffle(nombres)
random.shuffle(roles)



token= "NzI3Njc4OTI4MjczMTQ1OTI4.Xvvouw.dQQXDCSr8U1q9-6UicQZMcA7SiU"

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
@bot.command(name='roll')
async def Roll(ctx):
    for x in range(0,5):
             time.sleep(1.5)
             rol=roles[x]+"="+ nombres[x]
             await ctx.send(rol)
    
    


bot.run(token)