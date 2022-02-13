"""
Author: Nicholas Nguyen
Final Porject
File: squads.py


A class to hold onto and manage groups of enemies
"""
from random import randint
from slime import Slime
from golem import Golem
from vector2D import Vector2


SLIME_VELOCITY = 2
GOLEM_VELOCITY = 2


class Squads(object):

    @classmethod
    def slimeOverload(cls):
        slimeOverloadList = []
        for i in range(10):
            # Spawn 10 slimes in the top left of the map
            slimeOverloadList.append(Slime(Vector2(randint(0, 504),
                                                   randint(0, 504)),
                                     SLIME_VELOCITY))
        return slimeOverloadList

    @classmethod
    def golemAttack(cls):
        golemAttackList = []
        for i in range(3):
            golemAttackList.append(Golem(Vector2(randint(0, 1008),
                                                 randint(0, 1008)),
                                   GOLEM_VELOCITY))
        return golemAttackList

    @classmethod
    def golemAndSlimeOhNo(cls):
        golemAndSlimeOhNoList = []
        golemAndSlimeOhNoList.append(Golem(Vector2(randint(0, 1008),
                                                   randint(0, 1008)),
                                     GOLEM_VELOCITY))
        for i in range(5):
            golemAndSlimeOhNoList.append(Slime(Vector2(randint(0, 504),
                                                       randint(0, 504)),
                                         SLIME_VELOCITY))
        return golemAndSlimeOhNoList
