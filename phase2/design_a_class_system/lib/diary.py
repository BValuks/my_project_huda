from lib.phone_number_extractor import *
from lib.entry_selector import *

class Diary():
    def __init__(self):
        self.entry_list = []
        self.number_extractor = PhoneNumberExtractor()
    
    def add(self, diary_entry):
        self.entry_list.append(diary_entry)
    
    def all(self):
        return [entry.entry for entry in self.entry_list]
    
    def count_words(self):
        return sum([len(entry.entry.split()) for entry in self.entry_list])
    
    def list_numbers(self):
        return self.number_extractor.list_numbers(self.entry_list)