from lib.diary_2 import *

"""
When we initialise an instance of Diary
We should get an empty dictionary
"""
def test_initialise_instance_of_diary_contains_empty_dict():
    diary = Diary()
    assert diary.entry_list == []