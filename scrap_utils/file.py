import csv
import json


def load_json(filepath, encoding=None, errors=None, parse_float=None,
              parse_int=None, parse_constant=None):
    """
    Load json from file.

    Open file with `open()` function and load data with `json.load()`.

    Parameters
    ----------
    filepath: str
        The json filepath to load.
    encoding: str, optional
        The name of the encoding used to decode or encode the file.
        Default is whatever `locale.getpreferredencoding()` returns.
        `List of standand encoding
        <https://docs.python.org/3/library/codecs.html#standard-encodings>`_.
    errors: str, default None
        Specifies how encoding and decoding error should be handled
        The standard names include [1]_: `strict`, `ignore`, `replace`,
        `surrogateescape`, `xmlcharrefreplace`, `backslashreplace`,
        `namereplace`.
    parse_float: datatype, optional
        It will be called with the string of every JSON float to be decoded.
        Default is equivalent to `float(num_str)`.
        Example of another datatype that can be used is `decimal.Demimal`.
    parse_int: datatype, optional
        It will be called with the string of every JSON int to be decoded.
        Default is equivalent to `int(num_str)`.
        Example of another datatype that can be used is `float`.
    parse_constant [2]_: datatype, optional
        It will be called with one of the following strings:
        `'-Infinity'`, `'Infinity'`, `'NaN'`.

    Returns
    -------
    obj: python object
        A python object from the json using this `conversion table
        <https://docs.python.org/3/library/json.html#json-to-py-table>`_.

    References
    ----------
    .. [1] `open() documentation
        <https://docs.python.org/3/library/functions.html#open>`_
    .. [2] `json.load() documentation
        <https://docs.python.org/3/library/json.html#json.load>`_
    """
    with open(filepath, 'r', encoding=encoding, errors=errors) as file:
        obj = json.load(file, parse_float=parse_float, parse_int=parse_int,
                        parse_constant=parse_constant)
    return obj


def dump_json(obj, filepath, encoding=None, errors=None, indent=4,
              skipkeys=False, ensure_ascii=False, separators=None,
              sort_keys=False):
    """
    Dump json into filepath.

    Open file with `open()` function and dump json with `json.dump()`.

    Parameters
    ----------
    obj: python object
        A python object to convert to json using this `conversion table
        <https://docs.python.org/3/library/json.html#py-to-json-table>`_.
    filepath: str
        filepath to save the json.
    encoding: str, optional
        The name of the encoding used to decode or encode the file.
        Default is whatever `locale.getpreferredencoding()` returns.
        `List of standand encoding
        <https://docs.python.org/3/library/codecs.html#standard-encodings>`_.
    errors: str, default None
        Specifies how encoding and decoding error should be handled
        The standard names include [1]_: `strict`, `ignore`, `replace`,
        `surrogateescape`, `xmlcharrefreplace`, `backslashreplace`,
        `namereplace`.
    indent: int, default 4
        A positive integer indicates the number of spaces to indent levels.
    skipkeys: bool, default False
        If `True`, dict keys that are not of a basic type
        (str, int, float, bool, None) will be skipped
        instead of raising a TypeError.
    ensure_ascii: bool, default True
        If ensure_ascii is `True`, the output is
        guaranteed to have all incoming non-ASCII characters escaped.
        If ensure_ascii is `False`, these characters will be output as-is.
    seperators: (item_separator, key_separator) tuple, default `(', ', ': ')`
        A tuple of 2 strings, item seperator & key seperator.
        To eliminate space and make json compact, use `(',', ':')`
        and set `indent` to `None`.
    sort_keys: bool, optional
        If sort_keys is `True` (default: `False`),
        then the output of dictionaries will be sorted by key.

    Returns
    -------
    None

    References
    ----------
    .. [1] `open() documentation
        <https://docs.python.org/3/library/functions.html#open>`_
    .. [2] `json.dump() documentation
        <https://docs.python.org/3/library/json.html#json.dump>`_
    """
    with open(filepath, 'w', encoding=encoding, errors=errors) as file:
        json.dump(
            obj, file, indent=indent, skipkeys=skipkeys,
            ensure_ascii=ensure_ascii, separators=separators,
            sort_keys=sort_keys
        )


def to_csv(dataset, filepath, mode="a", encoding=None, errors=None, newline='',
           header=True, dialect='excel', **fmtparams):
    """
    Save dataset to csv file.

    Open file with `open()` function and write with `csvwriter.writerows()`.

    Parameters
    ----------
    dataset: iterable[ of iterables]
        The dataset to save [3]_.
        If dataset is 1D e.g list, tuple, set,
        the csv would have a column.
        If dataset is 2D e.g list of list or list of tuple,
        the inner iterables would be row.
    filepath: str
        filepath to save dataset.
    mode: str, default 'a'
        Mode in which file is opened.
        Default is `'a'` which appends at the end of the file if it exists.
        Another good choice is `'w'` which replace old file first.
    encoding: str, optional
        The name of the encoding used to decode or encode the file.
        Default is whatever `locale.getpreferredencoding()` returns.
        `List of standand encoding
        <https://docs.python.org/3/library/codecs.html#standard-encodings>`_.
    errors: str, default None
        Specifies how encoding and decoding error should be handled
        The standard names include [1]_: `strict`, `ignore`, `replace`,
        `surrogateescape`, `xmlcharrefreplace`, `backslashreplace`,
        `namereplace`.
    newline: str, optional
        Default is `''` [1]_.
    header: bool, default True
        Should header or first row be included in the file?
        Default is True, include header or first row,
    dialect: string or subclass of `csv.Dialect
    <https://docs.python.org/3/library/csv.html#csv.Dialect>`_, optional
        Default is `'excel'`.
    **fmtparams: Dialects and formatting parameters, optional
        For full details see `Dialects and formatting parameters
        <https://docs.python.org/3/library/csv.html#csv-fmt-params>`

    Returns
    -------
    None

    References
    ----------
    .. [1] `open() documentation
        <https://docs.python.org/3/library/functions.html#open>`_
    .. [2] `csvwriter documentation
        <https://docs.python.org/3/library/csv.html#csv.writer>`_
    .. [3] `writer() method documentation
        <https://docs.python.org/3/library/csv.html#csv.csvwriter.writerows>`_
    """
    with open(filepath, mode=mode, encoding=encoding, errors=errors,
              newline=newline) as csvfile:
        writer = csv.writer(csvfile, dialect=dialect, **fmtparams)
        if header:
            writer.writerows(dataset)
        else:
            writer.writerows(dataset[1:])


def read_csv():
    pass
