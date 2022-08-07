from tracemalloc import start
from urllib import response
from telegram import Update
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, CallbackContext
import requests
import settings


updater = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context:CallbackContext):
    update.message.reply_text('Welcome to Wikipedia Search Bot! '
                              'In order to find information about something please use /search '
                              'and add your requested name. For example /search Earth ')

def search(update: Update, context:CallbackContext):
    args = context.args

    if len(args) == 0:
        update.message.reply_text('Please insert a word or a phrase to send a request to this bot')
    else:
        search_text = ' '.join(args)
        response = requests.get('https://en.wikipedia.org/w/api.php', {
            'action': 'opensearch',
            'search': search_text,
            'limit': 1,
            'namespace': 0,
            'format': 'json',
        })

        result = response.json()
        link = result[3]
        if len(link):
            update.message\
                .reply_text('Link for your request: ' + link[0])
        else:
            update.message\
                .reply_text('There is no information about this request')



dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start))


updater.start_polling()
updater.idle()