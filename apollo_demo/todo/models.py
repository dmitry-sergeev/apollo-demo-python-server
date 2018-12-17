# -*- coding: utf-8 -*-
from django.db import models


class TodoNote(models.Model):
    note = models.CharField(max_length=1000)

    def __str__(self):
        return self.note
