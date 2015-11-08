# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AttributeSplit
                                 A QGIS plugin
 Split a layer by attribute values
                             -------------------
        begin                : 2015-11-06
        copyright            : (C) 2015 by Zoltan Siki
        email                : siki@agt.bme.hu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AttributeSplit class from file AttributeSplit.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .attribute_split import AttributeSplit
    return AttributeSplit(iface)
