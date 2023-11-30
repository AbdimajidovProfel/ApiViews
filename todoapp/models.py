from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=155, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    ended = models.BooleanField(default=False, verbose_name='Ended')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

