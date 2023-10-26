from django.urls import reverse
from django.utils import timezone
from mixer.backend.django import mixer

from base.testing import AuthTokenTesting


class UpdateTaskTest(AuthTokenTesting):
    """
    Unit test for update task
    """

    user = None

    @classmethod
    def setUpTestData(cls):
        cls.user = mixer.blend("users.User")
        cls.task = mixer.blend("tasks.Task", author=cls.user)

        cls.UPDATE_TASK_DATA = {"due_date": "2023-10-26"}

    def update_task(self, task, data, token=None):
        url = reverse("tasks-detail", args=[task.random_slug])

        return self.patch(url, data, token)

    def test_task_update(self):
        """
        Test Task update endpoint for user with authenticated
        """

        response = self.update_task(self.task, self.UPDATE_TASK_DATA, self.get_access_token(self.user))

        self.assert_status_200(response)

        self.task.refresh_from_db()

        self.assertEquals(
            timezone.datetime.strftime(self.task.due_date, "%Y-%m-%d"), self.UPDATE_TASK_DATA.get("due_date")
        )
