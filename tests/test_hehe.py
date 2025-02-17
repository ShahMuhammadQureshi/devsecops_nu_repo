import unittest
from unittest.mock import patch
import demo  # Ensure demo.py is in the same directory or properly importable

class TestDemo(unittest.TestCase):
    @patch('builtins.print')
    def test_output(self, mock_print):
        demo_output = hehe  # Execute the script
        mock_print.assert_called_once_with('Hello World')

if __name__ == '__main__':
    unittest.main()
