import factory
from django.utils import timezone

from employee.models import Employee


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    name = factory.Faker('word')
    abbreviation = factory.Faker('lexify', text='???')
    date_joined = factory.LazyFunction(timezone.now)
