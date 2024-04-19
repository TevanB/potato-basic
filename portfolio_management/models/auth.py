from django.db import models
from django.contrib.auth.models import User
from .holdings import Portfolio


class User(User):
    plan = models.TextField(default="Basic")
    holdings = models.ManyToManyField(Portfolio, related_name="owners")
