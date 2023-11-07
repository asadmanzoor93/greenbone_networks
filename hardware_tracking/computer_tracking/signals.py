import logging
import requests

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from computer_tracking.models import Computer

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Computer)
def check_employee_computers(sender, instance, **kwargs):
    if instance.employee:
        employee_devices = Computer.objects.filter(employee=instance.employee)
        if employee_devices.count() >= 3:
            notify_messaging_service(instance.employee.abbreviation)


def notify_messaging_service(employee_abbreviation):
    payload = {
        "level": "warning",
        "employeeAbbreviation": employee_abbreviation,
        "message": "Employee has 3 or more assigned computers."
    }

    try:
        response = requests.post(
            settings.MESSAGING_SERVICE_URL,
            json=payload
        )
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        logger.error(f'Message Notification Exception: {e}')
        pass
