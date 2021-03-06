from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150, blank=False)
    writer = models.CharField(max_length=150, blank=True)
    reserved = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title