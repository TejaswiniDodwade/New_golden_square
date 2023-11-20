# from lib.my_dairy import *

# def test_make_snippet_when_blank():
#    assert make_snippet("") == ""

# def test_make_snippet_for_5_word():
#    assert make_snippet("writing test case for dairy") == "writing test case for dairy"

# def test_make_snippet_more_than_5_word():
#    assert make_snippet("writing test case for my test dairy") == "writing test case for my..."

# test_make_snippet_when_blank()
# test_make_snippet_for_5_word()
# test_make_snippet_more_than_5_word()

from lib.my_dairy import *

def test_make_snippet():
    result1 = make_snippet("business studies is one of my fav subject")
    assert result1 == ("business studies is one of...")
    result2 = make_snippet("my fav colour is pink")
    assert result2 == ("my fav colour is pink")
    