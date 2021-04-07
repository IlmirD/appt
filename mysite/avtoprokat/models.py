from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

languages = [
        ('en', 'English'),
        ('ru', 'Русский'),
    ]

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, language, password=None):
        if not email:
            raise ValueError()
        if not username:
            raise ValueError()
        if not language:
            raise ValueError()
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            language=language,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, language, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            language=language,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=50)
    language = models.CharField(max_length=50, choices=languages, default='Russian')

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'language']

    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Car(models.Model):
    name_en = models.CharField(max_length=70)
    name_ru = models.CharField(max_length=70)
    created = models.DateField()
    added = models.DateField()
    renter = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ['name_en']

    def __str__(self):
        return self.name_en