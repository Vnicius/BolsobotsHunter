import os
import shutil
import argparse
from utils.tweets_to_csv import tweets_to_csv

DEFAULT_LANG = 'pt'
DEFAULT_OUTPUT = 'data.csv'

def hunt(query, lang=DEFAULT_LANG, output=DEFAULT_OUTPUT):
    '''
        Get all tweets from a query and save as a .csv file

        Prams:
            query (str): query string
            lang (str): tweets language
            output (str): output file name
    '''
    # change to TweetScraper directory
    os.chdir('TweetScraper')

    # crawlling the tweets
    os.system(f'scrapy crawl TweetScraper -a query="{query}" -a lang="{lang}"')
    
    # returning to the root directory
    os.chdir('..')

    # creating the data path
    data_path = os.path.join('TweetScraper', 'Data', 'tweet')

    # convert the tweets directory to csv
    tweets_to_csv(data_path, output)

    # remove the original tweets directory
    shutil.rmtree(data_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', help='Search query')
    parser.add_argument('-l', '--lang', help='Language', default=DEFAULT_LANG)
    parser.add_argument('-o', '--output', help='Output file name', default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    hunt(args.query, args.lang, args.output)