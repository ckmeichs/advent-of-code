class CubeConundrum():
    def __init__(self, content) -> None:
        self.sum = 0
        self.sum_2 = 0
        self.games = []
        self.max_cubes = {
            "red": 12,
            "green": 13,
            "blue": 14
        }

        for line in content:
            split_str = line.split(":")
            game_id = int(split_str[0].replace("Game ", ""))
            game_strings = split_str[1].split(";")
            game = []
            for game_str in game_strings:
                take = []
                cube_strings = game_str.split(",")
                for cube_str in cube_strings:
                    cube_data = cube_str.split(" ")
                    cube_dict = {
                        "color": cube_data[2],
                        "number": int(cube_data[1])
                    }
                    take.append(cube_dict)
                game.append(take)
            self.games.append(
                {
                    "id": game_id,
                    "game": game
                }
            )
        
    def possible_games(self):
        for game in self.games:
            game_possible = True
            for takes in game["game"]:
                for take in takes:
                    if take["number"] > self.max_cubes[take["color"]]:
                        game_possible = False
            if game_possible:
                self.sum = self.sum + game["id"]
        return self.sum 

    def required_cubes(self):
        for game in self.games:
            min_cubes = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for takes in game["game"]:
                for take in takes:
                    if min_cubes[take["color"]] < take["number"]:
                        min_cubes[take["color"]] = take["number"]
            power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
            self.sum_2 = self.sum_2 + power
        return self.sum_2
    