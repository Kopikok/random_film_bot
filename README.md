# Random Film Bot

Random Film Bot is a Python programm that will send you a random movie from OMDb (Open Movie Database) after sending command <code>/random</code> in Telegram

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the bot.

```bash
pip install -r requirements.txt
```

## Usage

To start the bot just type in cmd:

```bash
python3 bot.py
```

## Messages

<code>/start</code> - to start chat with the bot

<code>/abs_random</code> - to get a random movie

<code>/good_random</code> - to get a good random movie. The good movie contains at least 4 of 6 fields


## Dataset

Dataset <code>data/titles_dataset.ds</code> based on [IMDB's title basic dataset](https://datasets.imdbws.com/title.basics.tsv.gz) you can read more about it [here](https://www.imdb.com/interfaces/)

<code>data/titles_dataset.ds</code> contains only IMDB's ids of <code>movie</code> type videos splitted by whitespace
