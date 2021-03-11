from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    register = models.CharField(max_length=15, blank=False)
 
    def __str__(self):
        return self.first_name