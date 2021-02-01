import unittest
from unittest.mock import patch
from services.user_input_handler import UserInputHandler


class TestUserInputHandler(unittest.TestCase):

    @patch('builtins.input', lambda *args: '1')
    def test_choose_page_number(self):
        """

        :return:
        """
        self.assertEqual(UserInputHandler.choose_page_number(), '1')
