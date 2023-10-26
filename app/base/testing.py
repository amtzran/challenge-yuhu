import json
from urllib.parse import urlencode

from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class AuthTokenTesting(APITestCase):
    @staticmethod
    def get_access_token(user):
        """
        Obtain Token for User
        """
        return str(RefreshToken.for_user(user).access_token)

    @staticmethod
    def get_init_instances(mixer):
        """
        Create and return user, company and employee
        """
        user = mixer.blend("users.User")
        company = mixer.blend("companies.Company")
        employee = mixer.blend("employees.Employee", user=user, company=company)

        return user, company, employee

    def get(self, url, token=None, params=None):
        """GET method with access token"""
        kwargs = {}
        if token:
            kwargs["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        if params:
            kwargs["QUERY_STRING"] = urlencode(params, doseq=True)
        return self.client.get(url, **kwargs)

    def post(self, url, data, token=None, multipart=False):
        """POST method with access token"""
        kwargs = {}
        if token:
            kwargs["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        if multipart:
            kwargs["format"] = "multipart"
        else:
            kwargs["content_type"] = "application/json"
            data = json.dumps(data)
        return self.client.post(url, data, **kwargs)

    def patch(self, url, data, token, multipart=False):
        """PATCH method with access token"""
        kwargs = {}
        if token:
            kwargs["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        if multipart:
            kwargs["format"] = "multipart"
        else:
            kwargs["content_type"] = "application/json"
            data = json.dumps(data)
        return self.client.patch(url, data, **kwargs)

    def delete(self, url, token=None):
        """DELETE method with access token"""
        kwargs = {}
        if token:
            kwargs["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        return self.client.delete(url, **kwargs)

    def assert_status_200(self, response):
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def assert_status_201(self, response):
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def assert_status_204(self, response):
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.data)

    def assert_status_403(self, response):
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def assert_status_400(self, response):
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

    @staticmethod
    def file_test(image_file):
        img = Image.new("RGB", (10, 10))
        img.save(image_file, format="JPEG")
        image_file.seek(0)
        return image_file
