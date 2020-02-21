"""
Testing Tweets Preprocessor
"""
import unittest
from twitter_preprocessor import TwitterPreprocessor
from test_case_generator import TestCasesGenerator

class Tests(unittest.TestCase):
    """define testing class"""

    def setUp(self):
        return

    def test_clean_text(self):
        """testing cleaning"""
        for test_case in getattr(TestCasesGenerator, 'clean'):
            tweet = TwitterPreprocessor(test_case['case'])
            tweet.clean_text()
            result = tweet.text
            expected_result = test_case['expected']
            self.assertEqual(result, expected_result)


    def test_tokenize_text(self):
        """testing tokenizing"""
        for test_case in getattr(TestCasesGenerator, 'tokenize'):
            tweet = TwitterPreprocessor(test_case['case'])
            tweet.tokenize_text()
            result = tweet.text
            expected_result = test_case['expected']
            self.assertEqual(result, expected_result)

    def test_replace_token_with_index(self):
        """testing indexing"""
        for test_case in getattr(TestCasesGenerator, 'index'):
            tweet = TwitterPreprocessor(test_case['case'])
            tweet.replace_token_with_index()
            result = tweet.text
            expected_result = test_case['expected']
            self.assertEqual(result, expected_result)

    def test_pad_sequence(self):
        """testing pad sequence"""
        for test_case in getattr(TestCasesGenerator, 'padding'):
            tweet = TwitterPreprocessor(test_case['case'])
            tweet.pad_sequence()
            result = tweet.text
            expected_result = test_case['expected']
            self.assertEqual(result, expected_result)

    def test_preprocessing(self):
        """testing end to end preprocessing"""
        for test_case in getattr(TestCasesGenerator, 'preprocessing'):
            tweet = TwitterPreprocessor(test_case['case'])
            tweet.preprocessing()
            result = tweet.text
            expected_result = test_case['expected']
            self.assertEqual(result, expected_result)

