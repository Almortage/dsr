from pyrogram.types import Message
from Rose import *
from Rose.mongo.rulesdb import Rules



async def get_private_rules(_, m: Message, help_option: str):
    chat_id = int(help_option.split("_")[1])
    rules = Rules(chat_id).get_rules()
    if not rules:
        await m.reply_text(
            "◍ لم يضع ادمن الجروب اي قواعد هنا\n√",
            quote=True,
        )
        return ""
    await m.reply_text(
        f"""
**القواعد**:

{rules}
""",
        quote=True,
        disable_web_page_preview=True,
    )
    return ""

async def get_learn(_, m: Message, help_option: str):
    await m.reply_text(
        f"""
الطريقة الأخرى لاستخدامي هي كتابة الاستعلام المضمّن بنفسك
يجب أن يكون التنسيق بهذا الترتيب

`@XxvprxX your whisper @username`

الآن سأقسم التنسيق إلى 3 أجزاء وأشرح كل جزء منه

1- `@XxvprxX`
هذا هو اسم المستخدم الخاص بي ، يجب أن يكون في بداية الاستعلام المضمّن حتى أعلم أنك تستخدمني وليس روبوتًا آخر.

2- `رسالة الهمس`
انه الهمس الذي سيتم إرساله إلى المستخدم المستهدف ، فأنت بحاجة إلى إزالة الهمس وإدخال الهمس الفعلي.

3- `@username`
يجب استبدال هذا باسم مستخدم الهدف حتى يعرف الروبوت أن المستخدم الذي يحمل اسم المستخدم هذا يمكنه رؤية رسالة الهمس الخاصة بك.

مثال:-
`UUOF0 مرحبًا ، هذا اختبار @XxvprxX`

📎 يعمل الروبوت في مجموعات ويجب أن يكون المستخدم المستهدف معك في نفس المجموعة
ما كنت تنتظر؟!
جربني الآن 😉
""",
        quote=True,
        disable_web_page_preview=True,
    )
    return ""


