import os
import threading
import globalVarsTourney

def participate(a):
    a.pathCost = globalVarsTourney.pathCostAlg
    globalVarsTourney.windowNameAlg = a.name
    command = "python pacman.py -f -z 0.5 -l smallMaze -p SearchAgent -a fn="
    os.system(command + a.name)

def fight(a, b):
    print a.name + " vs " + b.name
    t1 = threading.Thread(target=participate, args=(a,))
    t2 = threading.Thread(target=participate, args=(b,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def roundRobin(algorithms):
    rounds = []
    for a in algorithms:
        for b in algorithms:
            if (not a.name == b.name) and ((a.name, b.name) not in rounds) and ((b.name, a.name) not in rounds):
                rounds.append((a.name, b.name))
                fight(a, b)
                if a.pathCost > b.pathCost:
                    b.roundsWin += 1
                    print b.name + " wins\n"
                elif a.pathCost < b.pathCost:
                    a.roundsWin += 1
                    print a.name + " wins\n"
                else:
                    if a.score < b.score:
                        a.roundsWin += 1
                        print a.name + " wins\n"
                    else:
                        b.roundsWin += 1
                        print b.name + " wins\n"
                # a.score = 0
                # b.score = 0
                # a.pathCost = 0
                # b.pathCost = 0

def beginTourney():
    roundRobin(globalVarsTourney.participants)

