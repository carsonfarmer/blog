Title: Speeding up geoprocessing in QGIS
Date: 2010-04-01 14:55
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Announcement
Tags: C++, geoprocessing, Python, QGIS, Free open-source software (FOSS), Geographic information science/systems (GIS)
Slug: speeding-up-geoprocessing-in-qgis

Last night I had an uncontrollable urge to make geopoprocessing in QGIS
better, faster and more fun! I had come across a couple of posts
([here][], [here][1]) on the idea of a cascaded union operation, and
since it has recently been added to [GEOS][] (which QGIS uses for its
geometry operations), I thought I'd give a much needed boost to the
fTools union tool and related functions.
<!--more-->

This required a bit of mucking about with [QgsGeometry][], but in the
end it really didn't take too much hacking to get things working
properly. I was able to add a `combineCascaded(QList<QgsGeometry*>)`
function to the `QgsGeometry` class, as well as the required Python
bindings. Basically what this function does is union small subsets of
the input layer, then union groups of the resulting features, and so on
recursively until the final union of all features in the input list is
computed. There is a nice explanation of the algorithm straight from the
horses mouth [here][].

I haven't yet committed these additions, as I'm not quite sure I like
how I've done things, but just to prove how much faster things can be,
here is a quick little demo that can be run from the built-in QGIS
Python console:

```python
import time
canvas = qgis.utils.iface.mapCanvas()
layer = canvas.layer(0) # assumes target layer is fist in layer list
provider = layer.dataProvider()
attrs = provider.attributeIndexes()
provider.select(attrs)
geoms = []
feat = QgsFeature()
# get a list of all the feature geometries in the layer
while(provider.nextFeature(feat)):
    geom = QgsGeometry(feat.geometry())
    geoms.append(geom)
```
First, using the current method, which adds all the geometries together one by one:

```python
start = time.time()
regular_geom = geom # start with the last geometry in the layer
for geometry in geoms:
    regular_geom = QgsGeometry(regular_geom.combine(geometry))
end = time.time()
total = end-start
print total
```

Secondly, using cascaded union, which uses magic to combine geometries together
more efficiently. Also requires fewer lines of code!

```python
start = time.time()
cascaded_geom = geom.combineCascaded(geoms)
end = time.time()
total = end-start
print total
```

When I tested this last night on the `grassland.shp` layer from the
[QGIS sample dataset][] the results were about **86.89** seconds for the
'old' method, and **6.14** seconds for the cascaded union method. That's
a **14.15** times speedup on a relatively small layer (about 143
features of varying complexity)! I've tested the function on both
poylgons and lines so far, and it appears to work quite nicely.
Eventually I'll add this to the official QGIS API so that others can
take advantage of the speedup. Additionally, the other fTools functions
which rely to some degree on unioning will also benefit from the extra
speed, which is always a good thing.

[here]: http://lin-ear-th-inking.blogspot.com/search?q=cascaded
[1]: http://blog.cleverelephant.ca/2009/01/must-faster-unions-in-postgis-14.html
[GEOS]: http://trac.osgeo.org/geos/
[QgsGeometry]: http://doc.qgis.org/stable/classQgsGeometry.html
[QGIS sample dataset]: http://www.qgis.org/en/download/sample-data.html
