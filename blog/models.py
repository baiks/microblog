from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, AbstractUser
from datetime import datetime


def file_timestamp():
    now = datetime.now()
    timestamp_str = now.strftime("%d%m%Y%H%M%S%f")
    return timestamp_str


def upload_path(instance, filename):
    timestamp_file = file_timestamp()
    return f"{timestamp_file}_{filename}"


class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=100, unique=True)
    image = models.FileField(upload_to=upload_path, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    objects = UserManager()

    class Meta:
        db_table = "users"
        managed = True


class Tweets(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, related_name="user_id", on_delete=models.CASCADE)
    tweet = models.CharField(max_length=140, null=False)

    class Meta:
        db_table = "tweets"
        managed = True


class Follows(models.Model):
    id = models.BigAutoField(primary_key=True)
    followed = models.ForeignKey(User, null=False, related_name="followed_id", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, null=False, related_name="follower_id", on_delete=models.CASCADE)

    class Meta:
        db_table = "follows"
        managed = True
