# -*- coding: utf-8 -*-
from get_json import GetJson
from termcolor import colored, cprint
import colorama
colorama.init()

class Visualizar():
    def __init__(self, match, match_id):
        get_field = GetJson(match)
        get_field.get_match_json(match_id)

        self.turn = get_field.turn()
        self.field = get_field.tiled()
        self.my_id = get_field.my_teamID()
        self.rival_id = get_field.rival_teamID()
        self.my_tilepoint = get_field.my_tilePoint()
        self.my_areapoint = get_field.my_areaPoint()
        self.rival_tilepoint = get_field.rival_tilePoint()
        self.rival_areapoint = get_field.rival_areaPoint()
        self.my_agents = get_field.my_agents()
        self.rival_agents = get_field.rival_agents()
        self.actions = get_field.actions()
    
    def print_field(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j] == self.my_id:
                    cprint(str(self.field[i][j]) + "   ", "red", end="")
                elif self.field[i][j] == self.rival_id:
                    cprint(str(self.field[i][j]) + "   ", "blue", end="")
                else:
                    cprint(str(self.field[i][j]) + "   ", "white", end="")
            print("\n")