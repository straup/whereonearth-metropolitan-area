#!/usr/bin/env python

import sys
import os
import os.path
import json
import utils
import pprint
import random
import shapely.geometry

import ArtisinalInts

import logging
logging.basicConfig(level=logging.INFO)

def generate_lookup_table(options):

    lookup = {}

    for root, dirs, files in os.walk(options.data):

        for f in files:

            if not f.endswith(".json") :
                continue

            path = os.path.join(root, f)
            path = os.path.abspath(path)

            fh = open(path, 'r')
            data = json.load(fh)
            fh.close()

            f = data['features'][0]
            props = f['properties']

            # FIX ME

            try:
                lookup[ props['ne:fid'] ] = props['woe:id']
            except Exception, e:
                pass

    return lookup
            
def import_urbanareas(options):

    # sudo make me work with multiprocessor...

    lookup = generate_lookup_table(options)

    areas = os.path.abspath(options.urbanareas)

    fh = open(areas, 'r')
    data = json.load(fh)

    for f in data['features']:

        ne_props = f['properties']
        ne_geom = f['geometry']
        ne_id = f['id']

        print ne_id

        props = {
            'ne:fid' : ne_id
            }

        woeid = lookup.get(ne_id, 0)

        if woeid != 0:

            woe_root = utils.woeid2path(woeid)
            woe_root = os.path.join(os.path.abspath(options.data), woe_root)

            fname = "%s.json" % woeid
            woe_path = os.path.join(woe_root, fname)

            woe_fh = open(woe_path, 'r')
            woe_data = json.load(woe_fh)

            woe_features = woe_data['features'][0]
            props = woe_features['properties']
                
        else:
            woeid, foundry = get_artisanal_int()
                
            props['woe:id'] =  woeid
            props['placetype'] = 'metropolitan-area'
            props['artisanal:id'] = woeid
            props['artisanal:foundry'] = foundry

        for k, v in ne_props.items():
            k = "ne:%s" % k
            props[k] = v

        shp = shapely.geometry.asShape(ne_geom)
        
        feature = {
            'id': woeid,
            'properties': props,
            'geometry': ne_geom
            }

        woe_data = {
            'type': 'FeatureCollection',
            'features': [ feature ],
            'bbox': shp.bounds
            }

        # print pprint.pformat(woe_data)
        # sys.exit()

        woe_root = utils.woeid2path(woeid)
        woe_root = os.path.join(os.path.abspath(options.data), woe_root)

        if not os.path.exists(woe_root):
            os.makedirs(woe_root)
            
        fname = "%s.json" % woeid

        woe_path = os.path.join(woe_root, fname)

        woe_fh = open(woe_path, 'w')
        woe_data = json.dump(woe_data, woe_fh, indent=2)
        woe_fh.close()
            
        print woe_path

def get_artisanal_int():

    i = random.randrange(0, 3)

    while True:

        try:
            if i == 0:
                int, ignore = ArtisinalInts.get_mission_integer()
                return int, "http://www.missionintegers.com/"
            elif i == 1:
                int, ignore = ArtisinalInts.get_brooklyn_integer()        
                return int, "http://www.brooklynintegers.com/"
            else:
                int, = ArtisinalInts.get_london_integer()
                return int, "http://www.londonintegers.com/"

        except Exception, e:
            print e

    return None

if __name__ == '__main__':

    import optparse

    parser = optparse.OptionParser(usage='')

    parser.add_option('--urbanareas', dest='urbanareas',
                        help='',
                        action='store')

    parser.add_option('--data', dest='data',
                        help='',
                        action='store')

    parser.add_option('--debug', dest='debug',
                        help='Enable debug logging',
                        action='store_true', default=False)

    options, args = parser.parse_args()

    if options.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


    import_urbanareas(options)
    logging.info("done");

    sys.exit()
