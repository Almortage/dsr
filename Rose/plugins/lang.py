###################################
####    From  Yukki Music Bot  ####
###################################

from lang import get_string
from Rose.mongo.language import *
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message
from Rose.utils.lang import *
from lang import get_command
from Rose.utils.custom_filters import admin_filter
from button import *

LANG = get_command("LANG")

keyboard = InlineKeyboardMarkup(
    [[
            InlineKeyboardButton(
                text="🇪🇬 عربي", callback_data="languages_en"
            ),
        ], 
        [
            InlineKeyboardButton(
                text="🇱🇰 සිංහල", callback_data="languages_si"
            ), 
            InlineKeyboardButton(
                text="🇮🇳 हिन्दी", callback_data="languages_hi"
            )
        ], 
        [
            InlineKeyboardButton(
                text="🇮🇹 Italiano", callback_data="languages_it"
            ), 
            InlineKeyboardButton(
                text="🇮🇳 తెలుగు", callback_data="languages_ta"
            ), 
        ], 
        [
            InlineKeyboardButton(
                text="🇮🇩 Indonesia", callback_data="languages_id"
            ), 
            InlineKeyboardButton(
                text="🇲🇾 English", callback_data="languages_ar"
            ),
        ], 
        [
            InlineKeyboardButton(
                text="🇮🇳 മലയാളം", callback_data="languages_ml"
            ), 
            InlineKeyboardButton(
                text="🇲🇼 Chichewa", callback_data="languages_ny"
            ), 
        ], 
        [
            InlineKeyboardButton(
                text="🇩🇪 German", callback_data="languages_ge"
            ), 
            InlineKeyboardButton(
                text="🇷🇺 Russian", callback_data="languages_ru"
            ), 
        ]]
)


@app.on_message(filters.command(LANG) & admin_filter)
@language
async def langs_command(client, message: Message, _):
    userid = message.from_user.id if message.from_user else None
    chat_type = message.chat.type
    user = message.from_user.mention
    lang = await get_lang(message.chat.id)
    if chat_type == "private":
      await message.reply_text("Choose Your languages\nඔබේ භාෂා තෝරන්න".format(lang),
        reply_markup=keyboard,
     )
    elif chat_type in ["group", "supergroup"]:
        lang = await get_lang(message.chat.id)
        group_id = message.chat.id
        st = await app.get_chat_member(group_id, userid)
        if (
                st.status != "administrator"
                and st.status != "creator"
        ):
         return 
        try:   
            await message.reply_text( "Choose Your languages\nඔබේ භාෂා තෝරන්න".format(user),
        reply_markup=keyboard,
     )
        except Exception as e:
            return await app.send_message(LOG_GROUP_ID,text= f"{e}")


@app.on_callback_query(filters.regex("languages"))
async def language_markup(_, CallbackQuery):
    langauge = (CallbackQuery.data).split("_")[1]
    user = CallbackQuery.from_user.mention
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer("⛔️ You're already on same language")
    await set_lang(CallbackQuery.message.chat.id, langauge)
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer("✅ Successfully changed your language.")
    except:
        return await CallbackQuery.answer(
            "This language is Under Construction 👷")
    await set_lang(CallbackQuery.message.chat.id, langauge)
    return await CallbackQuery.message.delete()

__MODULE__ = f"{Languages}"
__HELP__ = """
يمكنك تغير لغه الروبوت علي حسب
اللغه التي تناسب مجموعتك 
**امر الادمن:**
- اللغه او /lang  : اختر لغتك الان من خلال الضغط علي الازرار.
"""
__helpbtns__ = (
    [
        [
            InlineKeyboardButton(
                text="🇪🇬 عربي", callback_data="languages_en"
            ),
       ], 
       [
            InlineKeyboardButton(
                text="🇱🇰 සිංහල", callback_data="languages_si"
            ), 
            InlineKeyboardButton(
                text="🇮🇳 हिन्दी", callback_data="languages_hi"
            )
       ], 
       [
            InlineKeyboardButton(
                text="🇮🇹 Italiano", callback_data="languages_it"
            ), 
            InlineKeyboardButton(
                text="🇮🇳 తెలుగు", callback_data="languages_ta"
            )
       ], 
       [
            InlineKeyboardButton(
                text="🇮🇩 Indonesia", callback_data="languages_id"
            ),
            InlineKeyboardButton(
                text="🇲🇾 English", callback_data="languages_ar"
            ),
       ], 
       [
            InlineKeyboardButton(
                text="🇮🇳 മലയാളം", callback_data="languages_ml"
            ), 
            InlineKeyboardButton(
                text="🇲🇼 Chichewa", callback_data="languages_ny"
            ), 
       ], 
       [
            InlineKeyboardButton(
                text="🇩🇪 German", callback_data="languages_ge"
            ), 
            InlineKeyboardButton(
                text="🇷🇺 Russian", callback_data="languages_ru"
            ), 
        ], 
    ]
)
