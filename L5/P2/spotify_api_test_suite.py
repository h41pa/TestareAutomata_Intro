import unittest
import HtmlTestRunner

from L5.P2.tests.test_get_playlist import TestPlaylist
from L5.P2.tests.test_new_releases import TestNewReleases
from L5.P2.tests.test_get_album_endpoint import TestGetAlbum


class TestSuite(unittest.TestCase):

    def test_suite(self):
        suita_teste = unittest.TestSuite()

        suita_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPlaylist),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNewReleases),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAlbum)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Spotify Api report',
            report_name='spotify api test results'
        )
        runner.run(suita_teste)
