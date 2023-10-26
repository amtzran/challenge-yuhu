from django.urls import reverse
from mixer.backend.django import mixer

from base.testing import AuthTokenTesting


class DestroyTaskTest(AuthTokenTesting):
    """
    Unit test for destroy task
    """

    user = None

    @classmethod
    def setUpTestData(cls):
        cls.user = mixer.blend("users.User")
        cls.task = mixer.blend("tasks.Task", author=cls.user)

    def destroy_task(self, task, token=None):
        url = reverse("tasks-detail", args=[task.random_slug])

        return self.delete(url, token)

    def test_task_destroy(self):
        """
        Test task destroy endpoint for user with authenticated
        """

        response = self.destroy_task(self.task, self.get_access_token(self.user))

        self.assert_status_204(response)
