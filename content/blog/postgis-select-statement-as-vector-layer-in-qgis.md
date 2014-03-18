Title: PostGIS 'select' statement as vector layer in QGIS
Date: 2010-04-27 17:40
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful tip
Tags: PostGIS, QGIS, Query, Vector, FOSS, GIS, How-To
Slug: postgis-select-statement-as-vector-layer-in-qgis

Several colleagues of mine have asked whether it is possible to
visualise the results of a `SELECT` statement on a [PostGIS][] database
that returns spatial data in [QGIS][]. In other words, can we map the
results of something like:

```bash
SELECT id, st_union(the_geom) FROM spatial_table GROUP BY id;
```
My usual answer to this in the past has been "not yet...", but now thanks
to Giuseppe Sucameli and Jürgen E. Fischer, the answer is a resounding
"yes!". A [recent patch][] to QGIS trunk now makes custom Postgres
queries possible via the postgres data provider.
<!--more-->

<strike>Unfortunately there is no user interface implemented to take advantage
of this functionality (yet!)</strike>There is now a plugin available from the
[Faunalia python plugin repository][] called `RT Sql Layer` which provides
a GUI for loading `PostGIS` `SELECT` statements as layer, but you can also
access this handy feature via the `QGIS` `Python` console:

```python
db_conn = "dbname='gis' host=localhost port=5432 user='cfarmer' password='xxxx'"
id_field = "id"
table = "(select id, st_union(the_geom) from spatial_table group by id)"
uri = "%s key=%s table=%s (the_geom) sql=" % (db_conn,id_field,table,)
layer = QgsVectorLayer(uri, "testlayer", "postgres")
```

we can then add the layer to the map canvas via:

```python
QgsMapLayerRegistry.instance().addMapLayer(layer)
```

and even query/measure it via something like:

```python
provider = layer.dataProvider()
feat = QgsFeature()
provider.select([], QgsRectangle())
provider.nextFeature(feat)
dist = QgsDistanceArea()
dist.measure(feat.geometry())
```
Just another one of the many new features being added to QGIS every day!

[PostGIS]: http://postgis.refractions.net/
[QGIS]: http://www.qgis.org/
[recent patch]: https://trac.osgeo.org/qgis/changeset/13340
[Faunalia python plugin repository]: http://www.faunalia.it/qgis/plugins.xml
