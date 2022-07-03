from pymongo import MongoClient
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from Katherine import telethn as tbot, OWNER_ID, DEV_USERS
from Katherine import MONGO_DB_URI, BOT_ID, EVENT_LOGS as GBAN_LOGS
from Katherine.utils.pluginhelper import is_admin
from Katherine.events import register
from Katherine.modules.sql.users_sql import get_all_chats
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["kingxlbot"]

gmuted = db.gmute #RoseloverX

GBAN_LOGS = int(GBAN_LOGS)

@register(pattern="^/gmute ?(.*)")
async def gban(event):
 sender = event.sender.first_name
 group = event.chat.title
 if event.fwd_from:
        return
 if event.sender_id == OWNER_ID:
  pass
 elif event.sender_id in DEV_USERS:
  pass 
 else:
  return
 input = event.pattern_match.group(1)
 if input:
   arg = input.split(" ", 1)
 if not event.reply_to_msg_id:
  if len(arg) == 2:
    iid = arg[0]
    reason = arg[1]
  else:
    iid = arg[0]
    reason = "None"
  if not iid.isnumeric():
   username = iid.replace("@", "")
   entity = await tbot.get_input_entity(iid)
   try:
     r_sender_id = entity.user_id
   except Exception:
        await event.reply("Couldn't fetch that user.")
        return
  else:
   r_sender_id = int(iid)
  try:
   replied_user = await tbot(GetFullUserRequest(r_sender_id))
   fname = replied_user.user.first_name
  except Exception:
   fname = "User"
 else:
   reply_message = await event.get_reply_message()
   iid = reply_message.sender_id
   username = reply_message.sender.username
   fname = reply_message.sender.first_name
   if input:
     reason = input
   else:
     reason = "None"
   r_sender_id = iid
 if r_sender_id == OWNER_ID:
        await event.reply(f"Char Chavanni godhe pe\ngey Mere Lode Pe!.")
        return
 elif r_sender_id in DEV_USERS:
        await event.reply("This Person is a Dev, Sorry!")
        return
 elif r_sender_id == BOT_ID:
        await event.reply("Another one bits the dust! banned a betichod!")
        return
 chats = gmuted.find({})
 for c in chats:
      if r_sender_id == c["user"]:
          to_check = get_reason(id=r_sender_id)
          gmuted.update_one(
                {
                    "_id": to_check["_id"],
                    "bannerid": to_check["bannerid"],
                    "user": to_check["user"],
                    "reason": to_check["reason"],
                },
                {"$set": {"reason": reason, "bannerid": event.sender_id}},
            )
          await event.reply(
                "This user is already gmuted, I am updating the reason of the gmute with your reason.\n kitni bar ma  chodega iski 😂"
            )
          await tbot.send_message(GBAN_LOGS, "**Global Mute**\n#UPDATE\n**ID:** `{}`".format(r_sender_id))

 gmuted.insert_one(
        {"bannerid": event.sender_id, "user": r_sender_id, "reason": reason}
    )
 await tbot.send_message(GBAN_LOGS, "**Global Mute**\n**Sudo Admin:** {}\n**User:** {}\n**ID:** `{}`".format(sender, fname, r_sender_id))
 await event.reply("Sucessfully Added user to Gmute List!")
 
@register(pattern="^/ungmute ?(.*)")
async def ugban(event):
 sender = event.sender.first_name
 group = event.chat.title
 id = event.sender_id
 if event.fwd_from:
        return
 if event.sender_id == OWNER_ID:
  pass
 elif event.sender_id in DEV_USERS:
  pass
 else:
  return
 input = event.pattern_match.group(1)
 if input:
   arg = input.split(" ", 1)
 if not event.reply_to_msg_id:
  if len(arg) == 2:
    iid = arg[0]
    reason = arg[1]
  else:
    iid = arg[0]
    reason = None
  if not iid.isnumeric():
   username = iid.replace("@", "")
   entity = await tbot.get_input_entity(iid)
   try:
     r_sender_id = entity.user_id
   except Exception:
        await event.reply("Couldn't fetch that user.")
        return
  else:
   r_sender_id = int(iid)
  try:
   replied_user = await tbot(GetFullUserRequest(r_sender_id))
   fname = replied_user.user.first_name
  except Exception:
   fname = "User"
 else:
   reply_message = await event.get_reply_message()
   iid = reply_message.sender_id
   username = reply_message.sender.username
   fname = reply_message.sender.first_name
   if input:
     reason = input
   else:
     reason = None
   r_sender_id = iid
 if r_sender_id == OWNER_ID:
        await event.reply(f"Yeah FuckOff!")
        return
 elif r_sender_id in DEV_USERS:
        await event.reply("No!")
        return
 elif r_sender_id == BOT_ID:
        await event.reply("Who Dafaq Made You Sudo?!")
        return
 chats = gmuted.find({})
 for c in chats:
        if r_sender_id == c["user"]:            
            gmuted.delete_one({"user": r_sender_id})
            await event.reply("Globally Pardoned This User.!🏳️")
            await tbot.send_message(GBAN_LOGS, "**Global Unmute**\n**ID:** `{}`".format(
                                   r_sender_id))
            return
 await event.reply("Yeah that user is not in my Gmute list.!?")


              
@tbot.on(events.NewMessage(pattern=None))
async def gmute(event):
    chats = gmuted.find({})
    for c in chats:
        if event.sender_id == c["user"]: 
            await event.delete()
