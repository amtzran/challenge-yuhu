from django.db import models

from base.models import RandomSlugModel, TimeStampedModel


class Task(RandomSlugModel, TimeStampedModel):
    """
    Model for Task
    """

    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)

    email = models.EmailField()
    due_date = models.DateField()

    author = models.ForeignKey(to="users.User", on_delete=models.PROTECT, related_name="tasks")

    def __str__(self):
        return self.title + " - " + self.author.name

    class Meta:
        ordering = ["-created_at"]
