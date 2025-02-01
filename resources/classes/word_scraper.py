from resources.functions.build_pages_set import build_pages_set
from resources.functions.word_total_occurencies import word_total_occurrences


# My application’s implementation: ### Anas Zughayyar ###

class Scraper:
    def __init__(self, page_url: str, word: str):
        self.page_url = page_url
        self.word = word
        self.pages_set = build_pages_set(self.page_url)
        self.word_occurrences = word_total_occurrences(self.page_url, self.word)
