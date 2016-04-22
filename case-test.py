#test module to test 'practice_case.py' using a Class

import practice_case
import unittest

class TestCaseChange(unittest.TestCase):
    def test_snake_to_camel(self):
        found = practice_case.snake_to_camel('case_matters')
        expected = 'CaseMatters'
        assert found == expected

    def test_camel_to_snake(self):
        found = practice_case.camel_to_snake('CaseMatters')
        expected = 'case_matters'
        assert found == expected