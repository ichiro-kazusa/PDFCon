PDFCon
======================

# Usage

If you have not use pipenv, install it.

```bash
pip install pipenv
```

Clone this repository, and move into repository folder which has Pipfile.
Then run `pipenv install`

```bash
pipenv install
```

Finally, you can run application via pipenv.

```bash
pipenv run python src/mainw.py
```


# Release Notes

## v0.0.4

Application
* new: encryption

PDF Backend
* refactor: log system
* enhance: unit test
* enhance: change pdf engine to pikepdf from pymupdf.
* enhance: read check for file content is really pdf.

## v0.0.3

GUI
* new: add decrypt panel
* new: autofill for decrypt destination
* enhanced: execute button is centerized

PDF Backend
* new: decrypt implemented with pymupdf
* enhance: concat implementation is now with pymupdf
* del: it does not use PyPDF2 anymore.
* fix: close source file
* fix: error handling when source failed to open
* refactor: rewrite file open with 'with' statement

## v0.0.2

Application
* new: display version information

GUI 
* new: File Drag & Drop for concat source list
* new: keyboard operations for concat source list
  * Ctrl+A, DEL, ALT+UP, ALT+DOWN, ALT+HOME, ALT+END
* fix: concat source move error when nothing selected

PDF Backend
* refactor: PdfSrcFile and similar objects make not be file object.

## v0.0.1
* concat implemented

# Development
## TODO

Application
* new: extract pages

PDF Backend
* refactor: use DI for create repository

## Future

Application
* extract pages to single file
* split into single-page files
