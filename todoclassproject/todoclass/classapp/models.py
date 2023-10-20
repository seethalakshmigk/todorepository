from django.db import models


class TodoModel(models.Model):
    name = models.CharField(max_length=60)
    priority = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name

