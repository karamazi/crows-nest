import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

LOCAL_APP_ADDRESS = 'http://localhost:8000'


class VisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_if_user_can_add_new_cluster(self):
        # User enters the web app
        self.browser.get(LOCAL_APP_ADDRESS)
        self.assertIn('Armada', self.browser.title)

        # User wants to add new cluster
        input_box = self.browser.find_element_by_id("id_new_cluster")
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            "Cluster's address"
        )
        input_box.send_keys('http://localhost:8900')
        input_box.send_keys(Keys.ENTER)

        # Cluster is now displayed
        clusters_list = self.browser.find_element_by_id('id_clusters')
        rows = clusters_list.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'http://localhost:8900' for row in rows)
        )
        # User wants to add another cluster
        self.fail("Finish the test")

if __name__ == "__main__":
    unittest.main()
