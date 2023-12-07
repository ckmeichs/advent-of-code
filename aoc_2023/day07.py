from functools import cmp_to_key

class CamelCards:
    def __init__(self, content) -> None:
        self.hands = []
        
        for line in content:
            line_parts = line.split(" ")
            hand = line_parts[0]
            bid = int(line_parts[1])
            self.hands.append(
                {
                    "hand": hand,
                    "bid": bid,
                    "type": "High card",
                    "value": 0
                }
            )
        
        self.cards = ["2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"T" ,"J" ,"Q" ,"K" ,"A"]
        self.joker_cards = ["J" ,"2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"T" ,"Q" ,"K" ,"A"]
        self.hand_types = ["High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind"]
            
    def total_winnings(self, joker=False):
        win = 0
        
        for hand in self.hands:
            if joker:
                proc_hand = self.get_proc_hand(type="joker", hand=hand)
                value = self.get_hand_value_joker(proc_hand=proc_hand)
            else:
                proc_hand = self.get_proc_hand(type="standard", hand=hand)
                value = self.get_hand_value(proc_hand=proc_hand)
            hand["value"] = value
            hand["type"] = self.hand_types[value]
               
        sorted_final = []
        for hand_type in reversed(self.hand_types):
            hand_type_list = []
            for hand in self.hands:
                if hand_type == hand["type"]:
                    hand_type_list.append(hand)
            if joker:
                sorted_hand_type_list = sorted(hand_type_list, key=cmp_to_key(self.compare_equal_value_hands_joker), reverse=True)
            else:
                sorted_hand_type_list = sorted(hand_type_list, key=cmp_to_key(self.compare_equal_value_hands), reverse=True)
            sorted_final += sorted_hand_type_list
        
        factor = len(sorted_final)         
        for hand in sorted_final:
            win += (hand["bid"] * factor)
            factor -= 1
            
        return win
    
    def get_proc_hand(self, type, hand):
        proc_hand = []
        if type == "standard":
            cards = self.cards
        elif type == "joker":
            cards = self.joker_cards
                
        for card in cards:
            proc_hand.append({"card": card, "num": 0})
            
        for card in hand["hand"]:
            for proc_card in proc_hand:
                if card == proc_card["card"]:
                    proc_card["num"] += 1                               
        return proc_hand
    
    def get_hand_value(self, proc_hand):
        sorted_proc_hand = sorted(proc_hand, key=lambda k: k['num'], reverse=True)
        if sorted_proc_hand[0]["num"] == 5:
            return 6
        if sorted_proc_hand[0]["num"] == 4:
            return 5
        if sorted_proc_hand[0]["num"] == 3 and sorted_proc_hand[1]["num"] == 2:
            return 4
        if sorted_proc_hand[0]["num"] == 3 and sorted_proc_hand[1]["num"] == 1 and sorted_proc_hand[2]["num"] == 1:
            return 3
        if sorted_proc_hand[0]["num"] == 2 and sorted_proc_hand[1]["num"] == 2 and sorted_proc_hand[2]["num"] == 1:
            return 2
        if sorted_proc_hand[0]["num"] == 2 and sorted_proc_hand[1]["num"] == 1 and sorted_proc_hand[2]["num"] == 1 and sorted_proc_hand[3]["num"] == 1:
            return 1
        return 0
               
    def compare_equal_value_hands(self, ha, hb):
        for i in range(0, 5):
            if self.cards.index(ha["hand"][i]) < self.cards.index(hb["hand"][i]):
                return -1
            elif self.cards.index(ha["hand"][i]) > self.cards.index(hb["hand"][i]):
                return 1
        return 0
    
    def get_hand_value_joker(self, proc_hand):
        jokers = proc_hand[0]["num"]
        proc_hand.pop(0)
        sorted_proc_hand = sorted(proc_hand, key=lambda k: k['num'], reverse=True)
        
        if sorted_proc_hand[0]["num"] + jokers == 5:
            return 6
        if sorted_proc_hand[0]["num"] + jokers == 4:
            return 5
        if sorted_proc_hand[0]["num"] + jokers == 3 and sorted_proc_hand[1]["num"] == 2:
            return 4
        if sorted_proc_hand[0]["num"] + jokers == 3 and sorted_proc_hand[1]["num"] == 1 and sorted_proc_hand[2]["num"] == 1:
            return 3         
        if sorted_proc_hand[0]["num"] == 2 and sorted_proc_hand[1]["num"] == 2 and sorted_proc_hand[2]["num"] == 1:
            return 2
        if sorted_proc_hand[0]["num"] == 2 and sorted_proc_hand[1]["num"] == 1 and sorted_proc_hand[2]["num"] == 1 and sorted_proc_hand[3]["num"] == 1:
            return 1
        if sorted_proc_hand[0]["num"] + jokers == 2:
            return 1
        return 0
    
    def compare_equal_value_hands_joker(self, ha, hb):
        for i in range(0, 5):
            if self.joker_cards.index(ha["hand"][i]) < self.joker_cards.index(hb["hand"][i]):
                return -1
            elif self.joker_cards.index(ha["hand"][i]) > self.joker_cards.index(hb["hand"][i]):
                return 1
        return 0
        