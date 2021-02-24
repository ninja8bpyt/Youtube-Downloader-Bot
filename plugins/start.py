from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("👉SUBSCRIBE ME ON YT👈", url="https://www.youtube.com/channel/UCcCtEDm4GLiW8880HSU2f_Q?view_as=subscriber")],
        [InlineKeyboardButton(
            "👉Report Bugs👈", url="https://t.me/mr_ninjas_bot")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n Send Me An YouTube Video URL or /help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
