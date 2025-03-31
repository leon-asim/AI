from searching_framework.utils import Problem
from searching_framework.informed_search import astar_search


def is_valid_move(hx, hy, walls, n):
    if 0 <= hx < n and 0 <= hy < n:
        if (hx, hy) not in walls:
            return True
    return False


class House(Problem):
    def __init__(self, initial, walls, grid, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.grid = grid

    def successor(self, state):
        successors = dict()

        nx, ny = state[0] + 2, state[1]
        if is_valid_move(nx, ny, self.walls, self.grid) and (state[0] + 1, state[1]) not in self.walls:
            successors["Desno 2"] = (nx, ny)

        nx, ny = state[0] + 3, state[1]
        if is_valid_move(nx, ny, self.walls, self.grid) and (state[0] + 1, state[1]) not in self.walls and (
                state[0] + 2, state[1]) not in self.walls:
            successors["Desno 3"] = (nx, ny)

        nx, ny = state[0], state[1] + 1
        if is_valid_move(nx, ny, self.walls, self.grid):
            successors["Gore"] = (nx, ny)

        nx, ny = state[0], state[1] - 1
        if is_valid_move(nx, ny, self.walls, self.grid):
            successors["Dolu"] = (nx, ny)

        nx, ny = state[0] - 1, state[1]
        if is_valid_move(nx, ny, self.walls, self.grid):
            successors["Levo"] = (nx, ny)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        return (abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1])) / 3


if __name__ == '__main__':
    n = int(input())
    num_walls = int(input())

    walls = []
    for i in range(num_walls):
        x = tuple(map(int, input().split(',')))
        walls.append(x)

    walls = tuple(walls)

    human = tuple(map(int, input().split(',')))
    house = tuple(map(int, input().split(',')))

    problem = House(human, walls, n, house)

    result = astar_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")