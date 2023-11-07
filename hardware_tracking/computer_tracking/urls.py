from django.urls import path
from computer_tracking.views import (
    ComputerListView,
    ComputerDetailView,
    ComputerCreateView,
    ComputerUpdateView,
    ComputerDeleteView,
    EmployeeComputersView,
    AssignComputerToEmployee,
)

urlpatterns = [
    path('computers/', ComputerListView.as_view(), name='computer-list'),
    path('computers/<int:pk>/', ComputerDetailView.as_view(), name='computer-detail'),
    path('computers/create/', ComputerCreateView.as_view(), name='computer-create'),
    path('computers/<int:pk>/update/', ComputerUpdateView.as_view(), name='computer-update'),
    path('computers/<int:pk>/delete/', ComputerDeleteView.as_view(), name='computer-delete'),
    path('computers/employee/<str:employee_abbreviation>/', EmployeeComputersView.as_view(), name='employee-computers'),
    path('computers/<int:pk>/assign/', AssignComputerToEmployee.as_view(), name='assign-computer'),
]
