# COVID19 NSW Dashboard
COVID 19 NSW Dashboard written with Dash, Plotly and Heroku

## Setup
*Requires: Python 3.9*
- *https://linuxhint.com/install-python-3-9-linux-mint/ (linux)*
- *Windows 10 Store (windows)*

- Create a `venv` inside the repository `python3.9 -m venv venv`
- Activate the `venv` with `source venv/bin/activate` (Linux) or `venv\Scripts\activate.bat` (Windows)
- Install packages with `pip3.9 install -r requirements.txt` (linux) or `pip install -r requirements.txt` (windows)
- Confirm proper setup with `python3.9 app.py` or `python app.py`


## ChangeLog

#### 2020-03-09
- Major Refactor of Codebase
    - content.py is split into multiple files for each class and placed in a content module.
    - Most (all) methods in content classes are static methods
    - tabs.py is moved to a buttons module
    - Most modules are given an __init__.py file to clean up imports and linting

*Author: Duc Cong Duong*
