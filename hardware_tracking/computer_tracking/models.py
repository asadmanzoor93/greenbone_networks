from django.db import models

from employee.models import Employee


class Computer(models.Model):
    mac_address = models.CharField(max_length=17, unique=True)
    computer_name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.computer_name
