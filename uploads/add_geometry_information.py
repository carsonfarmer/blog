# -*- coding: utf-8 -*-
#-----------------------------------------------------------
#
# This file is part of fTools
# Copyright (C) 2011  Carson Farmer
# EMAIL: carson.farmer (at) gmail.com
# WEB  : http://www.ftools.ca/fTools.html
#
# A collection of data management and analysis tools for vector data
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------

from PyQt4.QtCore import *
from qgis.core import *

def geometryInformation(geom):
    if geom.wkbType() in (QGis.WKBPoint, QGis.WKBPoint25D):
        pt = QgsPoint()
        pt = inGeom.asPoint()
        attr1 = pt.x()
        attr2 = pt.y()
    else:
        measure = QgsDistanceArea()
        attr1 = measure.measure(geom)
        if geom.type() == QGis.Polygon:
            attr2 = perimeterLength(geom, measure)
        else: # line feature
            attr2 = None
    return (attr1, attr2)

def perimeterLength(geom, measure):
    value = 0.00
    if geom.isMultipart():
        poly = geom.asMultiPolygon()
        for k in poly:
           for j in k:
              value = value + measure.measureLine(j)
    else:
        poly = geom.asPolygon()
        for k in poly:
            value = value + measure.measureLine(k)
    return value

def addGeometryInformation(vlayer, onlySelected=False):
    """
    Inputs:
            vlayer = QgsVectorLayer
            onlySelected = bool
    Details:
          * 'vlayer' is the vector layer object that you wish to update
            geometry information on
          * 'onlySelected' specifies whether you want all features (False), 
            or only the selected features (True) to have their geometry 
            information updated
    Example:
            >>> mc = qgis.utils.iface.mapCanvas()
            >>> layer = mc.layer(0)
            >>> import add_geometry_information
            >>> add_geometry_information.addGeometryInformation(vlayer)
    Notes:
          * The above example works from the QGIS Python console, and assumes
            that the target layer in the first layer in the layer-list 
          * To import the module properly, make sure it is somewhere that 
            QGIS can find it, such as ~/.qgis/python
          * If the layer is in editing mode, then udpates can be 
            undone, otherwise, updates are written automatically to the provider
    """
    fieldNames = []
    calcStrings = []
    vectorType = vlayer.geometryType()
    if vectorType == QGis.Point:
        fieldNames = [QString("x_coord"), QString("y_coord")]
        calcStrings = [QString("$x"), QString("$y")]
    elif vectorType == QGis.Line:
        fieldNames = [QString("length")]
        calcStrings = [QString("$length")]
    elif vectorType == QGis.Polygon:
        fieldNames = [QString("area"), QString("perim")]
        calcStrings = [QString("$area"), QString("$perimeter")]
    else:
        print "Unknown vector layer geometry type."
        return

    calculationSuccess = True
    feature = QgsFeature()
    selectedIds = vlayer.selectedFeaturesIds()
    
    vlayer.blockSignals(True)
    wasEditing = vlayer.isEditable() # if it is editable, then we must be in edit mode
    if not wasEditing:
        vlayer.startEditing()
        if not vlayer.isEditable():
            print("Unable to edit input vector layer, please choose a layer "
                  "with edit capabilities, or use 'Add/Export geometry info' tool")
            return

    # block layerModified signals (that would trigger table update)
    attributeIds = []
    fieldMap = vlayer.pendingFields()
    fieldMap = dict([(field.name(), index) for index, field in fieldMap.iteritems()])
    for fieldName, calcString in zip(fieldNames, calcStrings):
        attributeId = -1
        if fieldName.toUpper() in fieldMap: # update existing uppercase field
            attributeId = fieldMap[fieldName.toUpper()]
        elif fieldName in fieldMap: # update existing lowercase field
            attributeId = fieldMap[fieldName]
        else: # create new field
            if not vlayer.dataProvider().capabilities() > 7: # can't add attributes
                print("Data provider does not support adding attributes: "
                      "Cannot add required geometry fields.")
                vlayer.rollBack()
                return False
            newField = QgsField(fieldName, QVariant.Double, "double", 10, 5)
            vlayer.beginEditCommand("Attribute added")
            if not vlayer.addAttribute(newField):
                print "Could not add the new field to the provider."
                vlayer.destroyEditCommand()
                if not wasEditing:
                    vlayer.rollBack()
                return False
            vlayer.endEditCommand()
            # get index of the new field
            fieldMap = vlayer.pendingFields()
            fieldMap = dict([(field.name(), index) for index, field in fieldMap.iteritems()])
            if not fieldName in fieldMap:
                print "Could not find the newly created field."
                if not wasEditing:
                    vlayer.rollBack()
                return False
            attributeId = fieldMap[fieldName]
        if attributeId == -1:
            print "Error writing to the geometry field."
            if not wasEditing:
                vlayer.rollBack()
            return False
        attributeIds.append(attributeId)
    rownum = 1
    vlayer.select(vlayer.pendingAllAttributesList(), QgsRectangle(), True, False)
    vlayer.beginEditCommand("Geometry info added")
    try:
        while vlayer.nextFeature(feature):
            if onlySelected: # should we only update the selected ones?
                if not feature.id() in selectedIds:
                    continue # skip this one...
            geom = QgsGeometry(feature.geometry())
            attrs = geometryInformation(geom)
            # since there are only two, just do them both in order
            for i, id in enumerate(attributeIds):
                vlayer.changeAttributeValue(feature.id(), id, attrs[i], False)
        vlayer.endEditCommand()
    except Exception, err:
        print "An error occured while adding geometry information:\n%s" % str(err)
        if not wasEditing:
            vlayer.rollBack()
            return

    # stop blocking layerModified signals and make sure that one layerModified signal is emitted
    vlayer.blockSignals(False)
    vlayer.setModified(True, False)

    if not wasEditing:
        vlayer.commitChanges()
    return True
    
def countFeaturesInPolygon(polygonLayer, inputLayer, onlySelected=False):
    feature = QgsFeature()
    selectedIds = polygonLayer.selectedFeaturesIds()
    if inputLayer.geometryType() == QGis.Point:
        fieldName = QString("pntcnt")
    elif inputLayer.geometryType() == QGis.Line:
        fieldName = QString("length")
    else:
        print "Invalid input layer type: Should be point or line layer"
        return False
    polygonLayer.blockSignals(True)
    wasEditing = polygonLayer.isEditable() # if it is editable, then we must be in edit mode
    if not wasEditing:
        polygonLayer.startEditing()
        if not polygonLayer.isEditable():
            print("Unable to edit input polygon layer: Please choose a layer with edit capabilities.")
            return
    if not inputLayer.crs() == polygonLayer.crs():
        print "Input layers have non-matching CRS: This may cause unexpected results."
    fieldMap = polygonLayer.pendingFields()
    fieldMap = dict([(field.name(), index) for index, field in fieldMap.iteritems()])
    attributeId = -1
    if fieldName.toUpper() in fieldMap: # update existing uppercase field
        attributeId = fieldMap[fieldName.toUpper()]
    elif fieldName in fieldMap: # update existing lowercase field
        attributeId = fieldMap[fieldName]
    else: # create new field
        if not polygonLayer.dataProvider().capabilities() > 7: # can't add attributes
            print("Data provider does not support adding attributes: "
                  "Cannot add required field.")
            if not wasEditing:
                polygonLayer.rollBack()
            return False
        if inputLayer.geometryType() == QGis.Point:
            newField = QgsField(fieldName, QVariant.Int, "integer")
        else: # if it's not a point, then it must be line otherwise we shouldn't be here
            newField = QgsField(fieldName, QVariant.Double, "double", 10, 5)
        polygonLayer.beginEditCommand("Attribute added")
        if not polygonLayer.addAttribute(newField):
            print "Could not add the new field to the polygon layer."
            polygonLayer.destroyEditCommand()
            if not wasEditing:
                polygonLayer.rollBack()
            return False
        polygonLayer.endEditCommand()
        # get index of the new field
        fieldMap = polygonLayer.pendingFields()
        fieldMap = dict([(field.name(), index) for index, field in fieldMap.iteritems()])
        if not fieldName in fieldMap:
            print "Could not find the newly created field."
            if not wasEditing:
                polygonLayer.rollBack()
            return False
        attributeId = fieldMap[fieldName]
    if attributeId == -1:
        print "Error writing to the new attribute."
        if not wasEditing:
            polygonLayer.rollBack()
        return False
    # create spatial index for faster querying later
    index = QgsSpatialIndex()
    inputLayer.select([], QgsRectangle(), True, False)
    while inputLayer.nextFeature(feature):
        index.insertFeature(feature)
    polygonLayer.select(polygonLayer.pendingAllAttributesList(), QgsRectangle(), True, False)
    polygonLayer.beginEditCommand("Count field udpated")
    inputFeature = QgsFeature()
    measure = QgsDistanceArea()
    geom = QgsGeometry()
    try:
        while polygonLayer.nextFeature(feature):
            if onlySelected: # should we only update the selected ones?
                if not feature.id() in selectedIds:
                    continue # skip this one...
            geom = QgsGeometry(feature.geometry())
            features = index.intersects(geom.boundingBox())
            count = 0.0
            for id in features:
                inputLayer.featureAtId(id, inputFeature, True)
                inputGeom = QgsGeometry(inputFeature.geometry())
                if inputLayer.geometryType() == QGis.Point:
                    if geom.contains(inputGeom.asPoint()):
                        count += 1
                else:
                    inputGeom = QgsGeometry(geom.intersection(inputGeom))
                    if not inputGeom.isGeosValid() or inputGeom.isGeosEmpty():
                        continue
                    count += measure.measure(inputGeom)
            polygonLayer.changeAttributeValue(feature.id(), attributeId, count, False)
        polygonLayer.endEditCommand()
    except Exception, err:
        print "An error occured while adding counts:\n%s" % str(err)
        if not wasEditing:
            polygonLayer.rollBack()
            return

    # stop blocking layerModified signals and make sure that one layerModified signal is emitted
    polygonLayer.blockSignals(False)
    polygonLayer.setModified(True, False)

    if not wasEditing:
        polygonLayer.commitChanges()
    return True
