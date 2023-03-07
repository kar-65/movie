from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    post=models.ImageField(upload_to="posters")

    def __str__(self):
        return self.name