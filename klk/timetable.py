from constraint import *

def ML_constraint(cas1, cas2):
    return int(cas1[-2:]) != int(cas2[-2:])

def time_constraint(cas1, cas2):
    if cas1[:3] == cas2[:3]:
        if int(cas2[-2:]) in [int(cas1[-2:]), int(cas1[-2:]) + 1]:
            return False

    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------

    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    variables = ["AI_vezbi", "ML_vezbi", "BI_vezbi"]
    ML_variables = ["ML_vezbi"]

    for i in range(int(casovi_AI)):
        problem.addVariable(f"AI_cas_{i+1}", AI_predavanja_domain)
        variables.append(f"AI_cas_{i+1}")

    for i in range(int(casovi_ML)):
        problem.addVariable(f"ML_cas_{i+1}", ML_predavanja_domain)
        variables.append(f"ML_cas_{i+1}")
        ML_variables.append(f"ML_cas_{i+1}")

    for i in range(int(casovi_R)):
        problem.addVariable(f"R_cas_{i+1}", R_predavanja_domain)
        variables.append(f"R_cas_{i+1}")

    for i in range(int(casovi_BI)):
        problem.addVariable(f"BI_cas_{i+1}", BI_predavanja_domain)
        variables.append(f"BI_cas_{i+1}")

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(), variables)

    for cas1 in ML_variables:
        for cas2 in ML_variables:
            if cas1 != cas2:
                problem.addConstraint(ML_constraint, [cas1, cas2])

    for cas1 in variables:
        for cas2 in variables:
            if cas1 != cas2:
                problem.addConstraint(time_constraint, [cas1, cas2])

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)