from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
)

from computer_tracking.models import Computer
from computer_tracking.serializers import ComputerSerializer
from employee.models import Employee


class ComputerListView(ListAPIView):
    """
    Retrieve a list of all computers.

    This view allows the system administrator to get a list of  all computer
    records.

    Endpoint: /api/computers/
    """

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ComputerDetailView(RetrieveAPIView):
    """
    Retrieve the details of a single computer.

    This view allows the system administrator to retrieve the details of a
    single computer by providing its primary key.

    Endpoint: /api/computers/<int:pk>/
    """

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ComputerCreateView(CreateAPIView):
    """
    Create a new computer.

    This view allows the system administrator to create a new computer by
    providing the necessary data in the request.

    Endpoint: /api/computers/create/
    """

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ComputerUpdateView(UpdateAPIView):
    """
    Update the details of a single computer.

    This view allows the system administrator to update the details of a
    single computer by providing its primary key and the updated data.

    Endpoint: /api/computers/<int:pk>/update/
    """

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComputerDeleteView(DestroyAPIView):
    """
    Delete a single computer.

    This view allows the system administrator to delete a single computer by
    providing its primary key.

    Endpoint: /api/computers/<int:pk>/delete/
    """

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class EmployeeComputersView(ListAPIView):
    """
    Retrieve a list of all computers assigned to a specific employee.

    This view allows the system administrator to retrieve a list of all
    computers assigned to a specific employee by providing their abbreviation.

    Endpoint: /api/computers/employee/<str:employee_abbreviation>/
    """

    serializer_class = ComputerSerializer

    def get_queryset(self):
        employee_abbreviation = self.kwargs['employee_abbreviation']
        return Computer.objects.filter(
            employee__abbreviation=employee_abbreviation
        )


class AssignComputerToEmployee(APIView):
    """
    Assign a computer to a new employee.

    This view allows the system administrator to assign a computer to a new
    employee by updating the 'employee_abbreviation' field for a specific
    computer.

    Endpoint: /api/computers/<int:pk>/assign/
    """

    def post(self, request, *args, **kwargs):
        computer_id = kwargs['pk']
        new_employee_abbreviation = request.data.get(
            'new_employee_abbreviation', None
        )

        if new_employee_abbreviation:
            computer = get_object_or_404(Computer, pk=computer_id)
            employee, _ = Employee.objects.get_or_create(
                abbreviation=new_employee_abbreviation
            )
            computer.employee = employee
            computer.save()

            return Response(
                {"detail": "Computer assigned to a new employee."},
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                {
                    "detail": "Please provide a valid new employee "
                              "abbreviation."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
