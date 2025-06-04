from constraint import *

def valid_meeting(simona, marija, petar):
    return simona and (marija or petar)

def available_constraint(simona, marija, petar, vreme):
    return simona == simona_available[vreme] and marija == marija_available[vreme] and petar == petar_available[vreme]

if __name__ == '__main__':

    marija_available = {12:0, 13:0, 14:1, 15:1, 16:0, 17:0, 18:1, 19:0}
    simona_available = {12:0, 13:1, 14:1, 15:0, 16:1, 17:0, 18:0, 19:1}
    petar_available = {12:1, 13:1, 14:0, 15:0, 16:1, 17:1, 18:1, 19:1}
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [i for i in range(12, 20)])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(available_constraint, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])
    problem.addConstraint(valid_meeting, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"])

    # ----------------------------------------------------

    for solution in problem.getSolutions():
        ordered_solution = {key: solution[key] for key in
                            ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"]}
        print(ordered_solution)
