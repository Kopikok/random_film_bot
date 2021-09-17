from secrets import tg_api_token
from secrets import omdb_api_token

import telebot

from tools import get_movie_info
from tools import get_good_movie_info


BOT = telebot.TeleBot(tg_api_token)


@BOT.message_handler(commands=["start"])
def start_chat(message):
    BOT.send_message(message.chat.id, "Hello. I can send you a description of random movie, just type: /abs_random\n" +
                     "or you can type: /good_random to get random movie with guaranteed description")


@BOT.message_handler(commands=["help"])
def send_help(message):
    BOT.send_message(message.chat.id, "Type /abs_random to get info about random movie\n" +
                     "Type /good_random to get info about random good movie" +
                     "The good movie will have more information than other")


@BOT.message_handler(commands=["abs_random"])
def randomize_movie(message):
    movie_info, movie_poster = get_movie_info(omdb_api_token)
    BOT.send_photo(chat_id=message.chat.id,
                   photo=movie_poster,
                   caption=movie_info)
    try:
        movie_poster.close()
    except AttributeError:
        pass


@BOT.message_handler(commands=["good_random"])
def get_good_movie(message):
    movie_info, movie_poster = get_good_movie_info(omdb_api_token)
    BOT.send_photo(chat_id=message.chat.id,
                   photo=movie_poster,
                   caption=movie_info)
    try:
        movie_poster.close()
    except AttributeError:
        pass


if __name__ == "__main__":
    BOT.polling()
