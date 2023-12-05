import common

def d2(filename,puzzle):
    final_array=[]

    limit_dict = {
            "red": 12,
            "blue": 14,
            "green": 13
            }

    lines = common.read_lines(filename)
    for line in lines:
        game_pass = True
        value_dict = {
            "blue": 0,
            "red": 0,
            "green": 0
        }
        linearray = line.split(':')
        game_id = linearray[0].split()[1]
        games = linearray[1].split(";")
        for game in games:
            stages = game.split(',')
            for stage in stages:
                number = int(stage.split()[0])
                colour = stage.split()[1]
                if puzzle == 1:
                    if number > limit_dict[colour]:
                        game_pass = False
                else:
                    if number > value_dict[colour]:
                        value_dict.update({colour:number})
        if puzzle == 1:
            if game_pass:
                final_array.append(int(game_id))
        else:
            power = int(value_dict["red"] * value_dict["blue"] * value_dict["green"])
            final_array.append(power)

    total = 0
    for i in final_array:
        total = total+i
    print("Puzzle %s: %s" %(puzzle,total))
