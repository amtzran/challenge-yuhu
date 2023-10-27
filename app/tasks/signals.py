from django.db.models import signals
from django.dispatch import receiver

from .models import Task
from .services import send_notification_email


@receiver(signals.post_save, sender=Task)
def create_or_update_task_send_notification(sender, instance, *args, **kwargs):
    """
    Send notification after create or update task
    """

    job_params = {"title": instance.title, "email": instance.email}
    send_notification_email.delay(job_params)
