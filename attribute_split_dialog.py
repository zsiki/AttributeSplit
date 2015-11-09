# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AttributeSplitDialog
                                 A QGIS plugin
 Split a layer by attribute values
                             -------------------
        begin                : 2015-11-06
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Zoltan Siki
        email                : siki@agt.bme.hu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from qgis.core import *  # get some constants
from qgis.utils import *  # get some utils
import util  # get my utility function

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'attribute_split_dialog_base.ui'))


class AttributeSplitDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, iface, parent=None):
        """Constructor."""
        super(AttributeSplitDialog, self).__init__(parent)
        self.iface = iface
        self.setupUi(self)
        # set event handler if layer selected
        self.LayerCombo.currentIndexChanged.connect(self.fillColumnNames)
        # set event handler for directory browser
        self.BrowseButton.clicked.connect(self.browse)

    def showEvent(self, event):
        """ initialize dialog

	    :param event: NOT USED
        """
        self.LayerCombo.clear()  # remove previous entries
        self.ColumnCombo.clear()
        self.BaseEdit.clear()    # clear textbox
        # fill layer name combo
        names = util.getLayerNames([QGis.Polygon, QGis.Line, QGis.Point])
        self.LayerCombo.addItems(names)
        # set active layer as default
        if iface.activeLayer():
            i = self.LayerCombo.findText(iface.activeLayer().name())
            if i > -1:
                self.LayerCombo.setCurrentIndex(i)

    def fillColumnNames(self):
        """ Fill column name combo from current layer
        """
        self.ColumnCombo.clear()
        lname = self.LayerCombo.currentText()
        if len(lname):
            vlayer = util.getMapLayerByName(lname)
            self.ColumnCombo.addItems(util.getFieldNames(vlayer, ["String", "Integer"]))

    def browse(self):
        """ select target directory
	"""
        self.DirectoryEdit.clear()
        dir = QtGui.QFileDialog.getExistingDirectory(self,
            "Select a folder", os.path.expanduser("~"),
            QtGui.QFileDialog.ShowDirsOnly)
	self.DirectoryEdit.setText(dir)