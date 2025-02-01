from typing import Set
from resources.classes.page import Page
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links_in_page(p: Page) -> Set[str]:
    """
    Extracts all the links from the given Page object's content.

    This function uses BeautifulSoup to parse the HTML content of the page
    and find all anchor tags with an 'href' attribute, collecting their URLs.

    Args:
        p (Page): An instance of Page containing the HTML content to parse.

    Returns:
        Set[str]: A set of unique URLs found in the page.

    Raises:
        ImportError: If BeautifulSoup is not installed or importable.
    """
    try:
        # Parse the HTML content of the page
        soup = BeautifulSoup(p.content, 'html.parser')

        # Find all 'a' tags with 'href' attribute
        links = soup.find_all('a', href=True)

        # Extract the URLs, ensuring we use absolute URLs
        extracted_links = set()
        for link in links:
            # Convert relative URLs to absolute URLs
            absolute_link = urljoin(p.url, link['href'])
            extracted_links.add(absolute_link)

        return extracted_links

    except ImportError:
        raise ImportError("BeautifulSoup is required for parsing HTML. Please install bs4: pip install bs4")