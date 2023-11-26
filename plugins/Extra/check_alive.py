import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("tutorial", CMD))
async def check_alive(_, message):
    await message.reply_text("<b>Think You Don't Know How To Verify <a href='https://t.me/ShinchanFilterRobot'>Me</a>! \nYou Can Watch This Video 🔥\nVideo Link 🔗 - || youtu.be/tLruG2ZNqJo?si=Y9vPy6ILQzt3xVVu ||</b>")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
