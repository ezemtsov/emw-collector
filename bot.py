import logging
import re
import os

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters)

import spotify

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#Spotify data
user = os.getenv("SPOTIFY_USER")
playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")

#Telegram data
token = os.getenv('TELEGRAM_TOKEN')
updater = Updater(token)
dispatcher = updater.dispatcher

#Bot text
collected_msg = "collected to emw 😍"
duplicate_msg = "that's a duplicate, dummy 🙃"
help_msg = "Hi dudes, I'll collect your stuff"

def help(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text= help_msg)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


def echo(bot, update):
    message = update.message.text
    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]' \
        '|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)

    for url in urls:
        if "open.spotify.com/track" in url:
            sp = spotify.login(user)
            track_id = spotify.search_track(sp,url)
            result = spotify.add_track(sp,user,playlist_id,track_id)

            if result == True:
                output = collected_msg
            else:
                output = duplicate_msg
            
            bot.send_message(
                chat_id = update.message.chat_id,
                text    = output
            )
    
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
