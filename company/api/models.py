from django.db import models


class Employee(models.Model):
    """
    Employee of a company.

    Attributes:

        name (models.Charfield): Employee's name
        email (models.EmailField): Employee's email
        department (models.Charfield): Employee's department

    """
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, max_length=100, unique=True)
    department = models.CharField(blank=False, max_length=100)

    def __str__(self):

        return "%s - %s" % (self.id, self.email)
