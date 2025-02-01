import unittest
from unittest.mock import MagicMock, patch
from resources.classes.word_scorer import WordScorer

class MainTest(unittest.TestCase):
    @patch('resources.classes.word_scorer.build_pages_set')
    @patch('resources.classes.word_scorer.count_word_occurrences')
    def test_get_word_score(self, mock_count_word_occurrences, mock_build_pages_set):
        # Given
        page_url = 'https://example.com'
        word = 'word'
        mock_pages = {MagicMock(content='This is a word test. The word appears here too.')}

        # Set up mock behavior
        mock_build_pages_set.return_value = mock_pages
        mock_count_word_occurrences.return_value = 2

        # When
        new_test = WordScorer(page_url, word)
        new_test.build_pages_set = mock_build_pages_set
        new_test.count_word_occurrences = mock_count_word_occurrences
        result = new_test.calculate_word_occurrences()

        # Then
        expected_occurrences = 2
        self.assertEqual(result, expected_occurrences, "The result does not match the expected number of occurrences")

if __name__ == '__main__':
    unittest.main()