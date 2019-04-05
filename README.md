# Bolsobots Hunter

## Install

### TweetScraper

```sh
  $ git clone https://github.com/jonbakerfish/TweetScraper.git
```

### Dependencies

- Anaconda

```sh
  $ conda env create -f environment.yml
```

```sh
  $ conda activate bolsobotshunter
```

- Pip

```sh
  $ pip install -r requirements.txt
```

## Usage

### [mission.py](./mission.py)

```sh
usage: mission.py [-h] [-q QUERY] [-l LANG] [-t TWEETS_FILE] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Search query
  -l LANG, --lang LANG  Tweets language
  -t TWEETS_FILE, --tweets-file TWEETS_FILE
                        Tweets file name
  -o OUTPUT, --output OUTPUT
                        Output file name
```

### [hunt.py](./hunt.py)

```sh
usage: hunt.py [-h] [-q QUERY] [-l LANG] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Search query
  -l LANG, --lang LANG  Language
  -o OUTPUT, --output OUTPUT
                        Output file name
```

### [snif.py](./snif.py)

```sh
usage: snif.py [-h] [-o OUTPUT] file

positional arguments:
  file                  CSV file with the tweets

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file name
```

## Getting the tweets

### Examples

- 1 - Searching tweets with the term `Golden Shoulder` and saving in the `tweets_gs.csv`

```sh
  $ python hunt.py -q "Golden Shoulder" -o tweets_gs
```

## Getting the suspicious users in the tweets

### Examples

- 1 - Searching for suspicious users in the file `tweets_gs.csv`

```sh
  $ python snif.py tweets_gs.csv -o suspicious.csv
```

## Getting the suspicious users with a query

### Examples

- 1 - Searching tweets with the term `Golden Shoulder` and saving the suspicious user in the file `list.csv`

```sh
  $ python mission.py -q "Golden Shoulder" --tweets-file tweets_gs -o list.csv
```

## Query

See the [TweetScraper usage](https://github.com/jonbakerfish/TweetScraper#usage)
