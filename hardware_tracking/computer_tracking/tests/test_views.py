from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from computer_tracking.models import Computer
from computer_tracking.tests.factories import ComputerFactory
from employee.tests.factories import EmployeeFactory


class ComputerListViewTest(TestCase):
    def setUp(self):
        self.computer = ComputerFactory.create(
            mac_address="00:11:22:33:44:55",
            computer_name="Test Computer",
            ip_address="192.168.1.100"
        )
        self.url = reverse('computer-list')
        self.client = APIClient()

    def test_computer_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ComputerDetailViewTest(TestCase):
    def setUp(self):
        self.computer = ComputerFactory.create(
            mac_address="00:11:22:33:44:55",
            computer_name="Test Computer",
            ip_address="192.168.1.100"
        )
        self.url = reverse('computer-detail', args=[self.computer.pk])
        self.client = APIClient()

    def test_computer_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ComputerCreateViewTest(TestCase):
    def setUp(self):
        self.url = reverse('computer-create')
        self.client = APIClient()

    def test_computer_create_view(self):
        data = {
            'mac_address': "00:11:22:33:44:66",
            'computer_name': "New Computer",
            'ip_address': "192.168.1.101"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ComputerUpdateViewTest(TestCase):
    def setUp(self):
        self.computer = ComputerFactory.create(
            mac_address="00:11:22:33:44:55",
            computer_name="Test Computer",
            ip_address="192.168.1.100"
        )
        self.url = reverse(
            'computer-update', kwargs={'pk': self.computer.pk}
        )
        self.client = APIClient()

    def test_partial_update(self):
        update_data = {
            "computer_name": "Updated Computer Name",
            "ip_address": "192.168.1.101",
        }

        response = self.client.patch(self.url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_computer = Computer.objects.get(pk=self.computer.pk)
        self.assertEqual(
            updated_computer.computer_name, update_data["computer_name"]
        )
        self.assertEqual(
            updated_computer.ip_address, update_data["ip_address"]
        )


class ComputerDeleteViewTest(TestCase):
    def setUp(self):
        self.computer = ComputerFactory.create(
            mac_address="00:11:22:33:44:55",
            computer_name="Test Computer",
            ip_address="192.168.1.100"
        )
        self.url = reverse(
            'computer-delete', kwargs={'pk': self.computer.pk}
        )
        self.client = APIClient()

    def test_computer_delete_view(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class EmployeeComputersViewTest(TestCase):
    def setUp(self):
        self.employee = EmployeeFactory.create(
            name="John Doe",
            abbreviation="asd"
        )
        self.computer = ComputerFactory.create(
            mac_address="00:11:22:33:44:99",
            computer_name="Employee Computer",
            ip_address="192.168.1.104",
            employee=self.employee
        )

        self.url = reverse(
            'employee-computers',
            kwargs={'employee_abbreviation': self.employee.abbreviation}
        )
        self.client = APIClient()

    def test_employee_computers_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AssignComputerToEmployeeTest(TestCase):
    def setUp(self):
        self.employee = EmployeeFactory.create(
            name="John Doe",
            abbreviation="asd"
        )
        self.computer = ComputerFactory.create(
            mac_address="00:11:22:33:44:00",
            computer_name="Unassigned Computer",
            ip_address="192.168.1.105"
        )

        self.url = reverse(
            'assign-computer', kwargs={'pk': self.computer.pk}
        )
        self.client = APIClient()

    def test_assign_computer_to_employee(self):

        data = {
            'new_employee_abbreviation': self.employee.abbreviation
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
