from django.contrib import admin
from computer_tracking.models import Computer


class ComputerAdmin(admin.ModelAdmin):
    list_display = (
        'mac_address', 'computer_name', 'ip_address', 'employee', 'description'
    )
    search_fields = ('computer_name',)


admin.site.register(Computer, ComputerAdmin)
