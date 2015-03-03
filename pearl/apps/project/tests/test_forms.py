from django.test import TestCase

from django.core.urlresolvers import reverse

from ..forms import NewProjectForm

class ProjectFormsTestCase(TestCase):

    fixtures = ['auth_user.json', 'accounts.json', 'project.json']

    def setUp(self):
        #print self._testMethodName
        response = self.client.get(reverse('auth_login'))
        self.assertEqual(response.status_code, 200)
        login = self.client.login(username='testpearl', password='123456')
        self.assertTrue(login)

    def test_NewProjectForm(self):
        form_data = { 'customer_id': 65, 'name': 'test project',
            'description': 'asdf asdfjlas dflas dflas df',
            'file_type' : 'fastq', 'total_fastq_files' : 2,
            'fastq_file1' : 'ftp://localhost/fastq_files/sample1.fastq.gz', }
        form = NewProjectForm(data=form_data)
        self.assertEqual(form.is_valid(), True)



'''
    def test_StartProcessingForm(self):
        form_data = { 'start_processing': 1, }
        form = StartProcessingForm(data=form_data)
        self.assertEqual(form.is_valid(), True)
'''
