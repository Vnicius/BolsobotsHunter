import argparse
import re
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('file', help='CSV file with the tweets')
parser.add_argument('-o', '--output', help='Output file name', default='blacklist.csv')
args = parser.parse_args()


df = pd.read_csv(args.file, encoding='utf-8')
users = df[['user_id', 'usernameTweet']]
users_unique = users.drop_duplicates('user_id')
bad_usernames = users[users['usernameTweet'].str.match(r'\w+\d{5,}')]

bad_usernames.to_csv(args.output, encoding='utf-8', index=False)

