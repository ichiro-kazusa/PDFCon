PDFCon
======================

PDFCon is a pdf manupilating tool with GUI. Powered by pikepdf/wxWidgets, requires python &ge; 3.8  .

This program now impelemts functions to concat/extract/encrypt/decrypt PDF. It tested only on Windows.

![image](https://user-images.githubusercontent.com/20105619/142193290-f4161e91-5d20-4187-b8ee-51fd60bc4ec4.png)


# Usage
## start with binary package

Download binary package from [Release Page](https://github.com/ichiro-kazusa/PDFCon/releases). Now only on Windows x64.

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

Application
* renew: application icon renewal

PDF Backend
* refactor: use DI for create repository

## Future

Application
* split into single-page files
