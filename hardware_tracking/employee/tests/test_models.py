from django.test import TestCase

from employee.tests.factories import EmployeeFactory


class EmployeeModelTestCase(TestCase):
    def test_create_feed(self):
        employee = EmployeeFactory.create(
            name='Test Employee',
            abbreviation='emp'
        )
        self.assertEqual(employee.name, 'Test Employee')
        self.assertEqual(employee.abbreviation, 'emp')
