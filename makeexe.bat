set PYTHONUTF8=1
python -X utf8 -m nuitka --onefile --windows-console-mode=disable --include-module=wx --include-module=wx._xml --windows-icon-from-ico=appicon.ico --output-filename=pdfcon.exe mainw.py