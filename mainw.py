from src.pdfui.mainapp import MainApp
from src.info import APPNAME, VERSION


if __name__ == '__main__':

    app = MainApp(title=f'{APPNAME} v{VERSION}')
    app.start_main_loop()
