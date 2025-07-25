import pytest

class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        wordList = wordList[::-1]
        return " ".join(wordList)

@pytest.mark.parametrize(
    "input_str,expected_output",
    [
        ("", ""),                                 # Empty string
        ("hello", "hello"),                       # Single word
        ("hello world", "world hello"),           # Two words
        ("  hello   world  ", "world hello"),     # Extra spaces
        ("a b c", "c b a"),                       # Multiple words
        ("  a  good   example ", "example good a"), # Leading/trailing/multiple spaces
        ("one", "one"),                           # Single word again
        ("Python is awesome", "awesome is Python"), # Regular sentence
    ]
)
def test_reverseWords(input_str, expected_output):
    assert Solution().reverseWords(input_str) == expected_output
