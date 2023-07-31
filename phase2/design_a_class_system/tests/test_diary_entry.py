from lib.diary_entry import *

"""
Given a DiaryEntry
It initialises with date, name, contents, entry and chunk_count
"""
def test_initialise_diary_entry():
    entry = DiaryEntry('Date1', 'Name1', 'Contents1')
    assert entry.date == 'Date1'
    assert entry.name == 'Name1'
    assert entry.contents == 'Contents1'
    assert entry.entry == 'Date1: Name1| Contents1'
    assert entry.chunk_count == 0

"""
Given a DiaryEntry
When using #word_count method, returns the number of word in the diary entry
"""
def test_diary_entry_word_count_method():
    entry = DiaryEntry('Date1', 'Name1', 'Contents1')
    assert entry.word_count() == 3