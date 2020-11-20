import unittest
import app


class TestApp(unittest.TestCase):
    """
    test class of app.py
    """

    @classmethod
    def setUpClass(cls):
        print('test start')
        cls.html = ""

    @classmethod
    def tearDownClass(cls):
        print('test over')

    def test_crawl(self):
        """
        test case for crawl
        """
        resp = app.crawl()
        self.assertEqual(200, resp.status_code)
        self.html = resp.text

    def test_scrape(self):
        """
        test case for crawl
        """
        items = app.scrape(self.html)
        self.assertIsNotNone(items)

    def test_raise_error(self):
        """
        test case for crawl(raise an error)
        """
        resp = app.crawl()
        self.assertEqual(1000000, resp.status_code)
        self.html = resp.text


if __name__ == "__main__":
    unittest.main()
