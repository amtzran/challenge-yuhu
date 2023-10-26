from django.urls import reverse
from mixer.backend.django import mixer

from base.testing import AuthTokenTesting


class ListTaskTest(AuthTokenTesting):
    """
    Unit test for list task
    """

    user = None

    @classmethod
    def setUpTestData(cls):
        cls.user = mixer.blend("users.User")
        mixer.cycle(10).blend("tasks.Task", author=cls.user)

    def get_tasks(self, token=None, params=None):
        url = reverse("tasks-list")

        return self.get(url, token, params)

    def test_task_list(self):
        """
        Test tasks list endpoint for user authenticated
        """

        response = self.get_tasks(token=self.get_access_token(self.user))

        self.assert_status_200(response)
        self.assertEqual(response.data.get("total"), 10)
