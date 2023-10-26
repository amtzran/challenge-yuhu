import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    """Base model for create other system models."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super(BaseModel, self).delete()


class CatalogModel(BaseModel):
    """Base catalog model for create other system catalogues models."""

    name = models.CharField(max_length=255)

    class Meta:
        abstract = True
        ordering = ["name"]

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super(CatalogModel, self).delete()

    def __str__(self):
        return self.name


class AddressModel(BaseModel):
    """
    Base model for common address
    """

    street_number = models.CharField(max_length=64)
    route = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)

    address_latitude = models.FloatField(blank=True, null=True)
    address_longitude = models.FloatField(blank=True, null=True)

    formatted_address = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.formatted_address


class ContactModel(BaseModel):
    """
    Base model for common contact
    """

    name = models.CharField(max_length=255)
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    job_title = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}/{self.phone}/{self.email}"
