from unittest import TestCase 
from factory import Factory

from django.test.utils import override_settings

from ..tasks import get_ftp_files 
from ..models import NewProject


class NewProjectFactory(Factory):
    class Meta:
        model = NewProject 

    id = 100
    customer_id = 64
    name = 'test project'
    description = 'asdf asdfjlas dflas dflas df'
    file_type = 'fastq'
    total_fastq_files = 2
    fastq_file1 = 'ftp://localhost/fastq_files/sample1.fastq.gz'
    fastq_file2 = ''


class CeleryTasksTestCase(TestCase):

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
    def test_get_ftp_files(self):
        n = NewProjectFactory()
        self.assertEqual(n.id, 100)
        result = get_ftp_files(n.pk)
        self.assertEqual(result, 0)

