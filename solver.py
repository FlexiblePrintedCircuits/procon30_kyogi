from get_json import GetJson
from send_json import SendJson
import random

class Solver():
    def __init__(self, field, my_num, rival_num, agents):
        ### 各種変数の初期化 ###
        self.field = field
        self.my_num = my_num
        self.rival_num = rival_num
        self.agents = agents
        #######################
    
    def solve(self):
        agents = self.agents
        action_dic = {"actions": []}

        ### 行動情報を辞書に格納 ###
        for i in agents:
            agent_action = MonteCarlo(self.field, i["x"] - 1, i["y"] - 1, self.my_num, self.rival_num)
            action = agent_action.playout()
            try:
                if action == "right":
                    if self.field[i["y"] - 1][i["x"]] == self.rival_num:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "remove", "dx": 1, "dy": 0})
                    else:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "move", "dx": 1, "dy": 0})
                elif action == "left":
                    if self.field[i["y"] - 1][i["x"] - 2] == self.rival_num:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "remove", "dx": -1, "dy": 0})
                    else:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "move", "dx": -1, "dy": 0})
                elif action == "up":
                    if self.field[i["y"] - 2][i["x"] - 1] == self.rival_num:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "remove", "dx": 0, "dy": 1})
                    else:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "move", "dx": 0, "dy": 1})
                elif action == "down":
                    if self.field[i["y"]][i["x"] - 1] == self.rival_num:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "remove", "dx": 0, "dy": -1})
                    else:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "move", "dx": 0, "dy": -1})
                elif action == "right_up":
                    if self.field[i["y"] - 2][i["x"]] == self.rival_num:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "remove", "dx": 1, "dy": 1})
                    else:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "move", "dx": 1, "dy": 1})
                elif action == "right_down":
                    if self.field[i["y"]][i["x"]] == self.rival_num:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "remove", "dx": 1, "dy": -1})
                    else:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "move", "dx": 1, "dy": -1})
                elif action == "left_up":
                    if self.field[i["y"] - 2][i["x"] - 2] == self.rival_num:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "remove", "dx": -1, "dy": 1})
                    else:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "move", "dx": -1, "dy": 1})
                elif action == "left_down":
                    if self.field[i["y"]][i["x"] - 2] == self.rival_num:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "remove", "dx": -1, "dy": -1})
                    else:
                        action_dic["actions"].append({"agentID": i["agentID"], "type": "move", "dx": -1, "dy": -1})
            except:
                action_dic["actions"].append({"agentID": i["agentID"], "type": "stay", "dx": 0, "dy": 0})
        ###########################

        return action_dic

class MonteCarlo():
    def __init__(self, field, x, y, my_num, rival_num):
        ### 各種変数の初期化 ###
        self.field = field
        # [プレイアウト回数, 勝った回数, UCB1]
        self.wood = {"right": [0, 0, 0.0], "left": [0, 0, 0.0], "up": [0, 0, 0.0], "down": [0, 0, 0.0], "right_up": [0, 0, 0.0], "right_down": [0, 0, 0.0], "left_up": [0, 0, 0.0], "left_down": [0, 0, 0.0]}
        self.x = x
        self.y = y
        self.my_num = my_num
        self.rival_num = rival_num
        ######################

    def playout(self):
        ### 各種変数の初期化 ###
        field = self.field
        x = self.x  #自分チームのエージェントの座標
        y = self.y
        rx = None  #相手チームのエージェントの座標（初期状態）
        ry = None
        #######################

        for m in ["right", "left", "up", "down", "right_up", "right_down", "left_up", "left_down"]:
            field = self.field
            
            if m == "right":
                try:
                    field[y][x + 1] = self.my_num
                    x += 1
                except:
                    pass
            elif m == "left":
                try:
                    field[y][x - 1] = self.my_num
                    x -= 1
                except:
                    pass
            elif m == "up":
                try:
                    field[y - 1][x] = self.my_num
                    y -= 1
                except:
                    pass
            elif m == "down":
                try:
                    field[y + 1][x] = self.my_num
                    y += 1
                except:
                    pass
            elif m == "right_up":
                try:
                    field[y - 1][x + 1] = self.my_num
                    y -= 1
                    x += 1
                except:
                    pass
            elif m == "right_down":
                try:
                    field[y + 1][x + 1] = self.my_num
                    y += 1
                    x += 1
                except:
                    pass
            elif m == "left_up":
                try:
                    field[y - 1][x - 1] = self.my_num
                    y -= 1
                    x -= 1
                except:
                    pass
            elif m == "left_down":
                try:
                    field[y + 1][x - 1] = self.my_num
                    y += 1
                    x -= 1
                except:
                    pass

            ### 30回のプレイアウトを実施 ###
            for i in range(30):
                i += 1
                ### 相手チームエージェントの座標を適当に取得 ###
                for j in range(len(field)):
                    for k in range(len(field[0])):
                        if field[j][k] == self.rival_num:
                            rx = k
                            ry = j
                    if rx != None:
                        break
                #############################################

                ### プレイアウトを実施 ###
                for j in range(40):
                    if i % 2 == 0:
                        field = self.my_play(field, x, y)
                    else:
                        field = self.rival_play(field, rx, ry)
                #########################

                ### 勝敗記録 ###
                self.wood[m][0] += 1
                self.wood[m][1] += self.win(field)
                self.wood[m][2] = self.wood[m][1] / self.wood[m][0]
                ###############
            
            ################################
        
        ### 最も勝率の高い手を返す ###
        max_probability = self.wood["right"][2]
        max_probability_key = "right"
        for key, value in self.wood.items():
            if value[2] > max_probability:
                max_probability = value[2]
                max_probability_key = key
        
        return max_probability_key
        ############################

    def my_play(self, field, x, y):
        actions = ["右", "左", "上", "下", "右上", "右下", "左上", "左下"]
        action = random.choice(actions)
        if action == "右":
            try:
                if field[y][x + 1] == self.rival_num:
                    field[y][x + 1] = 0
                elif field[y][x + 1] == 0:
                    field[y][x + 1] = self.my_num
                    x += 1
            except:
                pass
        elif action == "左":
            try:
                if field[y][x - 1] == self.rival_num:
                    field[y][x - 1] = 0
                elif field[y][x - 1] == 0:
                    field[y][x - 1] = self.my_num
                    x -= 1
            except:
                pass
        elif action == "上":
            try:
                if field[y - 1][x] == self.rival_num:
                    field[y - 1][x] = 0
                elif field[y - 1][x] == 0:
                    field[y - 1][x] = self.my_num
                    y -= 1
            except:
                pass
        elif action == "下":
            try:
                if field[y + 1][x] == self.rival_num:
                    field[y + 1][x] = 0
                elif field[y + 1][x] == 0:
                    field[y + 1][x] = self.my_num
                    y += 1
            except:
                pass
        elif action == "右上":
            try:
                if field[y - 1][x + 1] == self.rival_num:
                    field[y - 1][x + 1] = 0
                elif field[y - 1][x + 1] == 0:
                    field[y - 1][x + 1] = self.my_num
                    y -= 1
                    x += 1
            except:
                pass
        elif action == "右下":
            try:
                if field[y + 1][x + 1] == self.rival_num:
                    field[y + 1][x + 1] = 0
                elif field[y + 1][x + 1] == 0:
                    field[y + 1][x + 1] = self.my_num
                    y += 1
                    x += 1
            except:
                pass
        elif action == "左上":
            try:
                if field[y - 1][x - 1] == self.rival_num:
                    field[y - 1][x - 1] = 0
                elif field[y - 1][x - 1] == 0:
                    field[y - 1][x - 1] = self.my_num
                    y -= 1
                    x -= 1
            except:
                pass
        elif action == "左下":
            try:
                if field[y + 1][x - 1] == self.rival_num:
                    field[y + 1][x - 1] = 0
                elif field[y + 1][x - 1] == 0:
                    field[y + 1][x - 1] = self.my_num
                    y += 1
                    x -= 1
            except:
                pass

        return field

    def rival_play(self, field, x, y):
        actions = ["右", "左", "上", "下", "右上", "右下", "左上", "左下"]
        action = random.choice(actions)
        if action == "右":
            try:
                if field[y][x + 1] == self.my_num:
                    field[y][x + 1] = 0
                elif field[y][x + 1] == 0:
                    field[y][x + 1] = self.rival_num
                    x += 1
            except:
                pass
        elif action == "左":
            try:
                if field[y][x - 1] == self.my_num:
                    field[y][x - 1] = 0
                elif field[y][x - 1] == 0:
                    field[y][x - 1] = self.rival_num
                    x -= 1
            except:
                pass
        elif action == "上":
            try:
                if field[y - 1][x] == self.my_num:
                    field[y - 1][x] = 0
                elif field[y - 1][x] == 0:
                    field[y - 1][x] = self.rival_num
                    y -= 1
            except:
                pass
        elif action == "下":
            try:
                if field[y + 1][x] == self.my_num:
                    field[y + 1][x] = 0
                elif field[y + 1][x] == 0:
                    field[y + 1][x] = self.rival_num
                    y += 1
            except:
                pass
        elif action == "右上":
            try:
                if field[y - 1][x + 1] == self.my_num:
                    field[y - 1][x + 1] = 0
                elif field[y - 1][x + 1] == 0:
                    field[y - 1][x + 1] = self.rival_num
                    y -= 1
                    x += 1
            except:
                pass
        elif action == "右下":
            try:
                if field[y + 1][x + 1] == self.my_num:
                    field[y + 1][x + 1] = 0
                elif field[y + 1][x + 1] == 0:
                    field[y + 1][x + 1] = self.rival_num
                    y += 1
                    x += 1
            except:
                pass
        elif action == "左上":
            try:
                if field[y - 1][x - 1] == self.my_num:
                    field[y - 1][x - 1] = 0
                elif field[y - 1][x - 1] == 0:
                    field[y - 1][x - 1] = self.rival_num
                    y -= 1
                    x -= 1
            except:
                pass
        elif action == "左下":
            try:
                if field[y + 1][x - 1] == self.my_num:
                    field[y + 1][x - 1] = 0
                elif field[y + 1][x - 1] == 0:
                    field[y + 1][x - 1] = self.rival_num
                    y += 1
                    x -= 1
            except:
                pass
        
        return field
    
    def win(self, field):
        my_tile = 0
        rival_tile = 0
        for i in field:
            for j in i:
                if j == self.my_num:
                    my_tile += 1
                elif j == self.rival_num:
                    rival_tile += 1
        if my_tile > rival_tile:
            return 1
        else:
            return 0