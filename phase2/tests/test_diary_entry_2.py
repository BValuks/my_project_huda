from lib.diary_entry_2 import *

def test_initialise_diary_entry():
    diary_entry = DiaryEntry('28th July', 'Today was good')
    assert diary_entry.title == '28th July'
    assert diary_entry.contents == 'Today was good'

"""When we call the method count_words on an instance of
DiaryEntry we should get the number of words in all diary entries
"""
def test_count_words_on_instance_of_diary_entry():
    entry1 = DiaryEntry("28th July","I had a good day")
    assert entry1.word_count() == 7

"""When we call the reading time method on an instance of DiaryEntry we should get
the reading time if the user were to read that diary entry
"""
def test_reading_time_on_instance_of_diary_entry():
    entry = DiaryEntry("28th July","I had good day")
    assert entry.reading_time(3) == 2

def test_reading_chunk_method_returns_first_chunk():
    entry = DiaryEntry("30th July","I had yet another good day. Very nice.")
    assert entry.reading_chunk(2, 2) == '30th July: I had'

def test_reading_chunk_method_returns_second_chunk_when_called_twice():
    entry = DiaryEntry("30th July","I had yet another good day. Very nice.")
    entry.reading_chunk(2, 2)
    assert entry.reading_chunk(2, 2) == 'yet another good day.'

def test_reading_chunk_method_returns_final_chunk_and_resets_count_to_zero():
    entry = DiaryEntry("30th July","I had yet another good day. Very nice.")
    entry.reading_chunk(2, 2)
    entry.reading_chunk(2, 2)
    assert entry.reading_chunk(2, 2) == 'Very nice.'
    assert entry.chunk_count == 0
    assert entry.reading_chunk(2, 4) == '30th July: I had yet another good day.'

def test_reading_chunk_method_returns_final_chunk_same_length_as_words_read_and_still_resets():
    entry = DiaryEntry("30th July","I had yet another good day. I feel very good.")
    entry.reading_chunk(2, 2)
    entry.reading_chunk(2, 2)
    assert entry.reading_chunk(2, 2) == 'I feel very good.'
    assert entry.chunk_count == 0
    assert entry.reading_chunk(2, 4) == '30th July: I had yet another good day.'