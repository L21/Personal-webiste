from django.db import models
# Create your models here.
class projects(models.Model):
    url = models.URLField()
    project_title = models.CharField(max_length=100)
    intro = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    index = models.IntegerField(default=0)

class myself(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    git_hub = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)



