# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import globalVarsTourney


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    globalVarsTourney.algorithmRun = "dfs"
    solution = []
    succ = util.Stack()
    globalVarsTourney.dfs.score += 1
    succ.push((problem.getStartState(), [], []))
    while not succ.isEmpty():
        globalVarsTourney.dfs.score += 2
        pos, direc, visited = succ.pop()
        if problem.isGoalState(pos):
            print "DFS operations = ", globalVarsTourney.dfs.score
            globalVarsTourney.scoreDisplayed = globalVarsTourney.dfs.score
            return direc
        for position, direction, x in problem.getSuccessors(pos):
            globalVarsTourney.dfs.score += 1
            if not position in visited:
                globalVarsTourney.dfs.score += 2
                succ.push((position, direc + [direction], visited + [pos]))
                solution = direc + [direction]

    print "the solution is ", solution
    return solution


def breadthFirstSearch(problem):
    globalVarsTourney.algorithmRun = "bfs"
    solution = []
    succ = util.Queue()
    globalVarsTourney.bfs.score += 1
    succ.push((problem.getStartState(), [], []))
    while not succ.isEmpty():
        globalVarsTourney.bfs.score += 2
        pos, direc, visited = succ.pop()
        if problem.isGoalState(pos):
            print "BFS operations = ", globalVarsTourney.bfs.score
            globalVarsTourney.scoreDisplayed = globalVarsTourney.bfs.score
            return direc
        for position, direction, x in problem.getSuccessors(pos):
            globalVarsTourney.bfs.score += 1
            if not position in visited:
                globalVarsTourney.bfs.score += 2
                succ.push((position, direc + [direction], visited + [pos]))
                solution = direc + [direction]

    print "the solution is ", solution
    return solution


def uniformCostSearch(problem):
    globalVarsTourney.algorithmRun = "ucs"
    """Search the node of least total cost first."""
    "* YOUR CODE HERE *"
    current = problem.getStartState()
    path_cost = 0
    actions = []
    visited = set()
    stack = util.PriorityQueue()
    globalVarsTourney.ucs.score += 1
    stack.push((current, actions, path_cost), problem.getStartState()[-1])
    while (not stack.isEmpty()):
        globalVarsTourney.ucs.score += 2
        (state, actions, path_cost) = stack.pop()
        if (state not in visited):
            globalVarsTourney.ucs.score += 2
            visited.add(state)
            if problem.isGoalState(state):
                print "UCS operations = ", globalVarsTourney.ucs.score
                globalVarsTourney.scoreDisplayed = globalVarsTourney.ucs.score
                return actions
            globalVarsTourney.ucs.score += 1
            succ = problem.getSuccessors(state)
            for nextState, nextActions, nextCost in succ:
                globalVarsTourney.ucs.score += 1
                stack.push((nextState, actions + [nextActions], nextCost + path_cost), nextCost + path_cost)

    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    globalVarsTourney.algorithmRun = "astar"
    """Search the node that has the lowest combined cost and heuristic first."""
    "* YOUR CODE HERE *"
    starterPos = problem.getStartState()
    frontier = util.PriorityQueue()
    visited = []
    globalVarsTourney.astar.score += 3
    frontier.push((starterPos, [], 0), 0 + heuristic(starterPos, problem))
    (state, direction, toCost) = frontier.pop()
    visited.append((state, toCost + heuristic(starterPos, problem)))

    while not problem.isGoalState(state):
        globalVarsTourney.astar.score += 2
        successors = problem.getSuccessors(state)
        for suc in successors:
            globalVarsTourney.astar.score += 3
            visitedExist = False
            total_cost = toCost + suc[2]
            for (visitedState, visitedToCost) in visited:
                if (suc[0] == visitedState) and (total_cost >= visitedToCost):
                    globalVarsTourney.astar.score += 1
                    visitedExist = True
                    break
            if not visitedExist:
                globalVarsTourney.astar.score += 2
                frontier.push((suc[0], direction + [suc[1]], toCost + suc[2]),
                              toCost + suc[2] + heuristic(suc[0], problem))
                visited.append((suc[0], toCost + suc[2]))

        (state, direction, toCost) = frontier.pop()
    print "ASTAR operations = ", globalVarsTourney.astar.score
    globalVarsTourney.scoreDisplayed = globalVarsTourney.astar.score
    return direction

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch




