import factory

from computer_tracking.models import Computer
from employee.tests.factories import EmployeeFactory


class ComputerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Computer

    mac_address = factory.Faker('mac_address')
    computer_name = factory.Faker('word')
    employee = factory.SubFactory(EmployeeFactory)
