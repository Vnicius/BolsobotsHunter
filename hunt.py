import os
import shutil
import argparse
from tweets_to_csv import tweets_to_csv

parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query', help='Search query')
parser.add_argument('-l', '--lang', help='Language', default='pt')
parser.add_argument('-o', '--output', help='Output file name', default='data.csv')
args = parser.parse_args()

os.chdir('TweetScraper')
os.system(f'scrapy crawl TweetScraper -a query="{args.query}" -a lang="{args.lang}"')
os.chdir('..')

data_path = os.path.join('TweetScraper', 'Data', 'tweet')

tweets_to_csv(data_path, args.output)

shutil.rmtree(data_path)