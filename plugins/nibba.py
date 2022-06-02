from modules.database.dbqueue import remove_active_chat


@Client.on_message(
    command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & other_filters
)
@check_blacklist()
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = (await c.get_chat(chat_id)).invite_link
        if not invitelink:
            await c.export_chat_invite_link(chat_id)
            invitelink = (await c.get_chat(chat_id)).invite_link
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
        await user.join_chat(invitelink)
        await remove_active_chat(chat_id)
        return await user.send_message(chat_id, "✅ ᴜsᴇʀʙᴏᴛ ᴊᴏɪɴᴇᴅ ᴄʜᴀᴛ")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "✅ ᴜsᴇʀʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ɪɴ ᴄʜᴀᴛ")