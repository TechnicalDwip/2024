from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["stic_id"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
        sticker_id = message.reply_to_message.sticker.file_id
        unique_id = message.reply_to_message.sticker.file_unique_id

        text = f"**Sticker ID is :** `{sticker_id}` \n\n  **Unique ID is :** \n\n`{unique_id}`"
        btn = InlineKeyboardMarkup([[InlineKeyboardButton("Close", callback_data="cancel")]])

        await message.reply(text, quote=True, reply_markup=btn)
    else: 
        await message.reply("<b>Oops !! Not a sticker file</b>")

# Code above made by @Royaldwip. Do not remove credit.
