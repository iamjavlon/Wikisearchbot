from tracemalloc import start
from telegram import Update, User
from telegram.bot import Bot
from telegram.ext import MessageHandler, Updater, CommandHandler, CallbackContext
import settings


updater = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context:CallbackContext):
    update.message.reply_text("Assalamu alaykum!")

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()