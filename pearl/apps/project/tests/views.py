from django.test import TestCase
from django.core.urlresolvers import reverse 


class ProjectViewsTestCase(TestCase):

    fixtures = ['auth_user.json', 'accounts.json', 'project.json']

    def setUp(self):
        #print self._testMethodName
        response = self.client.get(reverse('auth_login'))
        self.assertEqual(response.status_code, 200)
        login = self.client.login(username='testpearl', password='123456')
        self.assertTrue(login)

    def test_newproject_view_get(self):
        response = self.client.get(reverse('project:project_new'))
        self.assertEqual(response.status_code, 200)

    def test_newproject_view_post_valid_entry(self):
        data = {'name': 'test project',
                'description': 'test description',
                'file_type': 'fastq', 
                'total_fastq_files': 2,
                'fastq_file1': 'ftp://pearl:pearl@localhost/fastq_files/sample1.fastq.gz',}
        response = self.client.post(reverse('project:project_new'), data ) 
        self.assertEqual(response.status_code, 302)

    def test_newproject_view_post_invalid_entry(self):
        data = {'description': 'test description', }
        response = self.client.post(reverse('project:project_new'), data ) 
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view(self):
        response = self.client.get(reverse('project:project_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_api(self):
        response = self.client.get(reverse('project:data_api',
                                           args=('tissues', 'elbow')))
        vars(response)
        self.assertEqual(response.status_code, 200)
#        expected_content = "Elbow"
 #       self.assertContains(expected_content, response)
        
        
"""
    def test_qcreport_view_get(self):
       response = self.client.get(reverse('project:project_qcreport', args={55}))
       self.assertEqual(response.status_code, 200)

    def test_qcreport_view_post_invalid_entry(self):
        data = {'start_processing': True }
        response = self.client.post(reverse('project:project_qcreport',
                                             args={55}), data)
        self.assertEqual(response.status_code, 200)

    def test_qcreport_view_post_valid_entry(self):
        data = {'trash_field': 'trash_options',}
        response = self.client.post(reverse('project:project_qcreport',
                                             args={55}), data)
        self.assertEqual(response.status_code, 200)


"""

'''  
class ProjectModelTestCase(TestCase):
    fixtures = ['test_user_login.json']
    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')

    def create_newproject(self):
        return NewProject.objects.create(
                customer_id = 64,
                name = 'test project',
                description = 'asdf asdfjlas dflas dflas df',
                file_type = 'fastq',
                total_fastq_files = 2,
                fastq_file1 = 'ftp://localhost/fastq_files/sample1.fastq.gz',
                fastq_file2 = 'ftp://localhost/fastq_files/sample2.fastq.bz2',
        )



'''

