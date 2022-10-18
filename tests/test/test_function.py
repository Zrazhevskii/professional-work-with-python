import unittest
from parameterized import parameterized
from function import check_document, get_doc_owner_name, add_new_shelf


class UnitTestMain(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    checklist = [
        ("2207 876234", True),
        ("11-2", True),
        ("10006", True),
        ("11111", False),
        ("12345", False)
    ]

    @parameterized.expand(checklist)
    def test_check_document_existance(self, doc_number, ex_result):
        result = check_document(doc_number)
        self.assertEqual(ex_result, result)

    checklist2 = [
        ["2207 876234", "Василий Гупкин"],
        ["11-2", "Геннадий Покемонов"],
        ["10006", "Аристарх Павлов"],
        ["11111", None]
    ]

    @parameterized.expand(checklist2)
    def test_get_doc_owner_name(self, doc_number, ex_result):
        self.assertEqual(get_doc_owner_name(doc_number), ex_result)

    checklist3 = [
        ['4', ('4', True)],
        ['5', ('5', True)],
        ['3', ('3', False)]
    ]

    @parameterized.expand(checklist3)
    def test_add_new_shelf(self, doc_number, ex_result):
        self.assertEqual(add_new_shelf(doc_number), ex_result)