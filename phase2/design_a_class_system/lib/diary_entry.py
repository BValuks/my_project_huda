class DiaryEntry():
    def __init__(self, date, name, contents):
        self.date = date
        self.name = name
        self.contents = contents
        self.entry = f'{date}: {name}| {contents}'
        self.chunk_count = 0
    
    def word_count(self):
        return len(self.entry.split())