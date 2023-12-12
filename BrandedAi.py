from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import os
import re


API_ID = os.environ.get("API_ID", "25646144") 
API_HASH = os.environ.get("API_HASH", "12f189832cff086ac98413c547fbab5c") 
SESSION_NAME = os.environ.get("SESSION_NAME", "BQBHfDSQVw1mOmAS1pEz-xkI3rfXCyEeUycvE_-uHcg-fWzL90UEJ4kOaYvcind4lhi06X_OZrWrJdnb00rjZk3Z8aQdtrm_K4yF5b1pbA7CZqdDziYuclpQLLuSeOo0jnk0VQCm5UN8aNowUfku433J1a43quBer07RIUM73WlU2355avRCrzlFHewWMLeoaSkC3GqF2lQ3BaJqOSp-DlyqLfW4qkj-QrL21JexPZryUSYVPiM4DAGCnJpJ3n1xEr1Gc2UzGVLb6pb4hPWR5WgrpKmE6zn3jV03nk1T2QbYaB76N6CUiRuw-XUQzi4JAD-Ukfu9d4NftvM-XjJkORAAAAAZzCS4kA")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://bikashxd:bgtop@cluster0.gh1hqe3.mongodb.net/?retryWrites=true&w=majority")
") 


client = Client(SESSION_NAME, API_ID, API_HASH)


@client.on_message(
    filters.command("repo", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.delete()
    Aloneai = await message.reply("🤭🤏✌️")
    await asyncio.sleep(1)
    await Branded.edit("**ʙᴏʜᴀᴛ ᴛᴀɪᴊ ʜᴏ ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ**")
    await asyncio.sleep(1)
    await Branded.edit("**ɪ ᴀᴍ ᴅᴏɪɴɢ ᴍʏ ʟᴏᴠᴇ 💕**")
    await Branded.delete()
    await asyncio.sleep(2)
    umm = await message.reply_sticker("")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://telegra.ph/file/64e4440d641998b4d9749.jpg",
        caption=f"""━━━━━━━━━━━━━━━━━━━━━━━━
👻 A ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ
ᴏғ ♻️ ᴋɪɴɢ ♥️
━━━━━━━━━━━━━━━━━
ᴅᴀᴛᴀʙᴀsᴇ ʙᴀᴄᴋᴇɴᴅ ʙᴏᴛ ғᴏʀ ᴛɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴇʀ [ᴋɪɴɢ](https://t.me/l_MR_ll_KING_l
┗━━━━━━━━━━━━━━━━━┛
🥵
IF HAVE ANY QUESTION THEN CONTACT » TO » MY » [OWNER] @l_MR_ll_KING_l""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🖤 OWNER 🖤", url=f"https://t.me/l_MR_ll_KING_l")]]
        ),
    ) 


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**KING IS ALIVE**")
    
    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Aloneai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       Brandeddb = MongoClient(MONGO_URL)
       Branded = Brandeddb["BrandedDb"]["Branded"] 
       is_Branded = Branded.find_one({"chat_id": message.chat.id})
       if not is_Branded:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       Brandeddb = MongoClient(MONGO_URL)
       Branded = Brandeddb["BrandedDb"]["Branded"] 
       is_Branded = Branded.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_Branded:                   
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Brandedstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       Brandeddb = MongoClient(MONGO_URL)
       Branded = Brandeddb["BrandedDb"]["Branded"] 
       is_Branded = Branded.find_one({"chat_id": message.chat.id})
       if not is_Branded:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       Brandeddb = MongoClient(MONGO_URL)
       Branded = Brandeddb["BrandedDb"]["Branded"] 
       is_Alone = Alone.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_Branded:                    
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Brandedprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Brandedprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
               

client.run()
