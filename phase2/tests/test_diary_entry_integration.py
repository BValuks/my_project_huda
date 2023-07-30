from lib.diary_2 import *
from lib.diary_entry_2 import *

def test_add_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry('28th July', 'Today is good')
    diary.add(diary_entry)
    assert diary.entry_list == ['28th July: Today is good']
    diary_entry2 = DiaryEntry('29th July', 'Today was also good')
    diary.add(diary_entry2)
    assert diary.entry_list == ['28th July: Today is good', '29th July: Today was also good']

"""
When we add two diary entries,
we get the entries back in the diary
entry list.
"""

def test_get_list_of_entries():
    diary = Diary()
    entry1 = DiaryEntry("28th July","I had a good day")
    entry2 = DiaryEntry("29th July","Today was also good")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.entry_list == ["28th July: I had a good day", "29th July: Today was also good"]

"""When we call the method count_words on an instance of
Diary we should get the number of words in all diary entries
"""
def test_word_count_method_on_instance_of_diary_class():
    diary = Diary()
    entry1 = DiaryEntry("28th July","I had a good day")
    entry2 = DiaryEntry("29th July","Today was also good")
    diary.add(entry1)
    assert diary.count_words() == 7
    diary.add(entry2)
    assert diary.count_words() == 13

    """When we call the reading time method on an instance of Diary we should get
the reading time if the user were to read all diary entries
"""
def test_reading_time_method_on_instance_of_diary_class():
    diary = Diary()
    entry1 = DiaryEntry("28th July","I had good day")
    entry2 = DiaryEntry("29th July","Today was also good")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(4) == 3
    entry3 = DiaryEntry("30th July","I had yet another good day")
    diary.add(entry3)
    assert diary.reading_time(4) == 5
    assert diary.reading_time(5) == 4

"""When we call #find_best_entry_for_reading_time, we
should get an instance of DiaryEntry representing the entry
that is closest to, but not over, the length that the user
could read in the minutes (minutes) they have given their
reading speed (wpm)
"""
def test_find_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("28th July","Good")
    entry2 = DiaryEntry("29th July","Today was also good")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(4,1) == "28th July: Good"