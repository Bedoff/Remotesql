from time import strftime
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, messagehandler
import mysqlcon

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hoşgeldin')
    update.message.reply_text('Bu bot sayesinde uzaktan mysql komutları çalıştırabilirsin')  #şuan için böyle çalışmıyor aşağıda belirlenmiş coinlerin sinyallerini veriyor
    update.message.reply_text('Eğer yardıma ihtiyacın olursa /help yazabilirsin')
    update.message.reply_text('Unutma ki bu bot geliştirilme sürecindedir')
        

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('yazım aşamasında')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def do_something(user_input):
    answer = mysqlcon.mydefsql(user_input)
    return answer

def reply(update, context):
    user_input = update.message.text
    update.message.reply_text(do_something(user_input))


def main():
    """Start the bot."""
    updater = Updater("2104334279:AAHWvAtw9JqjSa5oY74_PX23VH0wKUR6Pf4", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))   
    dp.add_handler(MessageHandler(Filters.text, reply))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()