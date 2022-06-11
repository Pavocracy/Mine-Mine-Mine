import sys
import os

def resource_path(relative_path):
    """This function is purely to get pyinstaller to embed game assets
    into the executable properly. This solution was found on stackoverflow.
    https://stackoverflow.com/questions/54210392/how-can-i-convert-pygame-to-exe
    """
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
