from pix2tex.cli import LatexOCR
from PIL import ImageGrab
import rumps
import subprocess
import clipboard


class MenuBarApp(rumps.App):
    def __init__(self):
        super(MenuBarApp, self).__init__("latexocr", icon="icon.png", template=True)
        self.img = None
        self.model = LatexOCR()

    @rumps.clicked("Snap", key="M")
    def on_click(self, _):
        try:
            subprocess.check_call(["screencapture", "-c", "-i"])
            self.img = ImageGrab.grabclipboard()
            clipboard.copy(self.model(self.img))
        except subprocess.CalledProcessError:
            rumps.alert("Error: Failed to capture screen or access clipboard.")

        if self.img:
            self.img.close()


if __name__ == "__main__":
    app = MenuBarApp()
    app.run()
