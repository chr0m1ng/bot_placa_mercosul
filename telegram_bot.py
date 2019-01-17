#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from placa_drawer import Placa
import logging
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Envie /placa_carro AAA-0000 ou /placa_moto AAA-0000')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Envie /placa_carro AAA0000')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text('Desculpe, não entendi "%s"' % update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def placa_carro(bot, update, args):
    if len(args) > 0:
        chat_id = update.message.chat_id
        pl = Placa()
        placa = pl.Desenhar(args[0], 'carro')
        placa.save('./tmp/%s.png' % (args[0]))
        bot.send_photo(chat_id=chat_id, photo=open('./tmp/%s.png' % (args[0]),'rb'))
        placa.close()
        os.remove('./tmp/%s.png' % (args[0]))
    else:
        update.message.reply_text('É necessario enviar a placa')

def placa_carro_aluguel(bot, update, args):
    if len(args) > 0:
        chat_id = update.message.chat_id
        pl = Placa()
        placa = pl.Desenhar(args[0], 'carro', 'comercial')
        placa.save('./tmp/%s.png' % (args[0]))
        bot.send_photo(chat_id=chat_id, photo=open('./tmp/%s.png' % (args[0]),'rb'))
        placa.close()
        os.remove('./tmp/%s.png' % (args[0]))
    else:
        update.message.reply_text('É necessario enviar a placa')

def placa_moto(bot, update, args):
    if len(args) > 0:
        chat_id = update.message.chat_id
        pl = Placa()
        placa = pl.Desenhar(args[0], 'moto')
        placa.save('./tmp/%s.png' % (args[0]))
        bot.send_photo(chat_id=chat_id, photo=open('./tmp/%s.png' % (args[0]),'rb'))
        placa.close()
        os.remove('./tmp/%s.png' % (args[0]))
    else:
        update.message.reply_text('É necessario enviar a placa')

def placa_moto_aluguel(bot, update, args):
    if len(args) > 0:
        chat_id = update.message.chat_id
        pl = Placa()
        placa = pl.Desenhar(args[0], 'moto', 'comercial')
        placa.save('./tmp/%s.png' % (args[0]))
        bot.send_photo(chat_id=chat_id, photo=open('./tmp/%s.png' % (args[0]),'rb'))
        placa.close()
        os.remove('./tmp/%s.png' % (args[0]))
    else:
        update.message.reply_text('É necessario enviar a placa')

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    token = os.environ.get('bot_mercosul_token', 'faltou token')
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("placa_carro", placa_carro, pass_args=True))
    dp.add_handler(CommandHandler("placa_carro_aluguel", placa_carro_aluguel, pass_args=True))
    dp.add_handler(CommandHandler("placa_moto", placa_moto, pass_args=True))
    dp.add_handler(CommandHandler("placa_moto_aluguel", placa_moto_aluguel, pass_args=True))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    print ('Starting bot...')
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()