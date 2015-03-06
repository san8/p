from django.test import TestCase
from factory import Factory

from ..models import Project


class NewProjectFactory(Factory):
    class Meta:
        model = Project

    user_id = 64
    name = 'test project'
    description = 'asdf asdfjlas dflas dflas df'
    file_type = 'fastq'
    total_fastq_files = 2
    fastq_file1 = 'ftp://localhost/fastq_files/sample1.fastq.gz'
    fastq_file2 = ''


class ProjectModelsTestCase(TestCase):

    def test_NewProject_creation(self):
        n = NewProjectFactory()
        self.assertTrue(isinstance(n, Project))
        self.assertEqual(n.__unicode__(), n.name)
