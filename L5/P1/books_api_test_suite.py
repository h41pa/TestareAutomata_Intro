import unittest
import HtmlTestRunner
# pip install html-testRunner
from L5.P1.tests.test_api_status import TestApiStatus
from L5.P1.tests.test_get_all_books import TestGetAllBooks
from L5.P1.tests.test_submit_order import TestSubmitOrder
from L5.P1.tests.test_update_order import TestUpdateOrder


class TestSuite(unittest.TestCase):

    def test_suite(self):
        suita_teste = unittest.TestSuite()

        suita_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestApiStatus),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAllBooks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateOrder)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='APi test report',
            report_name='Books API Test Results'
        )
        runner.run(suita_teste)


