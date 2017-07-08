class Player:

    names = []
    scores = []

    def name(self,f_name,l_name):
        Player.names.append([f_name,l_name])
        print("Name is",Player.names)
    def score(self,f_score):
        Player.scores.append(f_score)
        # print("Score is",Student.scores)
        print("Name : {}, Score : {}".format(Player.names,Player.scores))

player_1 = Player()
player_1.name("Sachin","Tendulkar")
player_1.score(88)


player_2 = Player()
player_2.name("Rahul","Dravid")
player_2.score(67)


print(player_1.scores)
print(player_2.scores)