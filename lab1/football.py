from searching_framework.uninformed_search import *


def move_human(hx, hy, dir):
    if(dir == "n") and hy < 5:
        hy += 1
    elif (dir == "e") and hx < 7:
        hx += 1
    elif (dir == "s") and hy > 0:
        hy -= 1
    elif (dir == "ne") and hy < 5 and hx < 7:
        hy += 1
        hx += 1
    elif (dir == "se") and hy > 0 and hx < 7:
        hy -= 1
        hx += 1

    return hx, hy

def shoot_ball(hx, hy, bx, by, dir):
    if (dir == "n") and hy < 5 and by < 5:
        hy += 1
        by += 1
    elif (dir == "e") and hx < 7 and bx < 7:
        hx += 1
        bx += 1
    elif (dir == "s") and hy > 0 and by > 0:
        hy -= 1
        by -= 1
    elif (dir == "ne") and hy < 5 and hx < 7 and by < 5 and bx < 7:
        hy += 1
        hx += 1
        by += 1
        bx += 1
    elif (dir == "se") and hy > 0 and hx < 7 and by > 0 and bx < 7:
        hy -= 1
        hx += 1
        by -= 1
        bx += 1

    return hx, hy, bx, by

def is_valid_move(hx, hy, bx, by, ops):
    if (hx, hy) == (bx, by):
        return False
    if (hx, hy) in ops:
        return False

    return True

# def is_shot_valid(bx, by, ops):
#     for op in ops:
#         if [bx, by] in [[op[0], op[1]], [op[0] + 1, op[1]], [op[0] + 1, op[1] - 1], [op[0], op[1] - 1], [op[0] - 1, op[1] - 1],
#                         [op[0] - 1, op[1]], [op[0] - 1, op[1] + 1], [op[0], op[1] + 1], [op[0] + 1, op[1] + 1]]:
#             return False
#
#     return True

def is_shot_valid(bx, by, ops):
    for op in ops:
        if (bx, by) in {(op[0], op[1]), (op[0] + 1, op[1]), (op[0] + 1, op[1] - 1), (op[0], op[1] - 1),
                         (op[0] - 1, op[1] - 1), (op[0] - 1, op[1]), (op[0] - 1, op[1] + 1),
                         (op[0], op[1] + 1), (op[0] + 1, op[1] + 1)}:
            return False
    return True





class Football(Problem):
    def __init__(self, initial, opponents, goal=None):
        super().__init__(initial, goal)
        self.opponents = opponents


    #state(initial_state, opponents, goal)
    def successor(self, state):
        successors = dict()

        hx, hy = move_human(state[0][0], state[0][1], "n")
        if [hx, hy] != [state[0][0], state[0][1]]:
            if is_valid_move(hx, hy, state[1][0], state[1][1], self.opponents):
                successors["Pomesti coveche gore"] = ((hx, hy), state[1])

        hx, hy = move_human(state[0][0], state[0][1], "e")
        if [hx, hy] != [state[0][0], state[0][1]]:
            if is_valid_move(hx, hy, state[1][0], state[1][1], self.opponents):
                successors["Pomesti coveche desno"] = ((hx, hy), state[1])

        hx, hy = move_human(state[0][0], state[0][1], "s")
        if [hx, hy] != [state[0][0], state[0][1]]:
            if is_valid_move(hx, hy, state[1][0], state[1][1], self.opponents):
                successors["Pomesti coveche dolu"] = ((hx, hy), state[1])

        hx, hy = move_human(state[0][0], state[0][1], "ne")
        if [hx, hy] != [state[0][0], state[0][1]]:
            if is_valid_move(hx, hy, state[1][0], state[1][1], self.opponents):
                successors["Pomesti coveche gore-desno"] = ((hx, hy), state[1])

        hx, hy = move_human(state[0][0], state[0][1], "se")
        if [hx, hy] != [state[0][0], state[0][1]]:
            if is_valid_move(hx, hy, state[1][0], state[1][1], self.opponents):
                successors["Pomesti coveche dolu-desno"] = ((hx, hy), state[1])

        hx, hy = move_human(state[0][0], state[0][1], "n")
        if [hx, hy] != [state[0][0], state[0][1]]:
            if is_valid_move(hx, hy, state[1][0], state[1][1], self.opponents):
                successors["Pomesti coveche gore"] = ((hx, hy), state[1])

        if (state[0][0], state[0][1] + 1) == (state[1][0], state[1][1]):
            hx, hy, bx, by = shoot_ball(state[0][0], state[0][1], state[1][0], state[1][1],  "n")
            if [bx, by] != [state[1][0], state[1][1]]:
                if is_shot_valid(bx, by, self.opponents):
                    successors["Turni topka gore"] = ((hx, hy), (bx, by))

        if (state[0][0] + 1, state[0][1]) == (state[1][0], state[1][1]):
            hx, hy, bx, by = shoot_ball(state[0][0], state[0][1], state[1][0], state[1][1],  "e")
            if [bx, by] != [state[1][0], state[1][1]]:
                if is_shot_valid(bx, by, self.opponents):
                    successors["Turni topka desno"] = ((hx, hy), (bx, by))

        if (state[0][0], state[0][1] - 1) == (state[1][0], state[1][1]):
            hx, hy, bx, by = shoot_ball(state[0][0], state[0][1], state[1][0], state[1][1],  "s")
            if [bx, by] != [state[1][0], state[1][1]]:
                if is_shot_valid(bx, by, self.opponents):
                    successors["Turni topka dolu"] = ((hx, hy), (bx, by))

        if (state[0][0] + 1, state[0][1] + 1) == (state[1][0], state[1][1]):
            hx, hy, bx, by = shoot_ball(state[0][0], state[0][1], state[1][0], state[1][1],  "ne")
            if [bx, by] != [state[1][0], state[1][1]]:
                if is_shot_valid(bx, by, self.opponents):
                    successors["Turni topka gore-desno"] = ((hx, hy), (bx, by))

        if (state[0][0] + 1, state[0][1] - 1) == (state[1][0], state[1][1]):
            hx, hy, bx, by = shoot_ball(state[0][0], state[0][1], state[1][0], state[1][1],  "se")
            if [bx, by] != [state[1][0], state[1][1]]:
                if is_shot_valid(bx, by, self.opponents):
                    successors["Turni topka dolu-desno"] = ((hx, hy), (bx, by))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal

if __name__ == '__main__':
    human = (tuple(map(int, input().split(','))))
    ball = (tuple(map(int, input().split(','))))

    initial_state = (human, ball)

    football = Football(initial_state, ((3, 3), (5, 4)), ((7, 2), (7, 3)))

    result = breadth_first_graph_search(football)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")