from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from Katherine.__main__ import *


# Buttons Function for admin module


def alicia_admin_callback(update, context):
    query = update.callback_query
    if query.data == "aliciaadmin_":
        query.message.edit_text(
            text=""" Admins only*:*
  ❍ /pin*:* silently pins the message replied to - add `'loud'` or `'notify'` to give notifs to users
  ❍ /unpin*:* unpins the currently pinned message
  ❍ /invitelink*:* gets invitelink
  ❍ /setgtitle <newtitle>*:* Sets new chat title in your group.
  ❍ /setgpic*:* As a reply to file or photo to set group profile pic!
  ❍ /delgpic*:* Same as above but to remove group profile pic.
  ❍ /setsticker*:* As a reply to some sticker to set it as group sticker set!
  ❍ /setdescription <description>*:* Sets new chat description in group.
  ❍ /antispam <on/off/yes/no>*:* Will toggle our antispam tech or return your current settings.
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(Chodu)")
                 ]
                ]
            ),
        )


def alicia_admin_ban_callback(update, context):
    query = update.callback_query
    if query.data == "aliciaadminban_":
        query.message.edit_text(
            text=""" Admins only*:*
  ❍ /ban <userhandle>*:* bans a user. (via handle, or reply)
  ❍ /sban <userhandle>*:* Silently ban a user. Deletes command, Replied message and doesn't reply. (via handle, or reply)
  ❍ /tban <userhandle> x(m/h/d)*:* bans a user for `x` time. (via handle, or reply). `m` = `minutes`, `h` = `hours`, `d` = `days`.
  ❍ /unban <userhandle>*:* unbans a user. (via handle, or reply)
  ❍ /punch <userhandle>*:* Punches a user out of the group, (via handle, or reply)  """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(Chodu)")
                 ]
                ]
            ),
        )


def alicia_admin_purge_callback(update, context):
    query = update.callback_query
    if query.data == "aliciaadminpurge_":
        query.message.edit_text(
            text=""" Admins only*:*
  ❍ /del*:* deletes the message you replied to
  ❍ /purge*:* deletes all messages between this and the replied to message.
  ❍ /purge <integer X>*:* deletes the replied message, and X messages following it if replied to a message.
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(Chodu)")
                 ]
                ]
            ),
        )



def alicia_admin_promote_callback(update, context):
    query = update.callback_query
    if query.data == "aliciaadminpromote_":
        query.message.edit_text(
            text=""" Admins only*:*
  ❍ /promote*:* promotes the user
  ❍ /demote*:* demotes the user
  ❍ /title <title here>*:* sets a custom title for an admin that the bot promoted
  ❍ /admincache*:* force refresh the admins list
  ❍ /fullpromote*:* if you want to promote an user with full rights then use it
  ❍ /fullpromote*:* if you want to fully promoted admin demote then use it
               """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(Chodu)")
                 ]
                ]
            ),
        )


def alicia_admin_warn_callback(update, context):
    query = update.callback_query
    if query.data == "aliciaadminwarn_":
        query.message.edit_text(
            text=""" Admins only*:*
  ❍ /warns <userhandle>*:* get a user's number, and reason, of warns.
  ❍ /warnlist*:* list of all current warning filters
  ❍ /warn <userhandle>*:* warn a user. After 3 warns, the user will be banned from the group. Can also be used as a reply.
  ❍ /dwarn <userhandle>*:* warn a user and delete the message. After 3 warns, the user will be banned from the group. Can also be used as a reply.
  ❍ /resetwarn <userhandle>*:* reset the warns for a user. Can also be used as a reply.
  ❍ /addwarn <keyword> <reply message>*:* set a warning filter on a certain keyword. If you want your keyword to \
  be a sentence, encompass it with quotes, as such: `/addwarn "very angry" This is an angry user`.
  ❍ /nowarn <keyword>*:* stop a warning filter
  ❍ /warnlimit <num>*:* set the warning limit
  ❍ /strongwarn <on/yes/off/no>*:* If set to on, exceeding the warn limit will result in a ban. Else, will just punch.
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(Chodu)")
                 ]
                ]
            ),
        )




def alicia_admin_mute_callback(update, context):
    query = update.callback_query
    if query.data == "aliciaadminmute_":
        query.message.edit_text(
            text=""" Admins only*:*
  ❍ /mute <userhandle>*:* silences a user. Can also be used as a reply, muting the replied to user.
  ❍ /tmute <userhandle> x(m/h/d)*:* mutes a user for x time. (via handle, or reply). `m` = `minutes`, `h` = `hours`, `d` = `days`.
  ❍ /unmute <userhandle>*:* unmutes a user. Can also be used as a reply, muting the replied to user.
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(Chodu)")
                 ]
                ]
            ),
        )


# Handlers start from here 

admin_callback_handler = CallbackQueryHandler(alicia_admin_callback, pattern=r"aliciaadmin_")
admin_ban_callback_handler = CallbackQueryHandler(alicia_admin_ban_callback, pattern=r"aliciaadminban_")
admin_purge_callback_handler = CallbackQueryHandler(alicia_admin_purge_callback, pattern=r"aliciaadminpurge_")
admin_promote_callback_handler = CallbackQueryHandler(alicia_admin_promote_callback, pattern=r"aliciaadminpromote_")
admin_warn_callback_handler = CallbackQueryHandler(alicia_admin_warn_callback, pattern=r"aliciaadminwarn_")
admin_mute_callback_handler = CallbackQueryHandler(alicia_admin_mute_callback, pattern=r"aliciaadminmute_")







