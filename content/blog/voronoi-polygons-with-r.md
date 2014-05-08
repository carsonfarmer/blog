Title: Voronoi polygons with R
Date: 2009-09-16 22:30
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful Tip
Tags: R, FOSS, How-To
Slug: voronoi-polygons-with-r

To create a nice bounded Voronoi polygons tessellation of a point layer
in `R`, we need two libraries: `sp` and `deldir`. The following function
takes a `SpatialPointsDataFrame` as input, and returns a
`SpatialPolygonsDataFrame` that represents the Voronoi tessellation of
the input point layer.
<!--more-->

```r
voronoipolygons = function(layer) {
    require(deldir)
    crds = layer@coords
    z = deldir(crds[,1], crds[,2])
    w = tile.list(z)
    polys = vector(mode='list', length=length(w))
    require(sp)
    for (i in seq(along=polys)) {
        pcrds = cbind(w[[i]]$x, w[[i]]$y)
        pcrds = rbind(pcrds, pcrds[1,])
        polys[[i]] = Polygons(list(Polygon(pcrds)), ID=as.character(i))
    }
    SP = SpatialPolygons(polys)
    voronoi = SpatialPolygonsDataFrame(SP, data=data.frame(x=crds[,1], 
        y=crds[,2], row.names=sapply(slot(SP, 'polygons'), 
        function(x) slot(x, 'ID'))))
}
```

To save the output to shapefile, simply use` writeOGR` from the `rgdal`
library:
```r
library(rgdal)
?writeOGR
```
