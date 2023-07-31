import pytest
from lib.diary import *
from lib.diary_entry import *
from lib.todo_list import *
from lib.todo import *
from lib.phone_number_extractor import *
from lib.entry_selector import *

"""
Given a Diary
When we add two diary entries
We see the entries in the entry_list
"""
def test_add_entries_to_diary_added_to_entry_list():
    diary = Diary()
    entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Contact number: 02083619836')
    entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.entry_list == [entry1, entry2]

"""
Given a Diary
When we add two diary entries and use #all
We see a list of formatted diary entries
"""
def test_diary_all_method_returns_list_of_formatted_diary_entry():
    diary = Diary()
    entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Contact number: 02083619836')
    entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == ['1st Jan: John Doe| Meeting to discuss stock chain. Contact number: 02083619836', '2nd Jan: Jane Seymour| Meeting to discuss new clients. Contact number: 07926158773']

"""
Given a Diary
When we add two diary entries and use #count_words
We see a number representing the number of words in all the diary entries combines
"""
def test_diary_count_words_method_returns_number_of_words():
    diary = Diary()
    entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Contact number: 02083619836')
    entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 24

"""
Given a Diary
When we add two diary entries and use #list_numbers
We see a list of number contained within the diary entries with the names attached
"""
def test_diary_list_numbers_method_returns_list_of_numbers_with_names_attached():
    diary = Diary()
    entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Contact number: 02083619836')
    entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.list_numbers() == ['John Doe: 02083619836', 'Jane Seymour: 07926158773']

"""
Given a Diary
When we add two diary entries and use #list_numbers
We see a list of number contained within the diary entries and any numbers that don't match the criterea for a phone number, aren't returned
"""
def test_diary_list_numbers_method_returns_list_of_numbers_with_names_attached():
    diary = Diary()
    entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Contact number: 02083619836')
    entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Went out for her birthday. She turned 34 today!')
    entry3 = DiaryEntry('3nd Jan', 'Stephen Hawking', 'Stephen told me about a really big number today, 87539027645')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.list_numbers() == ['John Doe: 02083619836']

"""
Given a Diary
When we add two diary entries and use #best_entry_for_reading_time
We see a formatted string representing the longest diary entry the user can read in the allotted time
"""
def test_diary_best_entry_for_reading_time_returns_the_correct_entry():
    diary = Diary()
    entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Changes to be made. Contact number: 02083619836')
    entry2 = DiaryEntry('2nd Jan', 'Jack Smith', 'Meeting to discuss family. Contact number: 07926158773')
    entry2 = DiaryEntry('3rd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
    diary.add(entry1)
    diary.add(entry2)
    selector = EntrySelector()
    assert selector.best_entry_for_reading_time(7, 2, diary) == '3rd Jan: Jane Seymour| Meeting to discuss new clients. Contact number: 07926158773'

'''
Use #add and #incomplete on an instance of TodoList
Should add todos to class list and return a list 
'''
def test_add_method_on_todolist_should_list_todos_as_incomplete():
    todo_list = TodoList()
    task1 = Todo('Example task 1')
    task2 = Todo('Example task 2')
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.incomplete() == [task1, task2]

'''
Use #add on instance of TodoList, use #mark_complete on
instance of Todo, use #complete on instance of TodoList
Should return a list with the instance of Todo that has
been complete
'''
def test_complete_method_should_list_completed_todos():
    todo_list = TodoList()
    task1 = Todo('Example task 1')
    task2 = Todo('Example task 2')
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    assert task1.complete == True
    assert todo_list.complete() == [task1]
    assert todo_list.incomplete() == [task2]

'''
Use #give_up on instance of TodoList containg todos
Should mark all todos as complete
'''
def test_give_up_method_should_mark_all_todos_as_complete():
    todo_list = TodoList()
    task1 = Todo('Example task 1')
    task2 = Todo('Example task 2')
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == [task1, task2]