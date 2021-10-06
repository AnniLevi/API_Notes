from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email must be specified')
        if not password:
            raise ValueError('Password must be specified')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        # user.is_staff = user.is_staff_user
        # user.is_admin = user.is_admin_user
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        user = self.create_user(email, password=password, **extra_fields)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', False)
        user = self.create_user(email, password=password, **extra_fields)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []   # доп.поля, которые запрашиваются при создании пользователя

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_first_name(self):
        if self.name:
            return self.name
        return self.email

    def get_last_name(self):
        if self.surname:
            return self.surname
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # @property
    # def is_staff_user(self):
    #     if self.is_admin:
    #         return True
    #     return self.is_staff
    #
    # @property
    # def is_admin_user(self):
    #     return self.is_admin

    def save(self, *args, **kwargs):
        self.set_password(self.password)   # хэширует пароль
        super().save(*args, **kwargs)
