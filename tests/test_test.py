import unittest
from unittest.mock import patch
import test  # Ensure test.py is in the same directory or properly importable

class TestTestScript(unittest.TestCase):
    @patch('builtins.print')
    def test_output(self, mock_print):
        test_output = test  # Execute the script
        expected_calls = [unittest.mock.call('Hi there'), unittest.mock.call(10)]
        mock_print.assert_has_calls(expected_calls)

if __name__ == '__main__':
    unittest.main()
