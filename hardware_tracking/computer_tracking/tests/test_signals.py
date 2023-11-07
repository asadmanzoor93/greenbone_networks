from django.conf import settings
from django.test import TestCase
from unittest.mock import patch, Mock

from computer_tracking.models import Computer
from computer_tracking.signals import notify_messaging_service
from computer_tracking.tests.factories import ComputerFactory
from employee.tests.factories import EmployeeFactory


class ComputerSignalTest(TestCase):
    def setUp(self):
        self.employee = EmployeeFactory(abbreviation="emp")
        self.computers = [
            ComputerFactory.create(
                employee=self.employee, ip_address="192.168.1.100"
            ),
            ComputerFactory.create(
                employee=self.employee, ip_address="192.168.1.101"
            ),
            Computer.objects.create(
                employee=self.employee, ip_address="192.168.1.102"
            ),
        ]

    def test_check_employee_computers_signal(self):
        with patch('computer_tracking.signals.notify_messaging_service') as \
                mock_notify_messaging_service:

            self.computers[0].computer_name = "Updated Computer Name"
            self.computers[0].save()

            mock_notify_messaging_service.assert_called_once_with(
                self.employee.abbreviation
            )

    def test_notify_messaging_service(self):
        expected_payload = {
            "level": "warning",
            "employeeAbbreviation": self.employee.abbreviation,
            "message": "Employee has 3 or more assigned computers."
        }

        with patch('requests.post') as mock_post:
            mock_response = Mock()
            mock_response.raise_for_status.return_value = None
            mock_post.return_value = mock_response

            notify_messaging_service(self.employee.abbreviation)
            mock_post.assert_called_once_with(
                settings.MESSAGING_SERVICE_URL, json=expected_payload
            )
