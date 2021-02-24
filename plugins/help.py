from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently I Only Support Single Video URL ( NO PLAYLISTS ) Send Me An URL For Downloading Audio Or Video From YouTube"
    await message.reply_text(helptxt)
