class TodoList():
    def __init__(self):
        self.todo_list = []

    def add(self, task):
        self.todo_list.append(task)
    
    def incomplete(self):
        return [todo for todo in self.todo_list if todo.complete == False]
    
    def complete(self):
        return [todo for todo in self.todo_list if todo.complete == True]
    
    def give_up(self):
        for todo in self.todo_list:
            todo.mark_complete()
        return [todo for todo in self.todo_list if todo.complete == True]