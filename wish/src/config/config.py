import argparse

import yaml

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', dest='config', required=True, help='Path to the config')

args = parser.parse_args()
config = args.config
with open(config) as stream:
    configs = yaml.safe_load(stream)

db_host = configs['database']['host']
db_port = configs['database']['port']
db_name = configs['database']['db_name']
user_name = configs['database']['user_name']
user_pass = configs['database']['user_pass']
