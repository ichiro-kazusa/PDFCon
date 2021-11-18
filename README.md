PDFCon
======================

PDFCon is a pdf manupilating tool with GUI. Powered by pikepdf/wxWidgets, requires python &ge; 3.8  .

This program now impelemts functions to concat/encrypt/decrypt PDF. It tested only on Windows.

![screenshot](https://user-images.githubusercontent.com/20105619/139176190-b6c960a7-67eb-46b2-96ba-36e9c703b811.png)

# Usage

## start with python command

If you have not use pipenv, install it.

```bash
pip install pipenv
```

Clone this repository, and move into repository folder which has Pipfile.
Then install related components.

```bash
pipenv install
```

Finally, you can run application via pipenv.

```bash
pipenv run python mainw.py
```

# Development
## TODO

PDF Backend
* refactor: use DI for create repository

## Future

Application
* split into single-page files
