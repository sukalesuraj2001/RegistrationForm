from django.db import models

# Create your models here.


class ApplicationForm(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name