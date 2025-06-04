from searching_framework.informed_search import *
from searching_framework.uninformed_search import *
from searching_framework.utils import *

def valid_state(x, y, boxes, n):
    if 0 <= x < n and 0 <= y < n:
        if (x, y) not in boxes:
            return True

    return False

def can_put_ball(x, y, boxes, closed_boxes):
    for box in boxes:
        if abs(x - box[0]) <= 1 and abs(y - box[1]) <= 1 and box not in closed_boxes:
            return box

    return None

class Boxes(Problem):
    def __init__(self, initial, boxes, n, goal=None):
        super().__init__(initial, goal)
        self.boxes = boxes
        self.n = n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[2] == 0

    def successor(self, state):
        successors = dict()

        new_x, new_y = state[0][0], state[0][1] + 1
        new_c = state[2]
        if valid_state(new_x, new_y, self.boxes, self.n):
            box = can_put_ball(new_x, new_y, self.boxes, state[1])
            closed = list(state[1])
            if box is not None:
                closed.append(box)
                new_c -= 1
            successors["Gore"] = ((new_x, new_y), tuple(closed), new_c)

        new_x, new_y = state[0][0] + 1, state[0][1]
        new_c = state[2]
        if valid_state(new_x, new_y, self.boxes, self.n):
            box = can_put_ball(new_x, new_y, self.boxes, state[1])
            closed = list(state[1])
            if box is not None:
                closed.append(box)
                new_c -= 1
            successors["Desno"] = ((new_x, new_y), tuple(closed), new_c)

        return successors


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    boxes = tuple(boxes)
    visited = ()
    initial_state = (man_pos, visited, num_boxes)

    problem = Boxes(initial_state, boxes, n)

    result = breadth_first_graph_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print('No Solution!')