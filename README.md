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

dump_json(obj, filepath, encoding=None, errors=None, indent=4,
          skipkeys=False, ensure_ascii=False, separators=None,
          sort_keys=False)
    
to_csv(dataset, filepath, dictionary=False, fieldnames=[], header=True,
       mode="a", encoding=None, errors=None, newline='', dialect='excel',
       **kwargs)

read_csv(filepath, dictionary=False, fieldnames=None, header=True, mode="r",
         encoding=None, errors=None, newline='', dialect='excel', **kwargs):

get(url, sleep_time=30, max_try=5, trials=0, **requests_kwargs)

post(url, sleep_time=30, max_try=5, trials=0, **requests_kwargs)
```
