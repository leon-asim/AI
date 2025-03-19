from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def move_straight(snake, dir, green_apples):
    head_x, head_y = snake[0]

    if dir == "s" and head_y > 0:
        new_head = (head_x, head_y - 1)
    elif dir == "e" and head_x < 9:
        new_head = (head_x + 1, head_y)
    elif dir == "n" and head_y < 9:
        new_head = (head_x, head_y + 1)
    elif dir == "w" and head_x > 0:
        new_head = (head_x - 1, head_y)
    else:
        return snake

    if new_head in green_apples:
        return (new_head,) + snake
    else:
        return (new_head,) + snake[:-1]

def move_right(snake, dir, green_apples):
    head_x, head_y = snake[0]

    if dir == "s" and head_x > 0:
        new_head = (head_x - 1, head_y)
        new_dir = "w"
    elif dir == "e" and head_y > 0:
        new_head = (head_x, head_y - 1)
        new_dir = "s"
    elif dir == "n" and head_x < 9:
        new_head = (head_x + 1, head_y)
        new_dir = "e"
    elif dir == "w" and head_y < 9:
        new_head = (head_x, head_y + 1)
        new_dir = "n"
    else:
        return snake, dir

    if new_head in green_apples:
        return (new_head,) + snake, new_dir
    else:
        return (new_head,) + snake[:-1], new_dir


def move_left(snake, dir, green_apples):
    head_x, head_y = snake[0]

    if dir == "s" and head_x < 9:
        new_head = (head_x + 1, head_y)
        new_dir = "e"
    elif dir == "e" and head_y < 9:
        new_head = (head_x, head_y + 1)
        new_dir = "n"
    elif dir == "n" and head_x > 0:
        new_head = (head_x - 1, head_y)
        new_dir = "w"
    elif dir == "w" and head_y > 0:
        new_head = (head_x, head_y - 1)
        new_dir = "s"
    else:
        return snake, dir

    if new_head in green_apples:
        return (new_head,) + snake, new_dir
    else:
        return (new_head,) + snake[:-1], new_dir

def is_valid_move(snake_pos, red_apples):
    new_head = snake_pos[0]
    body = snake_pos[1:]

    if new_head in red_apples:
        return False

    if new_head in body:
        return False

    return True

class Snake(Problem):
    def __init__(self, initial, red_apples, goal=None):
        super().__init__(initial, goal)
        self.red_apples = red_apples

    #(state=(snake, direction, green_apples), red_apples)
    def successor(self, state):
        successors = dict()

        new_snake = move_straight(state[0], state[1], state[2])
        if new_snake != state[0]:
            if is_valid_move(new_snake, self.red_apples):
                successors["ProdolzhiPravo"] = (new_snake, state[1], tuple(s for s in state[2] if new_snake[0] != s))

        new_snake, new_dir = move_right(state[0], state[1], state[2])
        if new_snake != state[0]:
            if is_valid_move(new_snake, self.red_apples):
                successors["SvrtiDesno"] = (new_snake, new_dir, tuple(s for s in state[2] if new_snake[0] != s))

        new_snake, new_dir = move_left(state[0], state[1], state[2])
        if new_snake != state[0]:
            if is_valid_move(new_snake, self.red_apples):
                successors["SvrtiLevo"] = (new_snake, new_dir, tuple(s for s in state[2] if new_snake[0] != s))


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0

if __name__ == '__main__':
    green = input()
    green_apples = []
    for i in range(int(green)):
        green_apples.append(tuple(map(int, input().split(','))))

    red = input()
    red_apples = []
    for i in range(int(red)):
        red_apples.append(tuple(map(int, input().split(','))))

    snake_pos = ((0, 7), (0, 8), (0, 9))
    direction = "s"

    green_apples = tuple(green_apples)
    red_apples = tuple(red_apples)

    initial_state = (snake_pos, direction, green_apples)
    snake = Snake(initial_state, red_apples)

    result = breadth_first_graph_search(snake)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")