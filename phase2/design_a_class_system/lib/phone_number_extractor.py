class PhoneNumberExtractor():
    def __init__(self):
        pass

    def list_numbers(self, entry_list):
        phone_number_list = []
        for entry in entry_list:
            for word in entry.entry.split():
                if word.isdigit() and len(word) == 11 and word[0] == '0':
                    phone_number_list.append(f'{entry.name}: {word}')
        return phone_number_list