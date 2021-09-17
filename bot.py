from secrets import tg_api_token
from secrets import omdb_api_token

import telebot

from tools import random_imdb_id
from tools import get_movie_poster
from tools import get_movie_info


BOT = telebot.TeleBot(tg_api_token)


@BOT.message_handler(commands=["start"])
def start_chat(message):
    BOT.send_message(message.chat.id, "Hello. I can send you a description of random movie, just type: /random")


@BOT.message_handler(commands=["random"])
def randomize_film(message):
    movie_id = random_imdb_id()
    movie_poster = get_movie_poster(movie_id, omdb_api_token)
    movie_info = get_movie_info(movie_id, omdb_api_token)
    BOT.send_photo(chat_id=message.chat.id,
                   photo=movie_poster,
                   caption=movie_info)
    movie_poster.close()


if __name__ == "__main__":
    BOT.polling()
