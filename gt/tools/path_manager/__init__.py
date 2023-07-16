"""
 GT Path Manager - A script for quickly re-pathing many elements in Maya.
 github.com/TrevisanGMW/gt-tools - 2020-08-26

 0.1 - 2020-08-26
 Created initial setup, added table and icons for file nodes

 1.0 - 2020-12-02
 Initial Release
 Added support for UDIMS and Image Sequences to the "file" node
 Added support for a lot of common nodes:
    audio, cacheFile, AlembicNode, BifMeshImportNode, gpuCache, MASH_Audio
 Added support for Arnold Lights
    aiPhotometricLight, aiStandIn, aiVolume
 Added support for Redshift Lights
    RedshiftProxyMesh, RedshiftVolumeShape, RedshiftNormalMap, RedshiftDomeLight, RedshiftIESLight
 Added support for Reference Files through OpenMaya API (Instead of PyMEL)

 1.1 - 2020-12-03
 Added support for Image Planes

 1.2 - 2021-05-11
 Made script compatible with Python 3 (Maya 2022+)

 1.2.1 to 1.2.3 - 2022-03-17 to 2022-08-17
 Fixed issue where error or found icons would look stretched (fixed size now)
 Organize the code and comments a bit better
 Changed to semantic versioning
 Removed unused imports
 Fixed "Refresh" button width
 Minor PEP8 Cleanup
 Aligned path to the left
 Added padding to table cells
"""


def launch_tool():
    """
    Launch user interface and create any necessary connections for the tool to function.
    Entry point for when using the tool GT Path Manager.
    """
    from gt.tools.path_manager import path_manager
    try:
        path_manager_dialog.close()
        path_manager_dialog.deleteLater()
    except Exception as exception:
        print(exception)
        pass
    path_manager.try_to_close_gt_path_manager()
    path_manager_dialog = path_manager.GTPathManagerDialog()
    path_manager_dialog.show()


if __name__ == "__main__":
    launch_tool()
