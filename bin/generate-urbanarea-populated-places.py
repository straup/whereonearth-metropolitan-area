#!/usr/bin/env python

import sys
import os
import os.path
import csv
from rtree import index
import shapely.geometry

import json
import pprint

import logging
logging.basicConfig(level=logging.INFO)

def index_places(places): 

    reader = csv.DictReader(open(places, 'r'))
    idx = index.Index()

    for row in reader:

        woeid = row.get('woe_id', False)

        if int(woeid) == 0:
            continue

        id = int(woeid)

        lat = float(row.get('latitude', False))
        lon = float(row.get('longitude', False))

        idx.insert(id, (lon, lat, lon, lat))

    return idx

def crawl (data, idx):

    writer = csv.writer(open('urbanarea-populated-places.csv', 'w'))
    writer.writerow(('urbanarea_woeid', 'populatedplaces_woeid'))

    for root, dirs, files in os.walk(data):

        for f in files:

            path = os.path.join(root, f)
            logging.info("processing %s" % path)

            fh = open(path)
            data = json.load(fh)

            bbox = data.get('bbox', False)
            features = data['features'][0]
            props = features['properties']
            geom = features['geometry']

            ua_woeid = props.get('woe:id', 0)

            try:
                for pp_woeid in idx.intersection(bbox):
                    row = (ua_woeid, pp_woeid)
                    writer.writerow(row)

            except Exception, e:

                shp = shapely.geometry.asShape(geom)

                try:
                    for pp_woeid in idx.intersection(shp.bounds):
                        row = (ua_woeid, pp_woeid)
                        writer.writerow(row)

                except Exception, e:
                    print "FIX MY BBOX: %s" % path
                    print e
                    continue

if __name__ == '__main__':

    places = sys.argv[1]
    data = sys.argv[2]

    idx = index_places(places)
    crawl(data, idx)

    

