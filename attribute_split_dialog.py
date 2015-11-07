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
    def __init__(self, parent=None):
        """Constructor."""
        super(AttributeSplitDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def showEvent(self, event):
        self.LayerCombo.clear()  # remove previous entries
        self.BaseEdit.clear()  # clear textbox
        names = util.getLayerNames([QGis.Polygon, QGis.Line, QGis.Point])
        self.LayerCombo.addItems(names)
