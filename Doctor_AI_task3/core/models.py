from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Years of experience")
    email = models.EmailField()
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.name
