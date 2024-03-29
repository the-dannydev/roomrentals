from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


class UserManager(BaseUserManager):
    def create_user(self, number, email=None, full_name=None, photo=None, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            number=number,
            full_name=full_name,
            email=self.normalize_email(email),
            photo=photo,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, number, email=None, full_name=None, photo=None, password=None):
        user = self.create_user(
            number, email=email, full_name=full_name, photo=photo, password=password)

        user.staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, number, email=None, full_name=None, photo=None, password=None):
        user = self.create_user(
            number, email=email, full_name=full_name, photo=photo, password=password)

        user.admin = True
        user.staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    number = PhoneNumberField(blank=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=False, null=False)
    photo = models.ImageField(blank=True, null=True,
                              upload_to='users/profile_picture')
    is_verified = models.BooleanField(_('verified'), default=False,)
    timestamp = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = ['full_name', 'email']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/user.jpg"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    objects = UserManager()

    def __str__(self):
        return str(self.number)
