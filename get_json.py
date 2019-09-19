import json
import requests

class GetJson():
    def get_match_first_json(self, match_num):
        ### 試合事前情報を取得 ###
        token = { "Authorization": "procon30_example_token" }
        url = "http://localhost:8081/matches"
        all_matches_data = requests.get(url, headers=token).json()
        ########################

        return all_matches_data[match_num]

    def get_match_json(self, match_id):
        ### 試合情報を取得 ###
        token = { "Authorization": "procon30_example_token" }
        url = "http://localhost:8081/matches/{0}".format(match_id)
        all_matches_data = requests.get(url, headers=token).json()
        ########################
        
        ### 各試合情報の初期化 ###
        self.match_width = all_matches_data["width"]
        self.match_height = all_matches_data["height"]
        self.match_points = all_matches_data["points"]
        self.match_startedAtUnixTime = all_matches_data["startedAtUnixTime"]
        self.match_turn = all_matches_data["turn"]
        self.match_tiled = all_matches_data["tiled"]
        self.match_my_teamID = all_matches_data["teams"][0]["teamID"]
        self.match_my_agents = all_matches_data["teams"][0]["agents"]
        self.match_my_tilePoint = all_matches_data["teams"][0]["tilePoint"]
        self.match_my_areaPoint = all_matches_data["teams"][0]["areaPoint"]
        self.match_rival_teamID = all_matches_data["teams"][1]["teamID"]
        self.match_rival_agents = all_matches_data["teams"][1]["agents"]
        self.match_rival_tilePoint = all_matches_data["teams"][1]["tilePoint"]
        self.match_rival_areaPoint = all_matches_data["teams"][1]["areaPoint"]
        self.match_actions = all_matches_data["actions"]
        #########################

    def width(self):
        return self.match_width
    def height(self):
        return self.match_height
    def points(self):
        return self.match_points
    def startedAtUnixTime(self):
        return self.match_startedAtUnixTime
    def turn(self):
        return self.match_turn
    def tiled(self):
        return self.match_tiled
    def my_teamID(self):
        return self.match_my_teamID
    def my_agents(self):
        return self.match_my_agents
    def my_tilePoint(self):
        return self.match_my_tilePoint
    def my_areaPoint(self):
        return self.match_my_areaPoint
    def rival_teamID(self):
        return self.match_rival_teamID
    def rival_agents(self):
        return self.match_rival_agents
    def rival_tilePoint(self):
        return self.match_rival_tilePoint
    def rival_areaPoint(self):
        return self.match_rival_areaPoint
    def actions(self):
        return self.match_actions