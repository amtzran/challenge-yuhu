from django.urls import reverse
from mixer.backend.django import mixer

from base.testing import AuthTokenTesting


class RetrieveTaskTest(AuthTokenTesting):
    """
    Unit test for retrieve task
    """

    user = None

    @classmethod
    def setUpTestData(cls):
        cls.user = mixer.blend("users.User")
        cls.task = mixer.blend("tasks.Task", author=cls.user)

    def get_task(self, task, token=None):
        url = reverse("tasks-detail", args=[task.random_slug])

        return self.get(url, token)

    def test_task_retrieve(self):
        """
        Test task retrieve endpoint for user with authenticated
        """

        response = self.get_task(self.task, self.get_access_token(self.user))

        self.assert_status_200(response)
