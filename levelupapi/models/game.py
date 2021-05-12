from django.db import models
from .game_type import Game_Type

class Game(models.Model):
    name = models.CharField(max_length=50, default="")
    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE, null=True)

    @property
    def event_count(self):
        return self.__event_count

    @event_count.setter
    def event_count(self, value):
        self.__event_count = value
        
    @property
    def user_event_count(self):
        return self.__user_event_count

    @user_event_count.setter
    def user_event_count(self, value):
        self.__user_event_count = value
