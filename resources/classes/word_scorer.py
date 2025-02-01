from resources.functions.build_pages_set import build_pages_set
from resources.functions.word_total_occurencies import word_total_occurrences


# My application’s implementation: ### Anas Zughayyar ###

# WordScorer class is used to carry word and url information for each user input
class WordScorer:
    def __init__(self, page_url: str, word: str):
        self.page_url = page_url
        self.word = word
        self.pages_set = None
        self.word_occurrences = None

    def build_pages_set(self):
        if self.pages_set is None:
            self.pages_set = build_pages_set(self.page_url)
        return self.pages_set

    def calculate_word_occurrences(self):
        if self.word_occurrences is None:
            self.word_occurrences = word_total_occurrences(self.page_url, self.word)
        return self.word_occurrences