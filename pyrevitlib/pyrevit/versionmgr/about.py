# -*- coding: utf-8 -*-
"""Utility module for pyRevit project information.

Examples:
        ```python
        from pyrevit.versionmgr import about
        a = about.get_pyrevit_about()
        a.subtitle
        ```
        'python RAD Environment for Autodesk Revit®'a.copyright'© 2014-2026 Ehsan Iran-Nejad'
"""

from collections import namedtuple


# FIXME: tuple attrs have duplicate docs
PyRevitAbout = namedtuple("PyRevitAbout", ["subtitle", "madein", "copyright"])
"""pyRevit project info tuple.

Attributes:
    subtitle (str): project subtitle
    madein (str): project made-in info
    copyright (str): project copyright info
"""


def get_pyrevit_about():
    """Return information about pyRevit project.

    Returns:
        (PyRevitAbout): pyRevit project info tuple
    """
    return PyRevitAbout(
        subtitle="BIM tools for Autodesk Revit®, built on pyRevit",
        madein="['pdx', 'hio', 'rno', 'sea']",
        copyright="BIMForge © 2026 · pyRevit © 2014-2026 Ehsan Iran-Nejad (GPL-3.0)",
    )
