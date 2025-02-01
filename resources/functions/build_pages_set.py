
# implement the build_pages_set function that returns a set of all pages to be visited.
from queue import Queue
from typing import Set
from resources.classes.page import Page
from resources.functions.download_page import download_page
from resources.functions.get_links_in_page import get_links_in_page
import logging

def build_pages_set(start_url: str, depth: int = 2) -> Set[Page]:
    visited = set()  # Track visited URLs to avoid redundant processing
    queue = Queue()  # Queue for breadth-first traversal
    queue.put((start_url, 0))  # Tuple with URL and current depth
    pages = set()

    while not queue.empty():
        url, current_depth = queue.get()
        if url in visited or current_depth > depth:
            continue  # Skip already visited URLs or exceed depth limit

        try:
            page = download_page(url)  # Download the page
        except Exception as e:
            logging.error(f"Failed to download {url}: {e}")
            continue

        visited.add(url)
        pages.add(page)

        if current_depth < depth:
            links = get_links_in_page(page)  # Extract links from the page
            for link in links:
                if link not in visited:
                    queue.put((link, current_depth + 1))

    return pages

# Depth Issue:
# The function uses a breadth-first search approach, limited by a depth parameter (default=2).
# This prevents excessive crawling and limits resource usage while maintaining efficiency.
