from django.db import models

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    rank = models.IntegerField(default=1)
    eater = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name




# Snack tables
#     chocolate   jb
#     chips       iris
#     apples      vij

