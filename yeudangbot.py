#setup
import discord
import os
from discord.ext import commands ,tasks
from itertools import cycle
print("Loading...")
yeudangbot = commands.Bot(command_prefix = '.')
yeudangbot.remove_command('help')
players = {}
status = cycle(['Bot này được tạo', 'bởi Creeper Mc'])
#kho event của bot
@yeudangbot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('Bạn đã nhập sai hoặn lệnh này không tồn tại')
#bot đã dc bật
@yeudangbot.event
async def on_ready():
	await yeudangbot.change_presence(status=discord.Status.online, activity=discord.Game('Bot được tạo bởi Creeper Mc'))
	change_status.start()
	print("Bot Yêu Đảng is ready")
#commands
@yeudangbot.command()
async def ping(ctx):
	await ctx.send(f'Ping = {round(yeudangbot.latency * 1000)}ms')

@yeudangbot.command()
async def cre(ctx):
	await ctx.send(f'Người đã tạo ra tôi là Creeper Mc#6177')
	await ctx.send(f'Con Bot này đã tiêu tốn của Creeper Mc 6 tiếng 12 phút lập trình liên tục')

@yeudangbot.command()
async def cute(ctx):
	await ctx.send(f'aww,bạn khen tôi cute kìa,ngại quá')
	await ctx.send(f'https://tenor.com/view/i-love-you-heart-love-gif-8891095')

@yeudangbot.command()
async def ver(ctx):
	await ctx.send(f'Yêu Đảng Bot v1.0')

@yeudangbot.command()
async def fack(ctx):
	await ctx.send(f':smiling_face_with_tear:')

@yeudangbot.command()
async def help(ctx):
	await ctx.send(f'.ping:xem chỉ số ping/ms')
	await ctx.send(f'.cre:Xem người đã tạo ra tôi')
	await ctx.send(f'.cute:để khen con bot cute')
	await ctx.send(f'.ver:để xem phiên bản')
	await ctx.send(f'.cls [số lượng]:xóa tin nhắn')
	await ctx.send(f'.fack:để chửi nó')
	await ctx.send(f'.help:để mở bảng này')
#clear
@yeudangbot.command()
async def cls(ctx, amout=1):
	await ctx.channel.purge(limit=amout)
#sprite
def onlyowner(ctx):
	return ctx.author.id == 482471247028944896	
@yeudangbot.command()
@commands.check(onlyowner)
async def kick(ctx, member : discord.Member, *, reason=None):
	await ctx.send(f'Đã đuổi {member.mention}')
	await member.kick(reason=reason)
@yeudangbot.command()
@commands.check(onlyowner)
async def ban(ctx, member : discord.Member, *, reason=None):
	await ctx.send(f'Đã chặn {member.mention}')
	await member.ban(reason=reason)
#BG tasks
@tasks.loop(seconds=5)
async def change_status():
	await yeudangbot.change_presence(activity=discord.Game(next(status)))
#dòng dưới là để chạy bot
yeudangbot.run('ODA3NTIyNjgxNDI3NTkxMTY4.YB5OGg.O3Co6Eur0IxQx4orDve3-v5U3Vw')
