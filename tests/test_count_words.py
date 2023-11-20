from lib.count_words import *

def test_count_words():
    result = count_words("My fav song") 
    assert result == 3
    