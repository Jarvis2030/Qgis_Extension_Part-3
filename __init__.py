# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Shapefile
                                 A QGIS plugin
 plugin to load shapefile
                             -------------------
#		begin                : 2020-01-13
#       copyright            : (C) Jarvis2030
#       email                : okomojacob2030@gmail.com
#       git source           : https://github.com/Jarvis2030/Qgis-Extension.git
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
    """Load Shapefile class from file Shapefile.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .display_shapefile import Shapefile
    return Shapefile(iface)
