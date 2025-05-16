from django.db import models

class SearchHistory(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city.title()}, {self.country.title()} at {self.searched_at}"

class TemperatureLog(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    temperature = models.CharField(max_length=20)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city.title()} - {self.temperature} at {self.recorded_at}"
