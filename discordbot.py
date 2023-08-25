import discord
from discord.ext import commands

intents = discord.Intents.default()  
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)

banned_words = ["씨발", "tlqkf", "시발", "ㅂㅅ", "느금마" ,"느그애비" ,"ㄴㄱㅁ","섹스","ㅅㅅ","망겜","병신","장애","새끼","ㅈ","ㅄ","ㅈㄹ","지랄","ㅅㅂ","부모님","엄마","아빠","걸레","걸래","쌍년","시바","새꺄","개새끼","개생키","뒤짐","염병","븅신","정액","보지","새1끼","새1끼","ㅆ","자지","옘병","꼬추","torl","Tlqkf","느그","털림","년","븅딱","박아","헤응","넣어","게이","레즈","ㅗ","_ㅣ_","_","ㅅ","ㅂ1ㅅ","병1신","ㅅ1ㅂ","시1발"]

@bot.event
async def on_ready(): 
    print("아아아아\n아아아아")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(검열))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content_lower = message.content.lower()
    if any(word in content_lower for word in banned_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, 욕설이 감지되어 메시지가 삭제되었습니다.")

    await bot.process_commands(message)

bot_token = "MTE0NDU4MjIyNDg0MzM5MTA5Ng.G0UtVt.XU0pP9VrzBXwCCqafqfWfLOkNknUHxO2LOHm5o"
bot.run(bot_token)
