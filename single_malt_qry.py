"""
Count number of records for single malt scotch in `iowa-liquor-sample.csv`.

Reads the file and computes the number of records (in this file, each line is a
record) that contain the exact case insensitive phrase "single malt scotch".
Ignores upper and lower casing, so "Single Malt Scotch", and
"SINGLE Malt Scotch" all match, whereas "Single's Malty Scootch" does not.
"""

import csv
from pprint import pprint

CSV_PATH = 'iowa-liquor-sample.csv'
SEARCH_STRING = 'single malt scotch'

def count(s):
    c = 0
    with open(CSV_PATH) as fi:
        fi_reader = csv.reader(fi)
        fi_reader.next()  # remove header
        for row in fi_reader:
            found = map(lambda x: x.lower().find(s) > -1, row)
            if sum(found) > 0:
                c += 1
    return c

if __name__ == '__main__':
    print("Counting records in '%s' with '%s'..." % (CSV_PATH, SEARCH_STRING))
    c = count(SEARCH_STRING)
    print("Result: %d" % c)
