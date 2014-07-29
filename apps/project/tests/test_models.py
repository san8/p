from django.test import TestCase 

from ..models import NewProject 


class ProjectModelsTestCase(TestCase):

    def create_NewProject(self, name="test", customer_id=65):
        return NewProject.objects.create(name="test", customer_id=65)

    def test_NewProject_creation(self):
        n = self.create_NewProject()
        self.assertTrue(isinstance(n, NewProject))
        self.assertEqual(n.__unicode__(), n.name)

