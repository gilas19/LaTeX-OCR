from setuptools import setup
import sys
sys.setrecursionlimit(5000)

APP = ["latexocr.py"]
OPTIONS = {
    "iconfile": "icon.icns",
    "argv_emulation": True,
    "plist": {
        'CFBundleShortVersionString': '0.2.0',
        "LSUIElement": True,
    },
    "packages": ["rumps", "PIL", "pix2tex", "numpy", "scipy"],
}

setup(
    name="LatexOCR",
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
