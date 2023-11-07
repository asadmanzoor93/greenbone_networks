from django.contrib import admin

from employee.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'date_joined',)
    ordering = ('-date_joined',)
    search_fields = ('name',)


admin.site.register(Employee, EmployeeAdmin)
