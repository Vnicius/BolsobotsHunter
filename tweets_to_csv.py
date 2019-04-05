
import pandas as pd
import glob
import json
import io

def tweets_to_csv(input_dir, file_name):
  directory = input_dir
  out_name = file_name

  if directory[-1] != '/':
    directory += '/'

  if '.csv' not in out_name:
    out_name += '.csv'

  files = glob.glob(directory + '*')
  #print(len(files))

  dictlist = []

  for file in files:

      json_string = io.open(file, 'r', encoding="utf-8").read()
      # print(json_string)
      json_dict = json.loads(json_string)
      dictlist.append(json_dict)

  df = pd.DataFrame(dictlist)

  df = df.replace({'\n': ' '}, regex=True)
  df = df.replace({'\t': ' '}, regex=True)

  df.to_csv(out_name, encoding='utf-8')

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument('dir', help='Directory with the Tweets')
  parser.add_argument('-n', '--name', help='Output file name', default='data.csv')
  args = parser.parse_args()
  
  tweets_to_csv(args.dir, args.file_name)