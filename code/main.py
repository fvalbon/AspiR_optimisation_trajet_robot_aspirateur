from Robot import Robot
from AspiR import AspiR
import time



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Sorbonne Université

Florent Valbon
Charly Nana Konguep
21/03/2020

Project Python 

CALCUL OF OPTIMAL PATH IN A GRID
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


"""
Reading of the file
"""


print("please select a grid (enter the name of the file): ")
filename = input()

file_in = open(filename, "r")
first_line = file_in.readline()
contenu = file_in.read()
n_x, n_y, n_r = first_line.split()
liste_contenu = contenu.split()
#problem
AspiR = AspiR(liste_contenu,n_x,n_y,n_r)

print("Chose a precision (0 if you want to have a speed but not sure result, increase if you want to have a most sure result) : ")
print("Choose it between 0 and", int(n_x)*int(n_y),":")
prec = int(input())


print("""""""""""""""
      
      PROJECT PYTHON : OPIMAL PATH
      
      """"""""""""""")

print("There is", len(AspiR.robots), "robots, and the grid is a", AspiR.room.n_x, "*", AspiR.room.n_y, "grid")

print("Program is runing : please wait a few moment...")


"""
User
"""

iter_max = 10000000000000000


#star of the time

start_time = time.time()

"""
Initialisations
"""
iter = 0
n_forb_path = 0 #number of no test path, that can be optimal result
room = AspiR.room
Init_Positions = set()
L_Init_Positions = []

min = 0

Robots = [] #list of all robots
for color in AspiR.robots :
    Robots.append(Robot(AspiR, color))


for index in AspiR.index_robots.values():
    Init_Positions.add(index)

for index in AspiR.index_robots.values():
    L_Init_Positions.append(index)


init_path = []
for color in AspiR.robots:
    for direction in ["W","S","E","N"]:
        init_path.append(color + direction)



# put traveled Squares
Traveled_Squares = set(Init_Positions)




#calcul of the best path


pools = [tuple(pool) for pool in (init_path,)] * 2


nPaths = [[]]

Paths = []

j = 0
for robot in Robots:
    robot._get_index(AspiR, L_Init_Positions[j])
    j = j + 1

nb_displacements = 0

"""
Calcul of the optimal path : cartesian product method
"""

for pool in pools:
    if len(Traveled_Squares) == room.n_x*room.n_y:
        break
    for x in nPaths:
        if len(Traveled_Squares) == room.n_x*room.n_y:
            break
        for y in pool:
            if len(Traveled_Squares) == room.n_x*room.n_y:
                break

            if time.time() - start_time == 300:
                print("program is runing, please wait ...")

            path = x + [y]

            count = 0
            if len(path)<=2:
                Paths.append(x + [y])

            if len(path)>2: # its impossible to fin a path with less 2 move


                for i in range(len(path) - 2):

                    """ 1) restrictiv conditions : don't go where robot do a round trip or move to the same direction
                    """


                    if ((path[i][0] == path[i + 1][0]) and (
                            (path[i][1] == "W" and path[i + 1][1] == "E") or (
                            path[i][1] == "E" and path[i + 1][1] == "W") or (
                                    path[i][1] == "S" and path[i + 1][1] == "N") or (
                                    path[i][1] == "N" and path[i + 1][1] == "S") or
                            (path[i][1] == "N" and path[i + 1][1] == "N") or (
                                    path[i][1] == "S" and path[i + 1][1] == "S") or
                            (path[i][1] == "E" and path[i + 1][1] == "E") or (path[i][1] == "W" and path[i + 1][1] == "W") )) :

                        break

                    count = count + 1


            if count == len(path) -2:




                """ Calcul
                """
                if iter < iter_max:

                    """ Move the robot
                    """

                    # sol is the path
                    sol = " "
                    # put traveled Squares

                    Traveled_Squares = set(Init_Positions)
                    # put robots at initials index in the map
                    # test a path and move the robot
                    count2 =0
                    while (len(Traveled_Squares) < room.n_x * room.n_y):
                        for i in range(len(path)):
                            if Robot(AspiR, path[i][0]).can_move(AspiR, path[i][1],liste_contenu) == False:
                                break
                            else:
                                while Robot(AspiR, path[i][0]).can_move(AspiR, path[i][1],liste_contenu):
                                    Robot(AspiR, path[i][0]).compute_move(AspiR, path[i][1],liste_contenu)
                                    Traveled_Squares.add(Robot(AspiR, path[i][0]).index)
                                count2 = count2+1
                                sol = sol + str(path[i][0]) + str(path[i][1]) + " "
                        break
                    if count2 == len(path):
                        if(len(Traveled_Squares) >= nb_displacements - prec): #if displacement is better
                            Paths.append(x + [y])  # give a set of possible paths
                            nb_displacements = len(Traveled_Squares)
                        else:
                            n_forb_path = n_forb_path + 1
                        iter = iter + 1

                    if (len(Traveled_Squares) == room.n_x * room.n_y):
                            min = sol
                    j =0
                    for robot in Robots:
                        robot._get_index(AspiR, L_Init_Positions[j])
                        j = j + 1






        nPaths = Paths



"""
Result
"""


if n_forb_path>0:
    print("**********\n WARNING : only" ,100 - (n_forb_path/(iter + 1))*100,"% directions that can lead to an optimal path has in totality been tested at each displacement. \n **********")

print("\n \n An optimal path is \n ********** \n", min,"\n ********** \n \n")
print("Number of displacements of the optimal path :",len(path))


print("Execution time : %s second ---" % (time.time() - start_time))

























