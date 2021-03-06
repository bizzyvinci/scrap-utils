# Scrap Utils
This is small package that contains some code regularly repeated when scraping.

### To install
```python
pip install scrap-utils
```

### Sample code
```python
import scrap_utils as su

response = su.get("https://python.org")
len(response.text)
```


### It has the following functions:
```python
load_json(filepath, encoding=None, errors=None, parse_float=None,
	parse_int=None, parse_constant=None)

dump_json(data, filepath, encoding=None, errors=None, indent=4, skipkeys=False,
	ensure_ascii=False, separators=None, sort_keys=False)

to_csv(dataset, filepath, mode="a", encoding=None, errors=None, newline='',
	header=True, dialect='excel', **fmtparams)

get(url, sleep_time=30, max_try=5, trials=0, **requests_kwargs)

post(url, sleep_time=30, max_try=5, trials=0, **requests_kwargs)
```

### To-do list I'm considering:
* read_csv()
* other requests methods
* add unittest
* readthedoc documentation

#### Feel free to add your contribution [here](https://github.com/bizzyvinci/scrap-utils)