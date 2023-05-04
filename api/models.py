from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=120)
    completed = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        self.title