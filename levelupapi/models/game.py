from django.db import models
from .game_type import Game_Type

class Game(models.Model):
    name = models.CharField(max_length=50, default="")
    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE, null=True)
