class EntrySelector():
    def __init__(self):
        pass

    def best_entry_for_reading_time(self, wpm, minutes, diary):
        words_to_be_read = wpm * minutes
        suitable_entry_list = [entry.entry for entry in diary.entry_list if entry.word_count() <= words_to_be_read]
        sorted_list = sorted(suitable_entry_list, reverse=True)
        return sorted_list[0]