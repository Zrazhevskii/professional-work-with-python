import unittest
from yandex_api import create_folder, delete_folder
import yandex_api


class TestYaApi(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_success_create_folder(self):
        result = create_folder('test')
        self.assertEqual(result, 201)

    # def test_passed_create_folder(self):
    #     self.assertEqual(file3.create_folder('test_passed'), 409)

    def tearDown(self):
        file3.delete_folder('test')
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()
