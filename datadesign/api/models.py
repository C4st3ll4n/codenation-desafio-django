from django.core import validators
from django.db import models


class User(models.Model):
    name = models.CharField("name", max_length=50)
    email = models.EmailField("email", max_length=254, validators=[validators.EmailValidator()])
    password = models.CharField("password", max_length=50, validators=[validators.MinValueValidator(8)])
    last_login = models.DateTimeField(auto_now=True)


class Agent(models.Model):
    name = models.CharField(name="name", max_length=50)
    status = models.BooleanField(name="status", default=False)
    env = models.CharField(name="env", max_length=20)
    version = models.CharField(name="version", max_length=5)
    address = models.GenericIPAddressField(protocol="IPV4", default="0.0.0.0")


class Event(models.Model):
    class Level(models.TextChoices):
        CRITICAL = "CRITICAL", "CRITICAL"
        DEBUG = "DEBUG", "DEBUG"
        ERROR = "ERROR", "ERROR"
        WARNING = "WARNING", "WARNING"
        INFO = "INFO", "INFO"

    level = models.CharField("level", max_length=20, choices=Level.choices, default=Level.INFO)
    data = models.TextField()
    arquivado = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Group(models.Model):
    name = models.CharField("name", max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
