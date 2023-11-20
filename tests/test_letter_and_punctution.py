from lib.letter_and_punctution import *

def test_letter_and_punctution():
    result1 = letter_and_punctution("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.")
    assert result1 is True
    result2 = letter_and_punctution("today we have a lot of programming languages")
    assert result2 is False