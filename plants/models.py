from django.db import models

class Plant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, default='')
    species = models.CharField(max_length=128)
    image_url = models.CharField(max_length=256, blank=True, default='')
    date = models.DateField()
    watering_frequency = models.IntegerField()
    
    def __str__(self):
        return self.name if self.name else self.species