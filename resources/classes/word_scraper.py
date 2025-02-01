from typing import Set
from page import Page


# My application’s implementation: ### Anas Zughayyar ###

class word_scraper:
    def __init__(self, page_url: str, word: str):
        self.page_url = page_url
        self.word = word
        self.pages_set = Set[Page]
