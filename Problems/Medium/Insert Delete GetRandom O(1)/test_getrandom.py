import pytest
import random

class RandomizedSet:
    def __init__(self):
        self.valueindex = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.valueindex:
            return False
        self.valueindex[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueindex:
            return False
        last_element, remove_idx = self.values[-1], self.valueindex[val]
        self.values[remove_idx], self.valueindex[last_element] = last_element, remove_idx
        del self.valueindex[val]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


@pytest.mark.parametrize("ops, args, expected", [
    # Test basic flow: insert, remove, insert same again
    (["insert", "remove", "insert", "getRandom"],
     [[1], [1], [1], []],
     [True, True, True, 1]),

    # Test removing non-existent
    (["insert", "insert", "remove", "remove"],
     [[1], [2], [3], [2]],
     [True, True, False, True]),

    # Test inserting duplicates
    (["insert", "insert"],
     [[5], [5]],
     [True, False]),

    # Test remove and re-insert
    (["insert", "remove", "insert"],
     [[7], [7], [7]],
     [True, True, True]),

    # Test getRandom from multiple values
    (["insert", "insert", "insert", "getRandom"],
     [[10], [20], [30], []],
     [True, True, True, "one_of:10,20,30"]),
])
def test_randomized_set(ops, args, expected):
    rs = RandomizedSet()
    for i, op in enumerate(ops):
        if op == "insert":
            assert rs.insert(args[i][0]) == expected[i]
        elif op == "remove":
            assert rs.remove(args[i][0]) == expected[i]
        elif op == "getRandom":
            result = rs.getRandom()
            if isinstance(expected[i], str) and expected[i].startswith("one_of:"):
                valid = list(map(int, expected[i].split(":")[1].split(",")))
                assert result in valid
            else:
                assert result == expected[i]
