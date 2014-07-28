from django.test import TestCase
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.test.utils import override_settings 

from .models import NewProject 
#from .tasks import get_ftp_files 

class ProjectViewsTestCase(TestCase):
    def test_dashboard(self):
        response = self.client.get(reverse('project:project_dashboard'))
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create(username='chillaranand', password='123456',
                is_active=True, is_staff=True, is_superuser=True) 
        self.user.set_password('123456') 
        self.user.save() 
        self.user = authenticate(username='chillaranand', password='123456') 
        login = self.client.login(username='chillaranand', password='123456') 
        self.assertTrue(login)
        response = self.client.get(reverse('project:project_dashboard'))
        self.assertEqual(response.status_code, 200)


class CeleryTasksTestCase(TestCase):

    def test_get_ftp_files(self):
        pass 
"""
        result = get_ftp_files.apply_async(args=[158,])
        self.assertEquals(result.get(), 0)
        self.assertTrue(result.successfull())

"""
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

    def test_newproject_creation(self):
        n = self.create_newproject()
        self.assertTrue(isinstance(n, NewProject))
        self.assertEqual(n.__str__(), n.name)

