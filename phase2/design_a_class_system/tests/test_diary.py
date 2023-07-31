from lib.diary import *

"""
Given a Diary
It initialises with an empty list
"""
def test_initialise_diary_with_empty_string():
    diary = Diary()
    assert diary.entry_list == []