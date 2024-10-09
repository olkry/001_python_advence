import unittest
import datetime
from calendar import weekday

from block_003_tests.hello_world_with_day import app

day_to_world_map = {
    0: 'Хорошего понедельника',
    1: ' Хорошего вторника',
    2: 'Хорошей среды',
    3: 'Хорошего четверга',
    4: 'Хорошей пятницы',
    5: 'Хорошей субботы',
    6: 'Хорошего воскресенья',
}


class TestHelloWorldWithDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def _get_weekday(self):
        current_day = datetime.datetime.today().weekday()
        return day_to_world_map[current_day]

    def test_can_get_correct_weekday(self):
        username= 'some'
        weekday = self._get_weekday()
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)
