from unittest import TestCase 
from nose.tools import eq_ 

from ..tasks import get_ftp_files 


class CeleryTasksTestCase(TestCase):

    def test_get_ftp_files_fail(self):
        project_id = 77
        result = get_ftp_files.apply_async(args=[project_id]).get() 
        eq_(result, 0)
