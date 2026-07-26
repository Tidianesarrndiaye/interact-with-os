# Reading and Writing CSV Files

## Module Contents

The `csv` module is a built-in Python module used to read and write CSV files. It provides a few core helpers:

- `csv.reader`: returns an iterator that reads rows from a CSV file.
- `csv.writer`: returns an object that converts data into delimited strings and writes them to a file-like object.
- `csv.DictReader`: works like a regular reader, but maps each row to a dictionary using the field names from the first row or the optional `fieldnames` parameter.

## Dialects and Formatting Parameters

Dialects define how a CSV file is structured. They control how the `csv` reader and writer behave.

Common dialect attributes include:

- `Dialect.delimiter`: a one-character string used to separate fields. The default is a comma.
- `Dialect.quotechar`: a one-character string used to quote fields containing special characters. The default is `"`.
- `Dialect.strict`: when set to `True`, the module raises `csv.Error` if it detects malformed input. The default is `False`.

## Reader Objects

A reader object exposes public methods and attributes such as:

- `reader.__next__()`: returns the next row from the iterator as a list. In practice, this is usually called with `next(reader)`.
- `reader.dialect`: a read-only description of the dialect currently used by the parser.

## Writer Objects

Writer objects let you write data to a CSV file. Useful methods and attributes include:

- `writer.writerows(rows)`: writes all rows from an iterable to the file object using the current dialect.
- `writer.dialect`: a read-only description of the dialect used by the writer.

## Key Takeaways

If you have not worked with CSV files yet, the `csv` module is a good place to start. Learning the reader and writer objects will help you work more efficiently with tabular data. The module also provides additional options for controlling formatting, parsing, and error handling.

## Resources for More Information

- [csv — CSV File Reading and Writing — Python 3.14.6 documentation](https://docs.python.org/3/library/csv.html)
- [Real Python: Python CSV](https://realpython.com/python-csv/)