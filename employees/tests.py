from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Employee
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class EmployeeAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.employee_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "department": "Engineering",
            "role": "Developer"
        }
        self.employee = Employee.objects.create(**self.employee_data)

    def test_create_employee(self):
        response = self.client.post(reverse('employee-list'), self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employee(self):
        response = self.client.get(reverse('employee-detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        update_data = {"name": "John Smith"}
        response = self.client.put(reverse('employee-detail', args=[self.employee.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        response = self.client.delete(reverse('employee-detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
