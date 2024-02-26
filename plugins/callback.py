"""JishuDeveloper"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram import Client , filters
from script import *
from config import *



@Client.on_callback_query(filters.regex('about'))
async def about(bot,update):
    text = script.ABOUT_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "home")]
                  ])
    await update.message.edit(text = text,reply_markup = keybord)


@Client.on_message(filters.private & filters.command(["donate"]))
async def donatecm(bot,message):
	text = script.DONATE_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("🦋 Admin",url = "https://t.me/CallAdminRobot"), 
        			InlineKeyboardButton("✖️ Close",callback_data = "cancel") ]])
	await message.reply_text(text = text,reply_markup = keybord)

@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["admin"]))
async def admincm(bot,message):
	text = script.ADMIN_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("✖️ Close ✖️",callback_data = "cancel") ]])
	await message.reply_text(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('help'))
async def help(bot,update):
    text = script.HELP_TXT.format(update.from_user.mention)
    keybord = InlineKeyboardMarkup([ 
                    [InlineKeyboardButton('🏞 Thumbnail', callback_data='thumbnail'),
                    InlineKeyboardButton('✏ Caption', callback_data='caption')],
                    [InlineKeyboardButton('🏠 Home', callback_data='home')]
                   ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('thumbnail'))
async def thumbnail(bot,update):
    text = script.THUMBNAIL_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('caption'))
async def caption(bot,update):
    text = script.CAPTION_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('donate'))
async def donate(bot,update):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)


@Client.on_callback_query(filters.regex('home'))
async def home_callback_handler(bot, query):
    text = f"""Hey {query.from_user.mention} <b>
➻ Tʜɪꜱ Iꜱ Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.⚡️
➻ Uꜱɪɴɢ Tʜɪꜱ Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ Aɴᴅ Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oғ Yᴏᴜʀ Fɪʟᴇꜱ.🖼
➻ Yᴏᴜ Cᴀɴ Aʟꜱᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ Aɴᴅ Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ.📁»🎬
➻ Tʜɪꜱ Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛꜱ Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜꜱᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.⚙️ 
</b>"""
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("⚙ Help", callback_data='help'),
		     InlineKeyboardButton("⚔ About", callback_data='about')]
		  ])
    await query.message.edit_text(text=text, reply_markup=keybord)






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
