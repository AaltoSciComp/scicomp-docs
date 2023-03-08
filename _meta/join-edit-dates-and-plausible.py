import argparse
import datetime
import re
import sys

import pandas

parser = argparse.ArgumentParser(
    description="""\
Combine a Plausible export (pages.csv) with the latest edit dates of
all files in the Git repository.  Produce a new CSV with the files
joined based on page name, sorted by most visited pages, for viewing
in (for example) a spreadsheet.
"""
)
parser.add_argument('plausible-pages', help="`pages.csv` in plausible export zipfile")
parser.add_argument('page-dates', help="Output of `make find-old`")
args = parser.parse_args()


def source_to_url(page):
    page = page.strip(' /')
    if page.endswith('index.rst'):
        return page[:-10]
    elif page.endswith('index.html'):
        return page[:-11]
    elif page.endswith('.rst'):
        return page[:-4]
    elif page.endswith('.md'):
        return page[:-3]
    else:
        return page

stats = pandas.read_csv(getattr(args, 'plausible-pages'),
    index_col='name',
    converters={
        'name': source_to_url,
    },
    )
# Aggregate by name.  bounce_rate and time_on_page needto be weighted
# averages, which we can do by weighting them before aggeregating and
# then un-weighting after.
stats['bounce_rate'] *= stats['visitors']
stats['time_on_page'] *= stats['pageviews']
stats = stats.groupby('name').agg(sum)
stats['bounce_rate'] //= stats['visitors']
stats['time_on_page'] //= stats['pageviews']
stats = stats.convert_dtypes()

dates = pandas.read_csv(getattr(args, 'page-dates'),
    header=None,
    index_col='page',
    names=['time', 'date', 'page'],
    converters={
        'time': lambda x: datetime.datetime.fromtimestamp(int(x)),
        'page': source_to_url,
    },
    )

stats = stats.join(dates, how='outer')
stats = stats.sort_values('pageviews', ascending=False)
stats['age'] = stats.time.apply(lambda x: (datetime.datetime.now()-x).days)

stats.to_csv(sys.stdout)
stats.index.set_names('page', inplace=True)
