from lib.todo import *

'''
Initialise an instance of Todo
Should initialise with a task and with a class property
'''
def test_inialise_todo():
    task = Todo('Walk the dog')
    assert task.task == 'Walk the dog'
    assert task.complete == False

'''
Call #mark_complete on an instance of Todo
Should change the class property from False to True
'''
def test_mark_complete_change_variable_to_true():
    task = Todo('Charge my laptop')
    task.mark_complete()
    assert task.complete == True