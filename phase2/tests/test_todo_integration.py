from lib.todolist_challenge import *
from lib.todo_challenge import *

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