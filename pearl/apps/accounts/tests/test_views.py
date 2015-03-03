from selenium import webdriver

from django.test import TestCase
from django.core.urlresolvers import reverse


class AccountsViewsTestCase(TestCase):
    fixtures = ['auth_user.json', 'accounts.json']

    def setUp(self):
        pass

    def test_register(self):
        response = self.client.get(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(reverse('auth_login'))
        self.assertEqual(response.status_code, 200)
        login = self.client.login(username='testpearl', password='123456')
        self.assertTrue(login)
        response = self.client.get(reverse('project:project_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_get(self):
        response = self.client.get(reverse('account:account_profile'))
        self.assertEqual(response.status_code, 302)
        login = self.client.login(username='testpearl', password='123456')
        self.assertTrue(login)
        response = self.client.get(reverse('account:account_profile'))
        self.assertEqual(response.status_code, 200)
        data = { 'timezone': 'UTC'}
        response = self.client.post(reverse('account:account_profile'), data)
        self.assertEqual(response.status_code, 302)



class AccountViewsLiveTestCase(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(reverse('account_signup'))
        username = self.driver.find_element_by_id("id_username")
        username.send_keys("anand")
        password = self.driver.find_element_by_id("id_password")
        password.send_keys("123456")
        login = self.driver.find_element_by_id("login")
        login.click()

    def test_newproject_view_get(self):
        self.driver.find_element_by_id("id_name").send_keys("test project")
        self.driver.find_element_by_css_selector(
            "input[type='radio'][value='fastq']").click()
        self.driver.find_element_by_id("id_fastq_file1").send_keys(
            "ftp://pearl:pearl@127.0.0.1/fastq_files/sample1.fastq.gz")
        self.driver.find_element_by_id("submit").click()

    def teardown(self):
        self.driver.quit()
