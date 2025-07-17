from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    bio=models.TextField()
    contact_email=models.EmailField()
    image=models.ImageField(upload_to='doctor_images/', blank=True)

    def __str__(self):
        return self.name
