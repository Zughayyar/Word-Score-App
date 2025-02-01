import unittest
from unittest.mock import MagicMock, patch
from resources.classes.word_scorer import WordScorer

class WordScorerTest(unittest.TestCase):  # More descriptive class name

    @patch('resources.classes.word_scorer.build_pages_set')
    @patch('resources.classes.word_scorer.word_total_occurrences') # Patch word_total_occurrences
    def test_calculate_word_occurrences(self, mock_word_total_occurrences, mock_build_pages_set):
        # Given
        page_url = 'https://example.com'
        word = 'word'
        mock_page = MagicMock(content='This is a word test. The word appears here too.', url=page_url) # Mock page with URL
        mock_pages = {mock_page} # Set of mock pages

        # Set up mock behavior
        mock_build_pages_set.return_value = mock_pages
        mock_word_total_occurrences.return_value = 2  # Return the expected count

        # When
        word_scorer = WordScorer(page_url, word)  # Use more descriptive variable name
        word_scorer.build_pages_set() # Call the original method, but mock its internal function
        result = word_scorer.calculate_word_occurrences()

        # Then
        expected_occurrences = 2
        self.assertEqual(result, expected_occurrences, "The result does not match the expected number of occurrences")

        # Assertions to check if mocks were called correctly (Important!)
        mock_build_pages_set.assert_called_once_with(page_url)
        mock_word_total_occurrences.assert_called_once_with(page_url, word) # Check with correct args

        #Test for already computed value
        result2 = word_scorer.calculate_word_occurrences()
        self.assertEqual(result2, expected_occurrences, "The result does not match the expected number of occurrences")
        mock_word_total_occurrences.assert_called_once_with(page_url, word) # Check only called once

if __name__ == '__main__':
    unittest.main()