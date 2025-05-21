from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cost = models.CharField(max_length=10)

    # characteristics
    M = models.CharField(max_length=10)
    T = models.CharField(max_length=10)
    SV = models.CharField(max_length=10)
    W = models.CharField(max_length=10)
    LD = models.CharField(max_length=10)
    OC = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Weapon(models.Model):
    character = models.ForeignKey(Character, related_name='weapons', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    range = models.CharField(max_length=50)
    A = models.CharField(max_length=10)
    WS = models.CharField(max_length=10)
    S = models.CharField(max_length=10)
    AP = models.CharField(max_length=10)
    D = models.CharField(max_length=10)
    keywords = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.character.name})"