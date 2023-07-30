"""
When we initialise an instance of Diary
We should get an empty dictionary
"""
diary = Diary()
diary.entry_list # => {}

"""
When we add two diary entries,
we get the entries back in the diary
entry list.
"""
diary = Diary()
entry1 = DiaryEntry("28th July","I had a good day")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.entry_list # => ["28th July: I had a good day",
"29th July: Today was also good"]

"""
When we call the all method on an instance of Diary,
we should get back a list of diary entries.
"""
diary = Diary()
entry1 = DiaryEntry("28th July","I had a good day")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.all() # =>
"28th July: I had a good day"
"29th July: Today was also good"

"""When we call the method count_words on an instance of
DiaryEntry we should get the number of words in all diary entries
"""
diary = Diary()
entry1 = DiaryEntry("28th July","I had a good day")
entry1.word_count() # => 7

"""When we call the method count_words on an instance of
Diary we should get the number of words in all diary entries
"""
diary = Diary()
entry1 = DiaryEntry("28th July","I had a good day")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.count_words() # => 13

"""When we call the reading time method on an instance of DiaryEntry we should get
the reading time if the user were to read that diary entry
"""
entry = DiaryEntry("28th July","I had good day")
entry.reading_time(3) # => 2

"""When we call the reading time method on an instance of Diary we should get
the reading time if the user were to read all diary entries
"""
diary = Diary()
entry1 = DiaryEntry("28th July","I had a good day")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.reading_time(13) # => 1

"""When we call #find_best_entry_for_reading_time, we
should get an instance of DiaryEntry representing the entry
that is closest to, but not over, the length that the user
could read in the minutes (minutes) they have given their
reading speed (wpm)
"""
diary = Diary()
entry1 = DiaryEntry("28th July","Good")
entry2 = DiaryEntry("29th July","Today was also good")
diary.add(entry1)
diary.add(entry2)
diary.find_best_entry_for_reading_time(4,1) # => 
"28th July: Good"

-----------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------

''' 
Initialise an instance of TodoList
Should be initialised with a blank list
''''
todo_list = TodoList()
todo_list.todo_list # => []

'''
Initialise an instance of Todo
Should initialise with a task and with a class property
'''
task = Todo('Walk the dog')
task.task # => 'Walk the dog'
task.complete # => False

'''
Use #add and #incomplete on an instance of TodoList
Should add todos to class list and return a list 
'''
todo_list = TodoList()
task1 = Todo('Example task 1')
task2 = Todo('Example task 2')
todo_list.add(task1)
todo_list.add(task2)
todo_list.incomplete() # => [task1, task2]

'''
Call #mark_complete on an instance of Todo
Should change the class property from False to True
'''
task = Todo('Charge my laptop')
task.mark_complete()
task.complete # => True

'''
Use #add on instance of TodoList, use #mark_complete on
instance of Todo, use #complete on instance of TodoList
Should return a list with the instance of Todo that has
been complete
'''
todo_list = TodoList()
task1 = Todo('Example task 1')
task2 = Todo('Example task 2')
todo_list.add(task1)
todo_list.add(task2)
task1.mark_complete()
task1.complete # => True
todo_list.complete() # => [task1]
todo_list.incomplete() # => [task2]

'''
Use #give_up on instance of TodoList containg todos
Should mark all todos as complete
'''
todo_list = TodoList()
task1 = Todo('Example task 1')
task2 = Todo('Example task 2')
todo_list.add(task1)
todo_list.add(task2)
todo_list.give_up
todo_list.complete() # => [task1, task2]
todo_list.incomplete() # => []