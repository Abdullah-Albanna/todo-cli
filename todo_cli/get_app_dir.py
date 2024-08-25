import sys
import os
from functools import cache

@cache
def getCurrentFolderName():
    # get the path of the current .py file
    current_file_path = os.path.abspath(__file__)

    # get the directory name of the current script
    current_folder_path = os.path.dirname(current_file_path)

    # get the folder name
    folder_name = os.path.basename(current_folder_path)

    return folder_name

@cache
def getAppDirectory() -> str:
    """
    Gets the script or the
    executable path
    """
    if getattr(sys, "frozen", False):
        # Running in a nuitka build
        bundle_dir = os.path.dirname(sys.executable)
    else:
        # Running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    
    bundle_dir = bundle_dir[: -len(getCurrentFolderName())]

    return bundle_dir
