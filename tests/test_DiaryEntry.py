from lib.DiaryEntry import *

def test_Diary_entry():
    diary_entry =  DiaryEntry("My Title", "These are the contents of my diary entry.")
    result1 = diary_entry.format()
    assert result1 == "My Title : These are the contents of my diary entry."
    result2 = diary_entry.count_words()
    assert result2 == 8
    result3 = diary_entry.reading_time(200)
    assert result3 == 0.04
    result4 = diary_entry.reading_chunk(20,1)
    assert result4 == "These are the contents of my diary entry."

    
