from django.test import TestCase

from computer_tracking.tests.factories import ComputerFactory
from employee.tests.factories import EmployeeFactory


class ComputerModelTestCase(TestCase):
    def test_create_feed(self):
        emp = EmployeeFactory.create(
            name='Test User',
            abbreviation='emp'
        )
        computer = ComputerFactory.create(
            mac_address='00:11:22:33:44:55',
            computer_name='Computer 1',
            ip_address='192.168.0.1',
            employee=emp,
            description='Test computer description',
        )
        self.assertEqual(computer.mac_address, '00:11:22:33:44:55')
        self.assertEqual(computer.computer_name, 'Computer 1')
        self.assertEqual(computer.employee.abbreviation, emp.abbreviation)
        self.assertEqual(
            computer.description, 'Test computer description'
        )
