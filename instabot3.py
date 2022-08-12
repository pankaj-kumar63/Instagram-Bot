"""
    Follow
"""

import argparse
import sys
import os

from tqdm import tqdm

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('user', type=str, help='user')
args = parser.parse_args()

# Add your bots here
BOTS_DATA = [
    {
        "username": "shukla928",
        "password": "7379561059",
        "proxy": "https://47.9.84.158"
    }
    # {
    #     "username": "user2",
    #     "password": "pass2",
    #     "proxy": "https://47.9.84.158"
    # },
    # {
    #     "username": "user3",
    #     "password": "pass3",
    #     "proxy": "https://47.9.84.158"
    # },
    # {
    #     "username": "user4",
    #     "password": "pass4",
    #     "proxy": "https://47.9.84.158"
    # },
]

for bot in tqdm(BOTS_DATA):
    bot['bot'] = Bot()
    bot['bot'].login(username=bot['kavita_patel7'], password=bot['kavitapatel9ptl'], proxy=bot['https://47.9.84.158'])
    bot['bot'].follow(args.user)