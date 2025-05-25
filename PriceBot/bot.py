import os
import discord
import asyncio
import aiohttp
from discord.ext import commands, tasks
from storage import load_tracked, save_tracked
from tracker import fetch_price
from config import BOT_TOKEN
from storage import load_tracked, save_tracked



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load tracked items from storage
tracked = load_tracked()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    price_check_loop.start()


@bot.command()
async def track(ctx, url: str, target: float):
    user = str(ctx.author.id)
    user_list = tracked.setdefault(user, [])
    
    user_list.append({"url": url, "target_price": target, "last_price": None})
    save_tracked(tracked)
    await ctx.send(f" Now tracking `{url}` for price ≤ ${target:.2f}")

@bot.command()
async def untrack(ctx, index: int):
    user = str(ctx.author.id)
    if user not in tracked or index < 1 or index > len(tracked[user]):
        return await ctx.send("Invalid index.")
    
    item = tracked[user].pop(index - 1)
    save_tracked(tracked)
    await ctx.send(f" Stopped tracking `{item['url']}`.")

@bot.command()
async def list(ctx):
    user = str(ctx.author.id)
    items = tracked.get(user, [])

    if not items:
        return await ctx.send("You have no tracked items.")
    
    msg = "\n".join(
        f"{i+1}. {it['url']} — target ${it['target_price']} (last: {it['last_price']})"
        for i, it in enumerate(items)
    )
    await ctx.send(f"Your tracked products:\n{msg}")

# Checks the prices every hour and a half
@tasks.loop(minutes=90)
async def price_check_loop():

    async with aiohttp.ClientSession() as session:
        for user_id, items in tracked.items():
            user = await bot.fetch_user(int(user_id))
            for it in items:
                try:
                    current = await fetch_price(session, it["url"])

                except Exception as e:
                    print("Error fetching", it["url"], e)
                    continue

                if it["last_price"] is None:
                    it["last_price"] = current
                    continue

                if current <= it["target_price"] and current < it["last_price"]:
                    await user.send(
                        f"💰 **Price Alert!***\n"
                        f"{it['url']}\n"
                        f"Current: ${current:.2f} ≤ Target: ${it['target_price']:.2f}"
                    )

                it["last_price"] = current

        save_tracked(tracked)

bot.run(BOT_TOKEN)
