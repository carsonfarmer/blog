Title: OSM data by country
Date: 2010-05-13 12:05
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Free open-source software (FOSS)
Tags: Ireland, OpenStreetMap, PostGIS, Road Networks, Geographic information science/systems (GIS), Helpful tips, Networks, Research
Slug: osm-data-by-country

For part of a traffic simulation project I am currently working on we
need country-wide road network data for Ireland. In the past, getting
decent road network data for an area this large was quite a task (not to
mention expensive and time consuming), however, with OpenStreetMap we
have access to this type of data instantly, and for free! In order to
download full country coverage all at once, all I had to do was turn to
this [extremely useful site][], which provides links for daily excerpts
of OpenStreetMap data for any country in Europe plus several non-country
regions such as the Alps region, as well as select countries outside of
Europe. It currently also features [special coverage of Haiti][].

Now that I have the OSM data downloaded, it should be relatively easy to
import it into my PostGIS database using [pgRouting][] and the
[osm2pgrouting][] import tool. More to come on this topic once I get
things working nicely...

[extremely useful site]: http://download.geofabrik.de/osm/
[special coverage of Haiti]: http://labs.geofabrik.de/haiti/
[pgRouting]: http://pgrouting.postlbs.org/
[osm2pgrouting]: http://pgrouting.postlbs.org/wiki/tools/osm2pgrouting
