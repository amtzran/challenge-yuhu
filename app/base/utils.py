import os

import boto3
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core import settings


class Utils:
    @staticmethod
    def upload_pdf(pdf: object, key: object) -> object:
        """
        @rtype: object
        """
        client = boto3.client("s3")
        return client.put_object(
            Bucket=os.environ.get("AWS_STORAGE_BUCKET_NAME"),
            ACL="public-read",
            ContentType="application/pdf",
            Body=pdf,
            Key=key,
        )

    @staticmethod
    def send_mail(subject, body, path_template, data, emails):
        template = get_template(path_template)
        content = template.render(data)

        message = EmailMultiAlternatives(
            subject=subject, body=body, from_email=f"Project Name<{settings.EMAIL_HOST_USER}>", to=emails
        )

        message.attach_alternative(content, "text/html")
        message.send()
