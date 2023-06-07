# Surprisal 🎉

`pysurprisal` lets you calculate the surprisal for words in a corpus of text, useful in NLP analysis.

## What is surprisal? 🤔

Surprisal is a metric showing how "surprising" it is that a word appears in a corpus of text. The concept comes from information theory, and is also referred to as entropy.

More surprising words in a corpus of text have higher values.

You can use surprisal to find uncommon and "interesting" words in a corpus of text.

[linguist.link](https://linguist.link) uses `pysurprisal` to calculate surprisal for words in a corpus of New York Times articles.

## Installation 🛠️

You can install `pysurprisal` using `pip`:

```bash
pip install pysurprisal
```

## Quickstart 🚀

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