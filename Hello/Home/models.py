from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=233)
    phone = models.CharField(max_length=20)
    desc = models.TextField()
    date_time = models.DateField()

    def __str__(self):
        return f"{self.name} / {self.email}"