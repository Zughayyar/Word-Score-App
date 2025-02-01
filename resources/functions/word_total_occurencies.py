
# implement word_score_app that returns total occurrences using count_word_occurrences function
import concurrent.futures
from resources.functions.build_pages_set import build_pages_set
from resources.functions.count_word_occurrences import count_word_occurrences

def word_total_occurrences(start_url: str, word: str, depth: int = 2) -> int:
    pages = build_pages_set(start_url, depth)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(count_word_occurrences, page, word) for page in pages]
        total_occurrences = sum(f.result() for f in concurrent.futures.as_completed(futures))

    return total_occurrences  # Ensure the value is returned

# Depth Issue:
# The function uses a breadth-first search approach, limited by a depth parameter (default=2).
# This prevents excessive crawling and limits resource usage while maintaining efficiency.
