from diary_entry_2 import *

class Diary():
    def __init__(self):
        self.entry_list = []
    
    def add(self, diary_entry):
        self.entry_list.append(diary_entry.entry)
    
    def all(self):
        for entry in self.entry_list:
            print(f'* {entry}')
    
    def count_words(self):
        count = 0
        for entry in self.entry_list:
            count += len(entry.split())
        return count
    
    def reading_time(self, wpm):
        return self.count_words() // wpm
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_to_be_read = wpm * minutes
        suitable_entry_list = [entry for entry in self.entry_list if len(entry.split()) <= words_to_be_read]
        sorted_list = sorted(suitable_entry_list, reverse=True)
        return sorted_list[0]