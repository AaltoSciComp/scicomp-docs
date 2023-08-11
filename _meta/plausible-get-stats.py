import argparse
import os
import sys

import pandas
import requests

parser = argparse.ArgumentParser(
    description="""\
Download all stats from plausible, put them in csv like we could
export from the interface.

This is needed because the web interface will only export the
top 100 pages
"""
)
parser.add_argument('hostname', help="e.g. plausible.io")
parser.add_argument('siteid', help="e.g. your.side.fi")
parser.add_argument('token', help="bearer token from API, empty=PLAUSIBLE_TOKEN env var", nargs='?')
parser.add_argument('--time-period', default='12mo', help="time period of query (e.g. '12mo')")
args = parser.parse_args()

token = args.token or os.environ['PLAUSIBLE_TOKEN']

data = requests.get(f'https://{args.hostname}/api/v1/stats/breakdown'
                     f'?site_id={args.siteid}'
                     f'&period={args.time_period}'
                     '&property=event:page'
                     '&limit=1000'
                     '&metrics=visitors,pageviews,bounce_rate,visit_duration',
                     headers={"Authorization": f"Bearer {token}"})
print(data.status_code, data.reason, file=sys.stderr)

data = data.json()['results']
df = pandas.DataFrame(data)
df.rename(columns={'page': 'name', 'visit_duration': 'time_on_page'}, inplace=True)
df = df.set_index('name')
df.to_csv(sys.stdout)
