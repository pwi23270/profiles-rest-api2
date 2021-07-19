from django.db import models
"""Note: if the server didn't work using python manage.py runserver 0.0.0.0:8000
 delete all lines in this file except the first line since it is here by defaulf because there are non-defined function
 and classes hence the server will not work"""
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
"""Note: Two lines should be between the classes"""
class UserProfileManager(BaseUserManager):
    """Q5: I didn't unserstand what he said about passwords in video 23 time 3:23"""
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Note: password here =! None since we need admin users to have passwords"""
        user = self.create_user(email, name, password)
        """Note: we didn't pass self argument in the user = self.create_user(email, name, password) since
        self is passed automatically in class functions"""
        user.is_superuser = True
        """Note: is_superuser is defined in PermissionsMixin so we don't need to define it like is_staff"""
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    """UserProfileManager is to be created later"""
    USERNAME_FIELD = 'email'
    """To make the user enter his email instead of username"""
    REQUIRED_FIELDS = ['name']
    """Q1: Why the name in the list must be between quotation marks since it is a variable it should be?"""
    """To make name mandetory and no need to add email since USERNAME_FIELD is by default mandetory"""
    def get_full_name(self):
        return self.name
        """Note: If you define a function inside a class the input must be self at least"""
        """Q2: Why de we need this function as long as we have name.models.CharField"""
    def get_short_name(self):
        """Q3:Why do we have full ane ans short name"""
        return self.name
    def __str__(self):
        """Return string representation of our user"""
        """Note: this function is recommended not mandetory since the output not necessary makes sense"""
        """Q4: Why do need to convert email into string since it is already string ?"""
        return self.email
