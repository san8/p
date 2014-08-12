from unittest import TestCase 
from model_mommy import mommy

from django.test.utils import override_settings

from ..tasks import fetch_files_ftp, work_flow
from ..models import NewProject



class CeleryTasksTestCase(TestCase):

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')

    def test_work_flow(self):
        n = mommy.make('NewProject')
        result = work_flow(n.id, n.status)
        self.assertEqual(result[0], n.id)
        self.assertEqual(result[1], n.status)
        
    def test_get_ftp_files(self):
        n = mommy.make('NewProject')
        local_dir = 'media/tests'
        url_list = ['ftp://pearl:pearl@localhost/fastq_files/sample1.fastq.gz',
                     'ftp://pearl:pearl@localhost/fastq_files/sample2.fastq.bz2']
        result = fetch_files_ftp(local_dir, url_list)
        self.assertTrue(result)


        
