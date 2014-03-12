Title: Adding direct editing of geometry fields in QGIS
Date: 2011-03-12 18:43
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful tip
Tags: Geographic information science/systems (GIS), Geometry, PyQGIS, Python, QGIS, Free open-source software (FOSS)
Slug: adding-direct-editing-of-geometry-fields-in-qgis

Being able to add/remove attributes isn't actually a very new feature
for QGIS at this point. However, to date non of the fTools functions
(Vector menu) have taken advantage of this capability. If a tool needed
to create a new field in the input vector layer, it simply wrote a new
version of the vector layer to disk with the additional fields added.
There have been several requests to allow some tools to add/update
attributes directly on the input layers, so I went ahead and created a
script to test this functionality out. I've 
[provided a copy here](|filname|/uploads/add_geometry_information.py) 
for anyone who would like to test it out before I add it to QGIS
permanently. Basically, the script will replace/update three of the
Vector menu tools, including `Analysis \> Sum line lengths`, `Analysis
\> Points in polygon`, and `Geometry tools \> Add/Export geometry
info`.
<!--more-->
Here are some examples of the script's usage from the QGIS Python
console:

1. Add geometry information (assumes that the target layer in first
layer in the layer-list):

```python
>>> mc = qgis.utils.iface.mapCanvas()
>>> layer = mc.layer(0)
>>> import add_geometry_information
>>> add_geometry_information.addGeometryInformation(vlayer) True
```

2. Count the number of points or length of lines in each polygon of an
input polygon layer (assumes polygon layer is second, and point or line
layer is the first in layer-list):

```python
>>> polygonLayer = mc.layer(1)
>>> input Layer = mc.layer(0)
>>> add_geometry_information.countFeaturesInPolygon(polygonLayer, inputLayer) True
```

Note that to import the module properly (and easily), make sure it is
somewhere that PyQGIS can find it, such as `\~/.qgis/python`. If the layer
is in editing mode, then udpates can be undone, otherwise, updates are
written automatically to the provider. The `countFeaturesInPolygon()`
function automatically recognizes if an input layer is a point or line
layer, and computes the correct information accordingly (outputting a
count for points, and line lengths for lines). For both functions, the
last argument can be a boolean specifying whether to update selected
features only (`default=False`).

C
