from resources.classes.page import Page
import requests

def download_page(url: str) -> Page:
    """
    Downloads the content of a web page given its URL and returns a Page object.

    This function simulates fetching a web page via HTTP request and constructs
    a Page object with the content and URL. It handles basic error cases like
    connection errors or non-200 status codes.

    Args:
        url (str): The URL of the web page to download.

    Returns:
        Page: An instance of Page containing the HTML content and the URL.

    Raises:
        requests.RequestException: If there's an error during the HTTP request.
        ValueError: If the response status code is not 200 (OK).
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url, timeout=10)  # Timeout set to 10 seconds as an example

        # Check if the request was successful
        if response.status_code == 200:
            # Create and return a Page object with the content and URL
            return Page(content=response.text, url=url)
        else:
            # Raise an exception if the status code is not 200
            raise ValueError(f"Failed to download page. Status code: {response.status_code}")

    except requests.RequestException as e:
        # Handle any request-related exceptions
        raise requests.RequestException(f"An error occurred while downloading the page: {e}")