# Surprisal

An implementation of surprisal in Python.

## Installation

```bash
pip install surprisal
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