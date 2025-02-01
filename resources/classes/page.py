
# Page Class to carry the page attributes for reusability
class Page:
    """A simple Page class to represent the downloaded HTML page."""
    def __init__(self, content: str, url: str):
        self.content = content
        self.url = url

# Assume the following functions are already implemented:

def download_page(url: str) -> Page:
    """The function returns an instance of a page object."""
    pass

def count_word_occurrences(p: Page, word: str) -> int:
    """The function counts word occurrences in the given page."""
    pass

def get_links_in_page(p: Page) -> set:
    """The function returns a set of links (strings) in the given page ."""
    pass