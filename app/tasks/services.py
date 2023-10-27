from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task()
def send_notification_email(job_params):
    """
    Sending notification by email
    """

    title = job_params.get("title", "")
    recipient = job_params.get("email")

    send_mail(
        "Notificación de Tarea",
        f"Tarea: {title}",
        settings.EMAIL_HOST_USER,
        [recipient],
        fail_silently=False,
    )
