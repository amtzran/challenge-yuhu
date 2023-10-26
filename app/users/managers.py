from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom User Manager class for User model
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """
        Custom create user method
        """
        extra_fields["is_staff"] = False
        extra_fields["is_superuser"] = False
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Custom create superuser method
        """
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        return self._create_user(email, password, **extra_fields)

    def create_user_without_password(self, email):
        """
        Define flow for creating user without a defined password,
        for example when an employee registers a new user
        """
        user, _ = self.get_or_create(email=email)
        return user
