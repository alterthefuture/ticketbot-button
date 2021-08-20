from discord import emoji
from discord.ext import commands
import discord
from discord_components import *
import datetime

intents=discord.Intents.all()

client = commands.Bot(command_prefix=";",intents=intents)

@client.event
async def on_ready():
    print("Bot is online.")
    DiscordComponents(client)

@client.command()
async def ticketcreate(ctx):
    embed=discord.Embed(description="To create a ticket press the button 📪",color=discord.Color.green(),timestamp=ctx.message.created_at)
    embed.set_author(name=f"General Support")
    embed.set_footer(text="Bot Made By CatNinja#0001",icon_url=client.user.avatar_url)

    await ctx.send(embed=embed,components=[
        Button(style=ButtonStyle.grey, label = "Create Ticket", emoji="📪")
    ])

    while True:
        respone = await client.wait_for("button_click")
        if respone.channel.id == ctx.channel.id:
            category_id = #category for tickets here

            for category in ctx.guild.categories:
                if category.id == category_id:
                    break

            ticket_amount = 1 if len(category.channels) == 0 else int(category.channels[-1].name.split("-")[-1]) + 1
            ticket_channel = await category.create_text_channel(f"ticket {ticket_amount}", permission_synced=True)
            await ticket_channel.set_permissions(respone.user, read_messages=True,send_messages=True)

            embed=discord.Embed(title="Ticket Opened",description=f"Support will be with you shortly, Please be patient.",color=discord.Color.green(),timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="Bot Made By CatNinja#0001",icon_url=client.user.avatar_url)
            await ticket_channel.send(f"{respone.user.mention} Welcome", embed=embed)

            await respone.respond(type=6)
            
client.run("token-here")
