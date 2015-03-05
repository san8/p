# from selenium import webdriver

# from django.test import TestCase
# from django.core.urlresolvers import reverse


# class ProjectViewsTestCase(TestCase):

#     fixtures = ['auth_user.json', 'accounts.json', 'project.json']

#     def setUp(self):
#         response = self.client.get(reverse('auth_login'))
#         self.assertEqual(response.status_code, 200)
#         login = self.client.login(username='testpearl', password='123456')
#         self.assertTrue(login)

#     def test_newproject_view_get(self):
#         response = self.client.get(reverse('project:project_new'))
#         self.assertEqual(response.status_code, 200)

#     def test_newproject_view_post_valid_entry(self):
#         data = {'name': 'test project',
#                 'description': 'test description',
#                 'file_type': 'fastq',
#                 'total_fastq_files': 2,
#                 'fastq_file1': 'ftp://pearl:pearl@localhost/fastq_files/sample1.fastq.gz',}
#         response = self.client.post(reverse('project:project_new'), data)
#         self.assertEqual(response.status_code, 302)

#     def test_newproject_view_post_invalid_entry(self):
#         data = {'description': 'test description', }
#         response = self.client.post(reverse('project:project_new'), data)
#         self.assertEqual(response.status_code, 200)

#     def test_dashboard_view(self):
#         response = self.client.get(reverse('project:project_dashboard'))
#         self.assertEqual(response.status_code, 200)

#     def test_api(self):
#         response = self.client.get(reverse('project:data_api',
#                                            args=('tissues', 'elbow')))
#         vars(response)
#         self.assertEqual(response.status_code, 200)
#         expected_content = "Elbow"
#         self.assertContains(expected_content, response)


# class ProjectViewsLiveTestCase(TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.maximize_window()
#         self.driver.get("http://127.0.0.1:8000/project/new/")
#         username = self.driver.find_element_by_id("id_username")
#         username.send_keys("anand")
#         password = self.driver.find_element_by_id("id_password")
#         password.send_keys("123456")
#         login = self.driver.find_element_by_id("login")
#         login.click()

#     def test_newproject_view_get(self):
#         self.driver.find_element_by_id("id_name").send_keys("test project")
#         self.driver.find_element_by_css_selector(
#             "input[type='radio'][value='fastq']").click()
#         self.driver.find_element_by_id("id_fastq_file1").send_keys(
#             "ftp://pearl:pearl@127.0.0.1/fastq_files/sample1.fastq.gz")
#         self.driver.find_element_by_id("submit").click()

#     def teardown(self):
#         self.driver.quit()
