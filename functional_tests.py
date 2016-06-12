import unittest
from selenium import webdriver

DJANGO_ADDRESS = 'http://localhost:8000'


class VisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_if_django_app_has_started(self):
        self.browser.get(DJANGO_ADDRESS)
        self.assertIn('Django', self.browser.title)

if __name__ == "__main__":
    unittest.main()
