class Scratchcards():
    def __init__(self, content) -> None:
        self.content = content
        self.cards = []
        self.num_scretchcards = 0
        
        for line in self.content:
            card_string = line.split(":")[0]
            card_id = int(card_string.split(" ")[-1]) - 1
            point_strings = line.split(":")[1]

            win_points_strint = point_strings.split("|")[0]
            my_points_string = point_strings.split("|")[1]
            
            win_points = win_points_strint.split(" ")
            my_points = my_points_string.split(" ")
            
            win_point_list = []
            my_point_list = []
            
            for point in win_points:
                if len(point) > 0:
                    win_point_list.append(int(point))
                    
            for point in my_points:
                if len(point) > 0:
                    my_point_list.append(int(point))
                       
            card = {
                "id": card_id,
                "win_points": win_point_list,
                "my_points": my_point_list,
            }
            self.cards.append(card) 
    
    def points(self):
        points = 0
        for card in self.cards:
            winning_points = 0
            for my_point in card["my_points"]:
                if my_point in card["win_points"]:
                    if winning_points == 0:
                        winning_points = 1
                    else:
                        winning_points = winning_points * 2
            points = points + winning_points
        return points
    
    def scretchcards(self):
        for card in self.cards:
            self.num_scretchcards = self.num_scretchcards + 1             
            matches = self.card_matches(card)
            if matches > 0:
                self.get_new_cards(card["id"], matches)
        return self.num_scretchcards
    
    def get_new_cards(self, card_id, number):
        for i in range(1, number + 1):
            self.num_scretchcards = self.num_scretchcards + 1
            self.get_new_cards(card_id + i, self.card_matches(self.cards[card_id + i]))
            
    def card_matches(self, card):
        matches = 0
        for my_point in card["my_points"]:
            if my_point in card["win_points"]:
                matches = matches + 1
        return matches