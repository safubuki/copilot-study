import unittest
from unittest.mock import patch
from io import StringIO
from src.ui import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.ui = UI()

    def test_display_menu(self):
        expected_output = "1. Add Task\n2. Display Tasks\n3. Delete Task\n4. Exit\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_menu()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_get_user_choice(self):
        user_input = "2"
        with patch('builtins.input', return_value=user_input):
            choice = self.ui.get_user_choice()
            self.assertEqual(choice, int(user_input))

    def test_invalid_choice(self):
        user_input = "5"
        expected_output = "Invalid choice. Please try again.\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', return_value=user_input):
                self.ui.invalid_choice()
                self.assertEqual(fake_out.getvalue(), expected_output)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()