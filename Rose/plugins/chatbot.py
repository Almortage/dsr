import requests
from pyrogram import filters
from googletrans import Translator
from Rose import *
from Rose.utils.filter_groups import *
from lang import get_command
from Rose.utils.lang import *
from Rose.utils.custom_filters import *
from Rose.utils.commands import *
from Rose import *
from Rose.mongo import chatb
from Rose.plugins.antlangs import get_arg
from Rose.utils.custom_filters import admin_filter
from button import *

tr = Translator()
CBOT = get_command("CBOT")
CBOTA = get_command("CBOTA")


@app.on_message(
    command("فعيل الردود")
    & ~filters.edited
    & ~filters.private
    & admin_filter
)
@language
async def cbots(client, message: Message, _):
    group_id = str(message.chat.id)
    chat_id = message.chat.id
    user_id = message.from_user.id
    user = await bot.get_chat_member(group_id, user_id)
    if not user.status == "creator" or user.status == "administrator":
        return
    if len(message.command) < 2:
        return await message.reply_text(_["chatb1"])
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    args = get_arg(message)
    sex = await message.reply_text(_["antil2"])
    lower_args = args.lower()
    if lower_args == "فتح":
        chatb.insert_one({f"chatbot": group_id})#default AI is Afflicate+
    elif lower_args == "قفل":
        chatb.delete_one({f"chatbot": group_id})
    else:
        return await sex.edit(_["chatb1"])
    await sex.edit(f"◍ تم تفعيل ردود البوت `{'Enabled' if lower_args=='on' else 'Disabled'}` بنجاح \n√")

@app.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.private
    & ~filters.edited,
    group=cbot)
async def szcbot(_, message: Message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        return
    if not message.reply_to_message.from_user:
        return
    if message.reply_to_message.from_user.id != BOT_ID:
        return
    if message.text[0] == "/":
        return
    chat = chatb.find_one({"chatbot":chat_id})   
    if chat:
        await app.send_chat_action(message.chat.id, "typing")
        try:
           lang = tr.translate(message.text).src
           trtoen = (message.text if lang=="en" else tr.translate(message.text, dest="en").text).replace(" ", "%20")
           text = trtoen.replace(" ", "%20") if len(message.text) < 2 else trtoen
           affiliateplus = requests.get(f"https://api.affiliateplus.xyz/api/chatbot?message={text}&botname=Rose&ownername=@supunma&user={chat_id}")
           textmsg = (affiliateplus.json()["message"])
           if "Affiliate+" in textmsg:
               textmsg = textmsg.replace("Affiliate+", "Rose")
           if "Lebyy_Dev" in textmsg:
               textmsg = textmsg.replace("Lebyy_Dev", "Supun Maduranga")
           if "God Brando" in textmsg:
               textmsg = textmsg.replace("God Brando", f"{message.from_user.first_name}")
           if "seeker" in textmsg:
               textmsg = textmsg.replace("seeker", f"wow")
           msg = tr.translate(textmsg, src='en', dest=lang)
           await message.reply_text(msg.text)
        except Exception:
           user_id = message.from_user.id
           lang = tr.translate(message.text).src
           trtoen = (message.text if lang=="en" else tr.translate(message.text, dest="en").text).replace(" ", "%20")
           text = trtoen.replace(" ", "%20") if len(message.text) < 2 else trtoen
           safeone = requests.get(f"https://api.safone.tech/chatbot?message={text}&bot_name=Rose&bot_master=Supun&user_id={user_id}")
           textmsg = (safeone.json()["answer"])
           if "Affiliate+" in textmsg:
               textmsg = textmsg.replace("Affiliate+", "Rose")
           if "[Safone]" in textmsg:
               textmsg = textmsg.replace("[Safone]", "Supun Maduranga")
           msg = tr.translate(textmsg, src='en', dest=lang)
           await message.reply_text(msg.text)







