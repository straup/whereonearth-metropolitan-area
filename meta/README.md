metropolitan-areas.csv
==

A plain vanilla CSV file mapping [Natural Earth Urban Area](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-urban-area/) `FID` IDs and
(artisanal) WOE IDs. Also included is the ISO-2 country code for the centroid of
the record's polygon derived from the [Flickr API](http://www.flickr.com/services/api/flickr.places.findByLatLon.html), the number of places
contained by the record and the foundry used to generate the artisanal WOE ID.

populated-places-concordance.csv
==

A plain vanilla CSV file mapping the concordance between the `GEONAMEID` field
in the [Natural Earth (NE) Populated
Places](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-populated-places/)
dataset to corresponding OpenStreetMap (OSM), Wikipedia and Where On Earth (WOE)
IDs. Also included are the NE name, ISO-3 country code and "megacity" status for
each record.

There is quite a lot of /overlap between Urban (metropolitan) Areas and
Populated Places so this file is included as a point of reference.

_Not all NE records have [Geonames](http://www.geonames.org/) IDs associated
with them._
