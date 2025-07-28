from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from keep_alive import keep_alive

TOKEN = "YOUR_BOT_TOKEN"
ADMIN_ID = 6503335261  # your Telegram ID
authorized_users = [ADMIN_ID]

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    buttons = [
        [InlineKeyboardButton("Check Site", callback_data="check_site")],
        [InlineKeyboardButton("Check .txt File", callback_data="mchk")],
        [InlineKeyboardButton("Generate Cards", callback_data="gen")],
        [InlineKeyboardButton("Gateway Scanner", callback_data="gatemass")]
    ]
    if user_id == ADMIN_ID:
        buttons.append([InlineKeyboardButton("Admin Auth", callback_data="auth")])
    update.message.reply_text("Welcome! Use the buttons below:", reply_markup=InlineKeyboardMarkup(buttons))

def auth(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        update.message.reply_text("Unauthorized.")
        return
    try:
        new_id = int(context.args[0])
        if new_id not in authorized_users:
            authorized_users.append(new_id)
            update.message.reply_text(f"✅ User {new_id} authorized.")
        else:
            update.message.reply_text("Already authorized.")
    except:
        update.message.reply_text("Usage: /auth <user_id>")

def unauth(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        update.message.reply_text("Unauthorized.")
        return
    try:
        remove_id = int(context.args[0])
        if remove_id in authorized_users:
            authorized_users.remove(remove_id)
            update.message.reply_text(f"❌ User {remove_id} unauthorized.")
        else:
            update.message.reply_text("User not found.")
    except:
        update.message.reply_text("Usage: /unauth <user_id>")

def main():
    keep_alive()
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("auth", auth))
    dp.add_handler(CommandHandler("unauth", unauth))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
