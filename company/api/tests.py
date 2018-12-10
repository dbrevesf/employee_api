from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status


class EmployeeTest(APITestCase):
    """
    Class which contains the unit tests for the API endpoint: Employee
    """

    url = '/employee/'
    client = APIClient()
    employee_1 = {'name': 'Arnaldo Pereira',
                  'email': 'arnaldo@luizalabs.com',
                  'department': 'Architecture'}
    employee_2 = {'name': 'Joao Pereira',
                  'email': 'joao@luizalabs.com',
                  'department': 'Mobile'}

    def test_list_employees(self):

        data = self.employee_1.copy()
        response = self.client.post(self.url, data, format='json')
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_single_employee(self):
        data = self.employee_1.copy()
        response = self.client.post(self.url, data, format='json')
        employee_id = response.data['id']
        employee_url = self.url + str(employee_id) + '/'
        response = self.client.get(employee_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['department'], data['department'])

    def test_list_nonexistent_employee(self):

        employee_id = '123'
        employee_url = self.url + str(employee_id) + '/'
        response = self.client.get(employee_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_employee_correctly(self):

        data = self.employee_1.copy()
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employee_duplicated_email(self):

        data_1 = self.employee_1.copy()
        self.client.post(self.url, data_1, format='json')
        data_2 = self.employee_2.copy()
        data_2['email'] = data_1['email']
        response = self.client.post(self.url, data_2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_employee_with_missing_name(self):

        data = self.employee_1.copy()
        data['name'] = ''
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_employee_with_missing_email(self):

        data = self.employee_1.copy()
        data['email'] = ''
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_employee_with_missing_department(self):

        data = self.employee_1.copy()
        data['department'] = ''
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_employee_correctly(self):

        data = self.employee_1.copy()
        response = self.client.post(self.url, data, format='json')
        employee_id = response.data['id']
        employee_url = self.url + str(employee_id) + '/'
        data['email'] = 'pereira@luizalabs.com'
        data.update({'pk': employee_id})
        response = self.client.put(employee_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee_duplicated_email(self):

        data_1 = self.employee_1.copy()
        response = self.client.post(self.url, data_1, format='json')
        employee_id = response.data['id']
        employee_url = self.url + str(employee_id) + '/'
        data_2 = self.employee_2.copy()
        self.client.post(self.url, data_2, format='json')
        data_1['email'] = data_2['email']
        data_1.update({'pk': employee_id})
        response = self.client.put(employee_url, data_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_employee_missing_name(self):

        data = self.employee_1.copy()
        response = self.client.post(self.url, data, format='json')
        employee_id = response.data['id']
        employee_url = self.url + str(employee_id) + '/'
        data['name'] = ''
        data.update({'pk': employee_id})
        response = self.client.put(employee_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_employee_missing_email(self):

        data = self.employee_1.copy()
        response = self.client.post(self.url, data, format='json')
        employee_id = response.data['id']
        employee_url = self.url + str(employee_id) + '/'
        data['email'] = ''
        data.update({'pk': employee_id})
        response = self.client.put(employee_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_employee_missing_department(self):

        data = self.employee_1.copy()
        response = self.client.post(self.url, data, format='json')
        employee_id = response.data['id']
        employee_url = self.url + str(employee_id) + '/'
        data['department'] = ''
        data.update({'pk': employee_id})
        response = self.client.put(employee_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_employee(self):

        data = self.employee_1.copy()
        response = self.client.post(self.url, data, format='json')
        employee_id = response.data['id']
        employee_url = self.url + str(employee_id) + '/'
        response = self.client.delete(employee_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
