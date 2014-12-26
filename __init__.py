# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Crs_Id
                                 A QGIS plugin
 This plugin returns layer's epsg code
                             -------------------
        begin                : 2014-12-26
        copyright            : (C) 2014 by Giuseppe De Marco
        email                : demarco.giuseppe@gmail.com
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
    """Load Crs_Id class from file Crs_Id.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .crs_id import Crs_Id
    return Crs_Id(iface)
