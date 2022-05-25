from django.db import models


class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    todo_date = models.DateField()
