from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField() 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"
