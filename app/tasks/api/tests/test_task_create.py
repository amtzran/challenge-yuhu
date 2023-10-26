from django.urls import reverse
from mixer.backend.django import mixer

from base.testing import AuthTokenTesting


class CreateTaskTest(AuthTokenTesting):
    """
    Unit test for create task
    """

    user = None

    @classmethod
    def setUpTestData(cls):
        cls.user = mixer.blend("users.User")

        cls.NEW_TASK_DATA = {
            "title": "A nice title for the task",
            "description": "A nice description for the task",
            "email": "alberto@example.com",
            "due_date": "2023-10-26",
        }

    def create_task(self, data, token=None):
        url = reverse("tasks-list")

        return self.post(url, data, token)

    def test_task_create(self):
        """
        Test Task create endpoint for user authenticated
        """

        response = self.create_task(data=self.NEW_TASK_DATA, token=self.get_access_token(self.user))

        self.assert_status_201(response)
        self.assertEquals(response.data.get("due_date"), "26/10/2023")
