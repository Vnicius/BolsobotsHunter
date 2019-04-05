import argparse
from hunt import hunt
from snif import snif

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', help='Search query')
    parser.add_argument('-l', '--lang', help='Tweets language', default='pt')
    parser.add_argument('-t','--tweets-file', help='Tweets file name', default='tweets.csv')
    parser.add_argument('-o', '--output', help='Output file name', default='list.csv')
    args = parser.parse_args()

    hunt(args.query, args.lang, args.tweets_file)
    snif(args.tweets_file, args.output)