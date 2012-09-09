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
Populated Places. Specifically the latter should contain a pointer to the former in their hierarchy. So, this file is included as a point of reference.

Not all NE records have [Geonames](http://www.geonames.org/) IDs or WOE IDs associated
with them. As of this writing the list has diverged from Natural Earth and some records may have WOE IDs but not Geonames IDs. That's because the WOE IDs were derived by geocoding the NE name (name, adm1, adm0) against the Flickr API and running the results through the [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) python library (really) and only accepting things with a score >= 95.

_The complete list of things to be geocoded still is in populated-places-to-be-geocoded.csv._

urbanareas-populated-places.csv
==

A plain vanilla CSV file mapping the relationships between an urban/metropolitan
WOE ID (see also: metropolitan-areas.csv) to one or more WOE IDs defined in the
concordance for Natural Earth populated places (see also:
populated-places-concordance.csv).

_This list is currently incomplete. There are still some populated places that
have neither a WOE ID or a Geonames ID. Those records have not been included in
this list._

