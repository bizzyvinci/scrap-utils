"""
============
Scrap Utils
============
This module provides some functions that might save you from repetition
in scraping projects.

Functions
---------
+-------------------+-----------------------------------------------+
| load_json         | Load json from file                           |
+-------------------+-----------------------------------------------+
| dump_json         | Dump json into filepath                       |
+-------------------+-----------------------------------------------+
| to_csv            | Save dataset to csv file                      |
+-------------------+-----------------------------------------------+
| read_csv          | Read dataset from csv file                      |
+-------------------+-----------------------------------------------+
| get               | Send a GET request with requests library      |
+-------------------+-----------------------------------------------+
| post              | Send a POST request with requests library     |
+-------------------+-----------------------------------------------+
"""

from .file import *
from .requests import *
