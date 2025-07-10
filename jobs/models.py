from django.db import models
# jobs/models.py
from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()

    def __str__(self):
        return self.job_title

# Create your models here.
