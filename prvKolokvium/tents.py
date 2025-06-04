from constraint import *

def neighbours(tree):
    neighbours = []
    for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if 0 <= tree[0] + x < 6 and 0 <= tree[1] + y < 6:
            neighbours.append((tree[0] + x, tree[1] + y))

    return neighbours

def tree_constraint(tree1, tree2):
    if abs(tree1[0] - tree2[0]) <= 1 and abs(tree1[1] - tree2[1]) <= 1:
        return False

    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot

    n = int(input())
    trees = []
    for _ in range(n):
        trees.append(tuple(map(int, input().split(" "))))

    trees = tuple(trees)

    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----

    for tree in trees:
        domain = []
        for neighbour in neighbours(tree):
            domain.append(neighbour)

        problem.addVariable(tree, domain)

    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------

    problem.addConstraint(AllDifferentConstraint())
    for tree1 in trees:
        for tree2 in trees:
            if tree1 < tree2:
                problem.addConstraint(tree_constraint, (tree1, tree2))

    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------

    solution = problem.getSolution()

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----

    for tree in trees:
        print(solution[tree][0], solution[tree][1])
