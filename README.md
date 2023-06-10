# pysurprisal

[![version](https://badge.fury.io/py/pysurprisal.svg)](https://badge.fury.io/py/pysurprisal)
[![downloads](https://img.shields.io/pypi/dm/pysurprisal)](https://pypistats.org/packages/pysurprisal)
[![license](https://img.shields.io/pypi/l/pysurprisal)](https://github.com/capjamesg/pysurprisal/blob/main/LICENSE)
[![python-version](https://img.shields.io/pypi/pyversions/pysurprisal)](https://badge.fury.io/py/pysurprisal)

An implementation of surprisal in Python.

## Installation

```bash
pip install pysurprisal
```

## Usage

```python
from pysurprisal import Surprisal

text = "..."

# calculate surprisal for each word in the text
data = Surprisal(text)
surprisals = data.calculate_surprisals()

# get the top 10 most surprising words
top_k = data.get_top_k(10)

# print dictionary of all surprisals
# key = word, value = surprisal
print(surprisals.surprisals)
```

## Contributors

- capjamesg

## License

This project is licensed under an [MIT license](LICENSE.md).
