from lib.todolist_challenge import *

''' 
Initialise an instance of TodoList
Should be initialised with a blank list
'''
def test_initialise_todolist():
    todo_list = TodoList()
    assert todo_list.todo_list == []