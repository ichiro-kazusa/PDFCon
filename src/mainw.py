import os
import sys
from pdfui.mainapp import MainApp
from info import APPNAME, VERSION


if __name__ == '__main__':

    # stderr suppression
    devnul = open(os.devnull, 'w')
    sys.stderr = devnul

    app = MainApp(title=f'{APPNAME} v{VERSION}')
    app.start_main_loop()
