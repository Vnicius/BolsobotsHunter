import sys
import argparse
import re
import pandas as pd

DEFAULT_OUTPUT = 'list.csv'

def snif(input_file, output=DEFAULT_OUTPUT):
    '''
        Search for suspicious users in the tweets

        Params:
            input_file (str): input file name
            output (str): output file name
    '''
    # read the file
    df = pd.read_csv(input_file, encoding='utf-8')

    if df.empty:
        sys.exit('Empty file')
    
    # get only the users id and username
    users = df[['user_id', 'usernameTweet']]
    
    # get only unique users
    users_unique = users.drop_duplicates('user_id')
    
    # apply the filter to get suspecious users
    bad_usernames = users[users['usernameTweet'].str.match(r'\w+\d{5,}')]

    # save the result
    bad_usernames.to_csv(output, encoding='utf-8', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='CSV file with the tweets')
    parser.add_argument('-o', '--output', help='Output file name', default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    snif(args.file, args.output)

