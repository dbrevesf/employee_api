from .models import Employee
from rest_framework import viewsets
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for list, add and remove employees.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
