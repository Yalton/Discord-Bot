#Imports discord api and commands from discord api
import discord
import random
from discord.ext import commands
from discord.utils import get

#Sets prefix to be used for commands in server EX: .echo Hello World
client = commands.Bot(command_prefix = '.')

#Bot has connected to discord and is ready
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('use .commands to see what I can do'))
    print('Bonesaw is reeeaaddy')
    channel = client.get_channel(733423232421593129)
    await channel.send('Ah it sure is nice to be alive again.')

#Bot detected a new member, sending them a message.
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.');
    ment = member.mention
    channel = client.get_channel(725551130993754192)
    await channel.send('Hello ' + ment +  'Welcome to Akuma Gaming! Most channels on the server are available to the general public but if you would like to post and use the voice channels read our rules in #akuma-policy. Come back here$

#On message function, massive
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.event
async def on_message(message):

    #lets not respond to ourselves
    if message.author == client.user:
        return

    #If Bot was mentioned in chat Send a random response from this list of responses
    if client.user.mentioned_in(message):
        print('Bot was mentioned in a message\n')
        ment = message.author.mention
        responses = ['Hello ' + ment + ' how are you?', 'Whats good ' + ment + ' lets get these dubs yeah?','Yooooo '+ ment +' 1v1 me right now.','Hey ' + ment + ' why are you talking to me? There are real people on here you know.','Gre$
        await message.channel.send(random.choice(responses))

    #Block of code to promote  users that type .readpolicy to members
    if message.content == '.readpolicy':
        print('New user attempting to get set up...\n')
        role = discord.utils.get(message.guild.roles, name="Akuma Friends")
        await message.author.add_roles(role)
        await message.channel.send('Setup process successful')

    #Command detector
    if '.' in message.content:
        print('Bot detected a command\n')
        await client.process_commands(message)
 else:
        #Ensure the bot doesent react in channels it shouldn't
        if message.channel.id is not '725658992046637136' or message.channel.id is not '725806600543273020' or message.channel.id is not '665272795583873024' or message.channel.id is not '664149931040309268' or message.channel.id is not$

            if message.attachments or 'won' in message.content or 'play' in message.content or 'down' in message.content or 'diamond' in message.content or 'plat' in message.content or 'gold' in message.content or 'promoted' in message.$
                emojis= ['<:SquidwardDab:725620558884241408>','<:ShibaSmug:725620553179988078>','<:MemeDogKek:725620554274570300>','<:ShibaShock2:725620553737568328>','<:MemePikachu:725620557961232414>','<:MemeKnuckles:72562055299530755$
                emoji = random.choice(emojis)
                await message.add_reaction(emoji)
            else:
                return
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Implements a commands to give users a list of all available commands
@client.command()
async def commands(ctx):
    await ctx.send('Acceptable commands are... \n.ping \n.coinflip \n.spongebob \n.echo MESSAGE \n.8ball QUESTION')

#Returns latency of bot and says PONG! Mostly for testing
@client.command()
async def ping(ctx):
    await ctx.send('Pong! [Bot latency ' + str((round(client.latency * 1000))) + 'ms]')

#Commands that will make the bot repeat a mesage it heard in the channel it hear it
@client.command()
async def echo(ctx,*,msg):
    await ctx.send(msg)

#Say command: Used to allow admins and mods to speak as the bot. The reality of it's existence should never be revealed to the general public
@client.command()
async def say(ctx,chnnl,*,msg):
    guild = client.get_guild(664149931040309265)
    print('Channel was ' + str(chnnl) + ' Message was ' + str(msg))
    channel = discord.utils.get(guild.channels,name=chnnl)
    await channel.send(str(msg))

#Coinflip command: Says either heads or tails in the chat the command was prompted in
@client.command()
async def coinflip(ctx):
    sides = ['heads.', 'tails.']
    await ctx.send('It is ' + random.choice(sides))

#Spongebob commands: Gives the user a random spongebob quote.
@client.command()
async def spongebob(ctx):
    quotes = ['Im ugly and Im proud!','All I know is fine dining and breathing.','Ravioli, ravioli. Give me the formuoli.','The inner machinations of my mind are an enigma.','Is mayonnaise an instrument?','Once upon a time there was an $
    await ctx.send(random.choice(quotes))

#8ball commands :Provides an answer to a yes or no question.
@client.command(aliases = ['8ball'])
async def _8ball(ctx,*,question):
    responses = ['It is certain','It is decidedly so.','Without a doubt','Yes - definitely.','You may rely on it.','As I see it,yes.','Most likely.','Outlook good.','Yes.','Signs point to yes','Reply hazy,try again.','Ask again later.',$
    await ctx.send('Question: ' + question + ' \nAnswer: ' + random.choice(responses) )

#Handling to inform the user of an error with the say command
@say.error
async def say_error(ctx,error):
    await ctx.send('This command requires two arguments. \n First the name of the channel you want to post in.\n Then a space and the message you want me to send \n EX: .say bot-test test \n ' )
#Handling to inform the user of an error with the 8ball command
@_8ball.error
async def _8ball_error(ctx,error):
    await ctx.send('Please provide me with a yes or no question.')

#Handling to inform the user of an errror with the echo command
@echo.error
async def echo_error(ctx,error):
    await ctx.send('Please provide me with a message to repeat.')

#useless command should remove soon
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

#Connects client to discord using the token
client.run('TOKEN')
