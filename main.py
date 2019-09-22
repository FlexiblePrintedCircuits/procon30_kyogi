from send_json import SendJson
from get_json import GetJson
from solver import Solver
from visualizar import Visualizar

print("######################################################################")
print("")
print("ププププププ   プププ    ロロロロロロロ    ココココココ      ンンン　　 ン")
print("         プ   プ  プ    ロ         ロ               コ               ン")
print("        プ    プププ    ロ         ロ               コ              ン")
print("       プ              ロ         ロ               コ             ン ")
print("   ププ                ロロロロロロロ     コココココ             ン")
print("")
print("#####################################################################")
print("\n\n")

match = int(input("試合順番？："))
match_data = GetJson(match)
match_id = match_data.team_id()

while True:
    while True:
        if input("フィールド情報を取得？:") == "1":
            break
    
    match_data.get_match_json(match_id)

    field = Visualizar(match, match_id)
    field.print_field()

    print("現在のターン：{0}".format(match_data.turn()))
    print("タイルポイント：{0}".format(match_data.my_tilePoint()))
    print("領域ポイント：{0}".format(match_data.my_areaPoint()))

    while True:
        if input("ソルブ？：") == "1":
            break
    
    solve_object = Solver(match_data.tiled(), match_data.my_teamID(), match_data.rival_teamID(), match_data.my_agents())
    action = solve_object.solve()
    print(action)

    while True:
        if input("送信？：") == "1":
            break

    try:
        SendJson.send(match_id, action)
        print("OK  次のターンに移ります")
    except:
        print("何らかのエラーが起きました。このターンは停留となります。")
        print("次のターンに移ります")