from django.db import models
from django.contrib.auth.models import User

class FishingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.date} at {self.location}"

FISH_SPECIES_CHOICES = [
    ('pike', 'Pike'),
    ('perch', 'Perch'),
    ('trout', 'Trout'),
    ('zander', 'Zander'),
    ('salmon', 'Salmon'),
    ('roach', 'Roach'),
    ('tench', 'Tench'),
    ('other', 'Other')
]

class Catch(models.Model):
    session = models.ForeignKey(FishingSession, on_delete=models.CASCADE, related_name='catches')
    species = models.CharField(max_length=50, choices=FISH_SPECIES_CHOICES)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.species} x {self.count}"