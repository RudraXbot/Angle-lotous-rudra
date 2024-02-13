from pyrogram.types import InlineKeyboardButton

import config
from BrandrdXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝔸𝒹𝒹 𝕄ℯ 𝔹ℯ𝒷"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["ɢʀᴏᴜᴘ"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝔸𝒹𝒹 𝕄𝓮𝓮 𝔹ℯ𝒷"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["ʜᴇʟᴘ"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["ᴍᴀᴀʟɪᴋ"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["ɢʀᴏᴜᴘ"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["ᴇʙʜɪ ᴡᴏʜɪ sᴀᴍᴇ ɢʀᴏᴜᴘ"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["ᴊᴀᴀ sᴏʀᴄᴇ ᴍɪʟᴇɢᴀ ᴊᴀᴀ"], callback_data="gib_source")
        ],
    ]
    return buttons
