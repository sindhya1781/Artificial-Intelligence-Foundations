#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    node = problem.getStartState();
    if problem.isGoalState(node) == True:
        return [];

    dfs_frontier_Stack = util.Stack();
    util.Stack.push(dfs_frontier_Stack, (node, []));

    flag = 0;
    dfs_explored = [];

    while util.Stack.isEmpty(dfs_frontier_Stack) == False and flag == 0:
        node, actions = util.Stack.pop(dfs_frontier_Stack);
        if node not in dfs_explored:
            dfs_explored.append(node);
            if problem.isGoalState(node) == True:
                flag = 1;
                return actions;
            elif problem.isGoalState(node) == False:
                for successor, action, cost in problem.getSuccessors(node):
                    new_action = actions + [action];
                    util.Stack.push(dfs_frontier_Stack, (successor, new_action));
    util.raiseNotDefined();    
    
    """
    Q1. The Pacman board will show an overlay of the states explored, and the order in which they were explored 
    (brighter red means earlier exploration). Is the exploration order what you would have expected? Does Pacman 
    actually go to all the explored squares on his way to the goal?
    
    Answer 1.
    The exploration order that I noticed was different from what I was expecting to see on the screen. I was expecting
    the pacman to go through every square that it had explored as is with DFS before reaching the optimal path. However, 
    it did not go through all the squares, it only went through select squares which led to the optimal path.
    
    I believe this can be attributed to the fact that we append the action to each successor that led us to the successor
    which means that irrespective of how many squares were actually traversed for dfs, when we reach the goal state, the
    path contains only the actions which led us to the goal state.
    
    """
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    node = problem.getStartState();
    tmp = (node, []);
    dfs_frontier_Queue = util.Queue();
    util.Queue.push(dfs_frontier_Queue, tmp);
    flag = 0;
    dfs_explored = [];

    dfs_frontier_check = [];
    dfs_frontier_check.append(tmp[0]);

    while util.Queue.isEmpty(dfs_frontier_Queue) == False and flag == 0:
        node = util.Queue.pop(dfs_frontier_Queue);
        actions = node[1];
        if problem.isGoalState(node[0]) == True:
            flag = 1;
            return actions;
        elif problem.isGoalState(node[0]) == False:
            for successor in problem.getSuccessors(node[0]):
                if successor[0] not in dfs_explored and successor[0] not in dfs_frontier_check:
                    new_action = actions + [successor[1]];
                    util.Queue.push(dfs_frontier_Queue, (successor[0], new_action));
                    dfs_frontier_check.append(successor[0]);
    
    util.raiseNotDefined();

    """
    Q2. Does BFS find a least cost solution? If not, check your implementation.
    Answer 1.
    
    Yes, BFS finds a least cost solution for Pacman.
    
    """
    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    print ("Entering ucs");
    node = problem.getStartState();
    dfs_frontier_Queue = util.PriorityQueue();
    util.PriorityQueue.push(dfs_frontier_Queue, (node, [], 0), 0);

    dfs_explored = [];
    dfs_frontier_check = [];
    dfs_frontier_check.append(node);
    frontier_cost = {};
    flag = 0;
    
    while util.PriorityQueue.isEmpty(dfs_frontier_Queue) == False and flag == 0:
        node, actions, tmp_cost = util.PriorityQueue.pop(dfs_frontier_Queue);
        if node not in dfs_explored:
            dfs_explored.append(node);
            
            if problem.isGoalState(node) == True:
                flag = 1;
                return actions;

            elif problem.isGoalState(node) == False:
                successors = problem.getSuccessors(node);
                for successor in successors:
                    print ("Successor ", successor)
                    succ_node = successor[0];
                    action = successor[1];
                    cost = successor[2];
                    newAction = actions + [action];
                    newCost = tmp_cost + cost;
                    temp_node = (succ_node, newAction, newCost);
                    if type(succ_node) == tuple:
                        if type(succ_node[1]) == list:
                            succ_node = succ_node[0];
                    if succ_node not in dfs_explored:
                        if succ_node not in dfs_frontier_check:
                            util.PriorityQueue.push(dfs_frontier_Queue, temp_node, newCost);
                            dfs_frontier_check.append(succ_node);
                            frontier_cost[succ_node] = newCost;
                        else:
                            if frontier_cost[succ_node] >= newCost: 
                                util.PriorityQueue.update(dfs_frontier_Queue, temp_node, newCost);
                            frontier_cost[succ_node] = newCost;
                        
    util.raiseNotDefined()          


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    print ("Entering ASTAR");
    node = problem.getStartState();
    dfs_frontier_Queue = util.PriorityQueue();
    util.PriorityQueue.push(dfs_frontier_Queue, (node, [], 0), heuristic(node, problem));

    dfs_explored = [];
    dfs_frontier_check = [];
    dfs_frontier_check.append(node);
    frontier_cost = {};
    flag = 0;
    
    while util.PriorityQueue.isEmpty(dfs_frontier_Queue) == False and flag == 0:
        node, actions, tmp_cost = util.PriorityQueue.pop(dfs_frontier_Queue);
        if node not in dfs_explored:
            dfs_explored.append(node);
            
            if problem.isGoalState(node) == True:
                flag = 1;
                return actions;

            elif problem.isGoalState(node) == False:
                successors = problem.getSuccessors(node);
                for successor in successors:
                    print ("Successor ", successor)
                    succ_node = successor[0];
                    action = successor[1];
                    cost = successor[2];
                    newAction = actions + [action];
                    newCost = tmp_cost + cost;
                    heuristic_cost = newCost + heuristic(succ_node, problem);
                    temp_node = (succ_node, newAction, newCost);
                    if type(succ_node) == tuple:
                        if type(succ_node[1]) == list:
                            succ_node = succ_node[0];
                    if succ_node not in dfs_explored:
                        if succ_node not in dfs_frontier_check:
                            util.PriorityQueue.push(dfs_frontier_Queue, temp_node, heuristic_cost);
                            dfs_frontier_check.append(succ_node);
                            frontier_cost[succ_node] = heuristic_cost;
                        else:
                            if frontier_cost[succ_node] >= newCost: 
                                util.PriorityQueue.update(dfs_frontier_Queue, temp_node, heuristic_cost);
                            frontier_cost[succ_node] = heuristic_cost;
                        
    util.raiseNotDefined()  
    
    """
    Q4. What happens on openMaze for the various search strategies?
    Answer 4.
    
    The open maze has lesser walls and more options to explore. This means that the following is observed in the
    different search strategies:
    1. DFS - The maze is open and has very limited walls which means that compared to a normal maze - the number of 
    nodes expanded are larger. The pacman is seem moving from one side to the other horizontally without any walls to
    change paths
    2. BFS - This search expands even more nodes compared to DFS as it expands in all directions available in a space
    with minimal walls in it. The red in the maze covers the entire maze except for a small square on the maze.
    3. UCS - This operates similar to BFS - it also covers the entire maze except for a small square on the maze.
    4. A* - Compared to the others, this search expands the least number of nodes and yet this search too explores a
    big chunk of the grid
    
    
    """
    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

