Title: View spatial data attribute tables in R
Date: 2008-10-14 13:44
Author: cfarmer
Email: carson.farmer@gmail.com
Category: Helpful tip
Tags: FOSS, GIS, How-To, R spatial
Slug: view-spatial-data-attribute-tables-in-r

Many GIS offer the ability to view the attribute table of a vector
layer. While this is perhaps less obvious in the R environment, it is
not impossible. The following command allows you to visually inspect,
and change any data.frame (or other vector, matrix, etc.), including
Spatial*DataFrames.
<!--more-->

```r
invisible(edit(spatial_layer@data))
```
Note: `invisible` allows you to close the viewer without filling the
console with the attributes of the table. You could also use:

```r
new_data = edit(spatial_layer@data)
```
to assign changes made to the data to a new variable, or use:
```r
spatial_layer@data = edit(spatial_layer@data)
```
or,
```r
fix(spatial_layer@data)
```
to make changes to the Spatial*DataFrame itself.
