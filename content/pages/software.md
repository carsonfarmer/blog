Title: Software
Date: 2008-09-23 09:49
Author: cfarmer
Email: carson.farmer@gmail.com
Slug: spatial-software
Icon: fa-code
Status: hidden

### Software development

Using the extensibility of QGIS (see below), I have developed several
python based 'spatial analysis' plugins to extend its functionality to
include spatial analysis, geoprocessing, geometry manipulation, both
spatial and aspatial statistics, as well as general data management
tools. The fTools plugin now comes standard with all versions of QGIS, and any 
additional plugins are now available via the Python Plugin installer from within QGIS.

### Quantum GIS

Quantum GIS (QGIS) is a free, user friendly Open Source Geographic
Information System ([GIS](http://en.wikipedia.org/wiki/GIS)) that runs on Linux, 
Unix, Mac OSX, and Windows. It supports vector, raster, and spatial database 
formats (e.g. ESRI ShapeFile, geotiff, PostGIS, etc.), and is licensed under 
the GNU General Public License.

#### QGIS Features

* Ability to view and overlay vector and raster data in different
  formats ([PostGIS](http://postgis.refractions.net/), 
  most [OGR vector formats](http://www.gdal.org/ogr/), all 
  [GDAL raster formats](http://www.gdal.org/), [GRASS](http://grass.itc.it/) 
  mapsets, and [WMS layers](http://en.wikipedia.org/wiki/Web_Map_Service)) 
  and projections
  without conversion to an internal or common format.
* Ability to create maps and interactively explore spatial data with a
  friendly graphical user interface.
* Ability to create, edit, and export spatial data to various
  different formats.
* Ability to publish maps on the internet in a few easy clicks
* Ability to create, edit, and use GRASS layers directly within QGIS,
  as well as the ability to use most GRASS tools through the 
  [GRASS plugin](http://wiki.qgis.org/qgiswiki/GrassCookbook) (available as 
  part of the standard QGIS install).
* Ability to adapt QGIS to specific needs through the extensible
  plugin architecture, allowing developers to extend the functionality
  of QGIS through python and C++ plugins. This allows more complex
  operations such as spatial analysis, geoprocessing functions, data
  management, as well as 
  [coupling QGIS with additional softare](http://www.ftools.ca/manageR.html),
  such as R.

### R Spatial

Spatial data analysis in R is evolving, and there are now a large number
of [  [packages](http://www.r-project.org/Rgeo/) that provide spatial 
statistical methods or interfaces
to GIS. The `sp` package provides classes and methods for spatial data
(points, lines, polygons, grids), and is now the 'standard' package for
handling spatial data, with several other packages (maptools, rgdal,
splancs, spgrass6, gstat, spgwr, ...) dependant on it.

#### R Spatial Resources

* [R spatial projects](http://r-spatial.sourceforge.net/) website is a good 
  starting point for basic information on the treatment of spatial data within R.
* [R Graphics](http://www.stat.auckland.ac.nz/~paul/RGraphics/rgraphics.html) 
  book from the Computer Science and Data Analysis Series by Paul Murrell
* [Applied Spatial Data Analysis with R](http://www.springerlink.com/content/978-0-387-78170-9)
  book from the UseR! series by Roger Bivand, Edzer Pebesma and Virgilio Gómez-Rubio.
* [R Cookbook](http://www.r-cookbook.com/node/40) is a great non-spatial resourse.

### Other Useful Software Links

* [Python Programming Language](http://www.python.org/)
* [Quantum Geographic Information System (QGIS)](http://www.qgis.org/)
* [Inkscape vector graphics editor](http://www.inkscape.org/)
* [Open Source Software Tools for Soil Scientists](http://casoilresource.lawr.ucdavis.edu/drupal/node/95) 
  from the California Soil Resource Lab is a fantastic resource for many open 
  source spatial projects, including R, PostGIS, GRASS, QGIS, and more.
