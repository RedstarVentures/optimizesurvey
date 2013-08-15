from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class EmailUserManager(BaseUserManager):

  def create_user(self, email, password=None):

    if not email:
      raise ValueError('Users must have an email address')

    user = self.model(email=email.lower())

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password):
    user = self.create_user(email, password=password)
    user.is_staff = True
    user.is_active = True
    user.is_superuser = True
    user.save(using=self._db)
    return user


class EmailUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(
    verbose_name='email address',
    max_length=255,
    unique=True,
    db_index=True
  )
  first_name = models.CharField(max_length=36, blank=True, null=True)
  last_name = models.CharField(max_length=36, blank=True, null=True)
  date_of_birth = models.DateField(blank=True, null=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  USER_TYPE = (
      (1, 'Client'),
      (2, 'Coach'),
      (3, 'Admin')
  )
  user_type = models.IntegerField(choices=USER_TYPE, default=1, verbose_name='User type')

  coach = models.ForeignKey('self', blank=True, null=True, verbose_name='Coach')

  date_joined = models.DateTimeField(auto_now_add=True)

  objects = EmailUserManager()
  USERNAME_FIELD = 'email'

  def get_full_name(self):
    return '{0} {1}'.format(self.first_name, self.last_name)

  def get_short_name(self):
    return self.first_name

  def __unicode__(self):
    return self.email

