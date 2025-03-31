from searching_framework.utils import Problem
from searching_framework.informed_search import astar_search

def move_house(house, house_dir):
    if house_dir == "desno":
        if house[0] < 4:
            return house[0] + 1, house[1], house_dir
        if house[0] == 4:
            return house[0] - 1, house[1], "levo"

    if house_dir == "levo":
        if house[0] > 0:
            return house[0] - 1, house[1], house_dir
        if house[0] == 0:
            return house[0] + 1, house[1], "desno"

def is_valid_move(hx, hy, allowed, house):
    if 0 <= hx <= 4 and 0 <= hy < 8:
        if (hx, hy) in allowed:
            return True
    elif 0 <= hx <= 4 and hy == 8:
        if (hx, hy) == house:
            return True

    return False
class House(Problem):
    def __init__(self, initial, allowed, goal=None):
        super().__init__(initial, goal)
        self.allowed = allowed


    #state(human, house, house_dir)
    def successor(self, state):
        successors = dict()
        hx, hy, hdir = move_house(state[1], state[2])

        successors["Stoj"] = (state[0], (hx, hy), hdir)

        new_x, new_y = state[0][0], state[0][1] + 1
        if is_valid_move(new_x, new_y, self.allowed, (hx, hy)):
            successors["Gore 1"] = ((new_x, new_y), (hx, hy), hdir)

        new_x, new_y = state[0][0], state[0][1] + 2
        if is_valid_move(new_x, new_y, self.allowed, (hx, hy)):
            successors["Gore 2"] = ((new_x, new_y), (hx, hy), hdir)

        new_x, new_y = state[0][0] + 1, state[0][1] + 1
        if is_valid_move(new_x, new_y, self.allowed, (hx, hy)):
            successors["Gore-desno 1"] = ((new_x, new_y), (hx, hy), hdir)

        new_x, new_y = state[0][0] + 2, state[0][1] + 2
        if is_valid_move(new_x, new_y, self.allowed, (hx, hy)):
            successors["Gore-desno 2"] = ((new_x, new_y), (hx, hy), hdir)

        new_x, new_y = state[0][0] - 1, state[0][1] + 1
        if is_valid_move(new_x, new_y, self.allowed, (hx, hy)):
            successors["Gore-levo 1"] = ((new_x, new_y), (hx, hy), hdir)

        new_x, new_y = state[0][0] - 2, state[0][1] + 2
        if is_valid_move(new_x, new_y, self.allowed, (hx, hy)):
            successors["Gore-levo 2"] = ((new_x, new_y), (hx, hy), hdir)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1]

    def h(self, node):
        return (abs(node.state[0][0] - node.state[1][0]) + abs(node.state[0][1] - node.state[1][1])) / 5

if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    human = (tuple(map(int, input().split(','))))
    house = (tuple(map(int, input().split(','))))
    house_dir = input()

    problem = House((human, house, house_dir), allowed)

    result = astar_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")