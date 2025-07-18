import random
import types
import pytest
from collections import Counter
from typing import List

# ----------  Solution under test  ----------
class Solution:
    def __init__(self, w: List[int]):
        self.weights = []
        prefix = 0
        for weight in w:
            prefix += weight
            self.weights.append(prefix)

    def pickIndex(self) -> int:
        idx = random.randint(1, self.weights[-1])
        left, right = 0, len(self.weights)
        while left < right:
            mid = (left + right) // 2
            if self.weights[mid] < idx:
                left = mid + 1
            else:
                right = mid
        return left
# ------------------------------------------


# ----------  Helper for deterministic randint  ----------
class FakeRandInt:
    """
    Cycles through a predefined sequence of integers to make
    pickIndex deterministic in unit tests.
    """
    def __init__(self, sequence):
        self.seq = list(sequence)
        self.i = 0

    def __call__(self, a, b):
        assert a == 1 and b >= 1, "Unexpected randint range"
        val = self.seq[self.i % len(self.seq)]
        self.i += 1
        return val
# ---------------------------------------------------------


# ----------  Deterministic unit tests  ----------
@pytest.mark.parametrize(
    "weights, randvals, expected_indices",
    [
        # Single element – should always return 0
        ([10], [1, 1, 1], [0, 0, 0]),

        # Two elements: prefix = [1, 4]
        # randint=1  → idx 0
        # randint=2,3,4 → idx 1
        ([1, 3], [1, 2, 4], [0, 1, 1]),

        # Three elements: prefix = [2, 5, 9]
        # randint=2 → 0; randint=3 → 1; randint=8 → 2
        ([2, 3, 4], [2, 3, 8], [0, 1, 2]),
    ],
)
def test_pick_index_deterministic(monkeypatch, weights, randvals, expected_indices):
    """Ensure pickIndex maps exact randint outputs to correct indices."""
    solution = Solution(weights)

    fake_rand = FakeRandInt(randvals)
    monkeypatch.setattr(random, "randint", fake_rand)

    results = [solution.pickIndex() for _ in randvals]
    assert results == expected_indices
# ---------------------------------------------------------


# ----------  Statistical sanity check  ----------
def test_pick_index_distribution():
    """
    With a fixed random seed and large sample, the empirical
    frequencies should roughly match the weights' ratios.
    """
    w = [1, 3, 2]               # probabilities 1/6, 3/6, 2/6
    expected = [1 / 6, 3 / 6, 2 / 6]
    trials = 60_000             # large enough for law of large numbers

    random.seed(42)
    sol = Solution(w)
    counts = Counter(sol.pickIndex() for _ in range(trials))
    freqs = [counts[i] / trials for i in range(len(w))]

    # Allow ±2 % absolute error
    for f, p in zip(freqs, expected):
        assert abs(f - p) < 0.02
# ---------------------------------------------------------
