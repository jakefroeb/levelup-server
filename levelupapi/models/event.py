from django.db import models
from .game import Game
from .gamer import Gamer

class Event(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    host = models.ForeignKey(Gamer, on_delete=models.CASCADE)

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value