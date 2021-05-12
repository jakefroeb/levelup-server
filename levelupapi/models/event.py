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
    
    @property
    def player_count(self):
        return self.__player_count

    @player_count.setter
    def player_count(self, value):
        self.__player_count = value
