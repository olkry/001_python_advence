import unittest

from get_social_status import get_social_status


class TestSocialAge(unittest.TestCase):

    def test_can_get_child_age(self):
        age = 8
        correct_answer = 'ребенок'
        function_answer = get_social_status(age)
        self.assertEqual(correct_answer, function_answer)

    def test_can_get_teenager_age(self):
        age = 16
        correct_answer = 'подросток'
        function_answer = get_social_status(age)
        self.assertEqual(correct_answer, function_answer)

    def test_can_get_adult_age(self):
        age = 35
        correct_answer = 'взрослый'
        function_answer = get_social_status(age)
        self.assertEqual(correct_answer, function_answer)

    def test_can_get_pre_old_age(self):
        age = 60
        correct_answer = 'пожилой'
        function_answer = get_social_status(age)
        self.assertEqual(correct_answer, function_answer)

    def test_can_get_old_age(self):
        age = 128
        correct_answer = 'пенсионер'
        function_answer = get_social_status(age)
        self.assertEqual(correct_answer, function_answer)

    def test_cannot_pass_str_as_age(self):
        age = 'old'
        with self.assertRaises(ValueError):
            get_social_status(age)
