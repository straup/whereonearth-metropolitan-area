#!/usr/bin/env python

import sys
import os
import os.path
import json
import csv
import types

import logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':

    whoami = os.path.abspath(sys.argv[0])
    bindir = os.path.dirname(whoami)
    rootdir = os.path.dirname(bindir)

    datadir = os.path.join(rootdir, 'data')
    metadir = os.path.join(rootdir, 'meta')

    lookup_path = os.path.join(metadir, "metropolitan-areas.csv")
    lookup_fh = open(lookup_path, 'w')

    writer = csv.writer(lookup_fh)
    writer.writerow(('fid', 'woeid', 'iso', 'places', 'foundry'))

    for root, dirs, files in os.walk(datadir):

        for f in files:

            path = os.path.join(root, f)
            logging.info("processing %s" % path)

            fh = open(path)
            data = json.load(fh)

            feature = data['features'][0]
            props = feature['properties']

            fid = props.get('ne:fid', 0)
            woeid = props.get('woe:id', 0)
            iso = props.get('iso', '')
            places = props.get('ne:hasPlace', 0)

            foundry = props.get('artisanal:foundry', '')

            writer.writerow((fid, woeid, iso, places, foundry))
