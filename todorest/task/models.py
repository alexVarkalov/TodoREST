from __future__ import unicode_literals

from django.db import models

import arrow


class Task(models.Model):
    status = models.BooleanField(default=False)
    task = models.CharField(max_length=30)
    queue = models.IntegerField(default=arrow.utcnow().timestamp)

    owner = models.ForeignKey('auth.User', related_name='tasks')