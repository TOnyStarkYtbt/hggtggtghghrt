import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

app = Client("my_account")

START_TEXT = """
Hello {}, I am a photo background remover bot. Send me a photo I will send the photo without background.
Made by @HTechMedia
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/HTechMedia'),
        InlineKeyboardButton('Support', url='https://telegram.me/HTechMediaSupport')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )


@app.on_message(filters.private)
async def hello(client, message):
        await update.message.edit_text(
            text=START_TEXT.format{message.from_user.mention}")
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
            )

app.run()
