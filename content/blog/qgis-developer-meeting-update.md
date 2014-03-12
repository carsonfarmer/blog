Title: QGIS developer meeting update
Date: 2009-11-11 17:33
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Announcement
Tags: C++, geoprocessing, Python, QGIS, Free open-source software (FOSS), Geographic information science/systems (GIS), Helpful tip, How to
Slug: qgis-developer-meeting-update

Last week I attended the 2009 QGIS Developers Meeting in Vienna,
Austria. We all had a really good time, [met many new people][], and
actually got a lot done in the process. There have been updates about
the meeting [(hackfest)][] on the QGIS blog, and Tim Sutton has [written
a few words][] about our progress as well. I'm not going to repeat what
others have said, but I *would* like to give a quick update on the work
that I was doing at the meeting, and show off the new geoprocessing
features now available to all QGIS developers (Python and C++).
<!--more-->

My main goal for the meeting was to start/continue work on the new
'Analysis Library' for QGIS. Basically, this was intended to be a port
(to C++ from Python) of the [fTools][] suite of tools already available
in QGIS. These tools currently provide geoprocessing, geometry, and
various other analysis functionality natively within QGIS. However, the
Python implementation is simply a Python plugin, and so does not provide
these functions to other developers hoping use/add geoprocessing
capabilities to their own plugins or tools. In addition, in some cases
the Python fTools functions can be quite slow, and would benefit greatly
from the speed-ups afforded by a compiled language like C++.

Porting these functions to C++ is still underway, and so far we have
implementations for buffering, dissolving, centroids, convex hulls,
layer extents in the QgsGeometryAnalyzer class, and intersections in the
QgsOverlayAnalyzer class. We have set it up so that it should be
relatively easy to add functions and classes to the library in the
future, though I expect there will be many changes to the library along
the way. We have also created Python bindings for the library, so these
functions will also be available to Python developers. By doing so, it
is now extremely easy to perform geoprocessing functions directly from
the QGIS Python console, or from QGIS Python plugins, with only a few
lines of code.

### The old way
In the past, Python developers had to operate directly on the
geometries of the layers in order to do any sort of geoprocessing. For
example, to perform a (very) simple buffer, one had to use the following
code in the QGIS Python console:

```python
from qgis.core import iface
mc = iface.mapCanvas() # get a reference to the map canvas
layer = mc.layer(0) # get a reference to the first layer in the layer list
provider = layer.dataProvider() # data provider for the layer
provider.select(layer.pendingAllAttributesList(), QgsRectangle(), True, True) # select features to buffer
in_feat = QgsFeature() # empty input feature
out_feat = QgsFeature() # empty output feature
writer = QgsVectorFileWriter( "output_path.shp", provider.encoding(), provider.fields(), 
QGis.WKBPolygon, provider.crs() ) # use this to write results to disk (as shapefile)
while(provider.nextFeature(feat)): # for each feature that we selected...
    geometry = feat.geometry() # grab it's geometry
    buffer = geometry.buffer(100,10) # buffer the geometry
    out_feat.setAttributeMap(in_feat.attributeMap()) # set the attributes for the output feature
    out_feat.setGeometry(buffer) # set the bufer as the output geometry
    writer.addFeature(out_feat) # write the feature to file
del writer # delete/close the writer to save to disk
```

### The new way
With the new QGIS Analysis Library, things are much simpler, and the
same (or more complex) buffering example can be completed with only 5
lines of code in the QGIS Python Console:

```python
from qgis.core import iface # import iface (interface)
from qgis.analysis import QgsGeometryAnalyzer # import (par of) the analysis library
mc = iface.mapCanvas() # get a reference to the map canvas
layer = mc.layer(0) # get a reference to the first layer in the layer list
QgsGeometryAnalyzer().buffer(layer, "output_path.shp", 100, False, False, -1) # perform the buffer
```

Note: only the first two parameters in the buffer function are really
required, and the additional parameters control the buffer distance,
whether to use a subset (selected features) of the layer, whether to
dissolve the output buffer regions, and whether to use a field (field
ID) from the input layer's attribute table as the buffer distance.

Pretty nice eh? For now, the QGIS Analysis Library is only available in
Trunk, however, before long these tools should be available as part of
the official releases, so I hope we will start to see more Plugins
taking advantage of these new capabilities in the future...

[met many new people]: http://blog.qgis.org/node/139
[(hackfest)]: http://qgis.org/en/developer-meeting.html
[written a few words]: http://linfiniti.com/2009/11/report-back-on-the-qgis-hackfest-in-vienna-november-2009/
[fTools]: http://www.ftools.ca/
