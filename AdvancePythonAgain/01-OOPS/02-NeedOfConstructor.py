class Player:

    def __init__(self):
        self.player_name = []
        self.scores = []

    def name(self,p_name):
        self.player_name.append(p_name)
        print("Name is",self.player_name)
    def score_card(self,f_score):
        self.scores.append(f_score)
        # print("Score is",Student.scores)
        print("Name : {}, Score : {}".format(self.player_name,self.scores))

player_1 = Player()
player_1.name("Sachin Tendulkar")
player_1.score_card(88)

player_2 = Player()
player_2.name("Rahul Dravid")
player_2.score_card(67)


print(player_1.scores)
print(player_2.scores)