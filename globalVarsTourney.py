

class Participant:
    name = ""
    score = 0
    pathCost = 0
    roundsWin = 0
    def __init__(self, name):
        self.name = name

    # def updateScore(self, score):
    #     self.score = score


bfs = Participant("bfs")
dfs = Participant("dfs")
ucs = Participant("ucs")
astar = Participant("astar")
participants = [bfs, dfs, ucs, astar]
pathCostAlg = -1
windowNameAlg = ""
algorithmRun = ""
scoreDisplayed = 0
