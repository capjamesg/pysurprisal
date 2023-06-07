import math
from collections import Counter
from scipy.special import rel_entr

def compute_kl_divergence(p: dict, q: dict) -> float:
    """
    Compute the KL divergence between two probability distributions.

    Args:
        p (dict): The first probability distribution.
        q (dict): The second probability distribution.

    Returns:
        float: The KL divergence between the two probability distributions.

    Examples:
        >>> p = {"the": 0.5, "quick": 0.25, "brown": 0.25}
        >>> q = {"the": 0.25, "quick": 0.5, "brown": 0.25}
        >>> print(compute_kl_divergence(p, q))
        0.17328679513998632
    """
    return sum(rel_entr(p[word], q[word]) for word in p)

class Surprisal:
    """
    A statistical implementation of surprisal.
    """
    text: str
    counts: dict
    surprisals: dict
    probabilities: dict

    def __init__(self, text: str):
        self.text = text
        self.counts = self.get_word_frequencies(text)
        self.surprisals = {}
        self.probabilities = {}

    def get_word_frequencies(self, text: str) -> dict:
        """
        Get the word frequencies of a text.

        Args:
            text (str): The text to get the word frequencies of.

        Returns:
            dict: The word frequencies of the text.

        Examples:
            >>> text = "The quick brown fox jumps over the lazy dog."
            >>> surprisal = Surprisal(text)
            >>> print(surprisal.get_word_frequencies())
            {'the': 2, 'quick': 1, ...}
        """
        counts = Counter()

        for word in text.lower().split():
            counts[word] += 1

        return counts

    def calculate_surprisals(self, text: str = None) -> dict:
        """
        Calculate the surprisals for each word in a text.

        Args:
            text (str, optional): The text on which to calculate the surprisals. Defaults to None.

        Returns:
            dict: The surprisals for each word in the text.

        Examples:
            >>> text = "The quick brown fox jumps over the lazy dog."
            >>> surprisal = Surprisal(text)
            >>> print(surprisal.calculate_surprisals())
            {'the': 3.0910424533583156, 'quick': 3.784189633918261, 'brown': 3.784189633918261, 'fox': 3.784189633918261, 
            'jumps': 3.784189633918261, 'over': 3.784189633918261, 'lazy': 3.784189633918261, 'dog.': 3.784189633918261}
        """
        if text is None:
            text = self.text
            counts = self.counts
        else:
            counts = self.get_word_frequencies(text)

        surprisals = []
        surprisals_as_dict = {}
        probabilities = {}

        for word in counts:
            probabilities[word] = counts[word] / len(text)

            surprisals.append(-math.log(probabilities[word]))
            surprisals_as_dict[word] = -math.log(probabilities[word])

        self.surprisals = surprisals_as_dict

        return surprisals_as_dict

    def get_top_k_surprisals(self, k: int = 10) -> list:
        """
        Get the top k words in a text by surprisal.

        Args:
            k (int, optional): The number of words to return. Defaults to 10.

        Returns:
            list: The top k words in a text by surprisal.

        Examples:
            >>> text = "The quick brown fox jumps over the lazy dog."
            >>> surprisal = Surprisal(text)
            >>> surprisal.get_top_k_surprisals()
            ['the', 'over', 'lazy', 'fox', 'jumps', 'dog.', 'quick', 'brown']
        """
        if len(self.surprisals) == 0:
            self.calculate_surprisals()

        return sorted(self.surprisals, key=self.surprisals.get, reverse=True)[:k]
