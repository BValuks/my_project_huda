class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.entry = f'{self.title}: {self.contents}'
        self.chunk_count = 0
    
    def word_count(self):
        # return len(self.title.split()) + len(self.contents.split())
        return len(self.entry.split())
    
    def reading_time(self, wpm):
        # return (len(self.title.split()) + len(self.contents.split())) // wpm
        return len(self.entry.split()) // wpm
    
    def reading_chunk(self, wpm, minutes):
        words_read = wpm * minutes
        entry_split = self.entry.split()
        starting_index = self.chunk_count * words_read
        output = entry_split[starting_index : starting_index + words_read]
        if len(output) < words_read or output == entry_split[-words_read:]:
            self.chunk_count = 0
        else:
            self.chunk_count += 1
        return ' '.join(output)