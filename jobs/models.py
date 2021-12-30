from django.db import models

class Project(models.Model):
    
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return self.title