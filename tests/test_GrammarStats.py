from lib.GrammarStats import *

def test_GrammarStats():
    grammar_stats = GrammarStats()
    result1 = grammar_stats.check("How many apples are there?")
    assert result1 == True
    result2 = grammar_stats.percentage_good()
    assert result2 == 100