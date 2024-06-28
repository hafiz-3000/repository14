# Harmon Tech Unit Test
# Python

import unittest

class TestCharacterCount(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(f(""), {})

    def test_single_character(self):
        self.assertEqual(f("a"), {'a': 1})
        
    def test_multiple_characters(self):
        self.assertEqual(f("abc"), {'a': 1, 'b': 1, 'c': 1})
        
    def test_repeated_characters(self):
        self.assertEqual(f("aabbcc"), {'a': 2, 'b': 2, 'c': 2})
        
    def test_mixed_characters(self):
        self.assertEqual(f("aabcc"), {'a': 2, 'b': 1, 'c': 2})
        
    def test_case_sensitivity(self):
        self.assertEqual(f("aA"), {'a': 1, 'A': 1})
        
    def test_special_characters(self):
        self.assertEqual(f("a!@#a"), {'a': 2, '!': 1, '@': 1, '#': 1})

if __name__ == "__main__":
    unittest.main()
