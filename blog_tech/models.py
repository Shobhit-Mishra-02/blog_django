from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    desc = models.TextField()
    content = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.title