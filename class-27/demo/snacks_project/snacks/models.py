from django.db import models

class Snack(models.Model):
    name = models.CharField(max_length=64)
    rank = models.IntegerField(default=0)
    eater = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    