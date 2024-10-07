import discord
from discord.ext import commands
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Mengakses API
load_dotenv()
API         = os.getenv('API')
BotDiscord  = os.getenv('BotToken')


# Konfigurasi Gemini API
genai.configure(api_key= API )
model = genai.GenerativeModel('gemini-pro')

# Konfigurasi bot Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) #bisa di isi(command_prefix='!') atau tidak (command_prefix='')

@bot.event
async def on_ready():
    print(f'{bot.user} telah berhasil login!')

@bot.command(name="tanya")                              #bila bot di isi(!p) atau tidak(p)
async def tanya(ctx, *, pertanyaan):
    try:
        response = model.generate_content(pertanyaan)
        await ctx.send(response.text)
    except Exception as e:
        await ctx.send(f"Maaf, terjadi kesalahan: {str(e)}")

# Jalankan bot
bot.run(BotDiscord)
