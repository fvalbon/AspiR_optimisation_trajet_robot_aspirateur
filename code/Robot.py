from AspiR import AspiR


class Robot:
    """Class define of robot caracterize by :
    - is color
    - is position

    """
    def __init__(self,aspiR,color):
        """Constructor"""
        self.color = color
        self.index = aspiR.index_robots[color]


    def can_move(self, aspiR, direction,liste_contenu):
        """say if the robot can move in a direction or not"""

        room = aspiR.room
        if room.has_wall(self.index,direction,liste_contenu) == True:
            return False
        else:
            if direction == "W":
                for color in [color for color in aspiR.robots if color != self.color]:
                    if (aspiR.index_robots[color] == self.index - 1):
                        return False
                return True

            if direction == "S":
                for color in [color for color in aspiR.robots if color != self.color]:
                    if (aspiR.index_robots[color] == self.index + room.n_y):
                        return False
                return True

            if direction == "E":
                for color in [color for color in aspiR.robots if color != self.color]:
                    if (aspiR.index_robots[color] == self.index + 1):
                        return False
                return True

            if direction == "N":
                for color in [color for color in aspiR.robots if color != self.color]:
                    if (aspiR.index_robots[color] == self.index - room.n_y):
                        return False
                return True



    def _get_index(self,aspiR,new_index):
        """setter"""
        self.index = new_index
        aspiR.index_robots[self.color] = new_index


    def compute_move(self, aspiR, direction,liste_contenu):
        """To move a Robot in a direction"""

        room = aspiR.room
        if self.can_move(aspiR,direction,liste_contenu) == False:
            print("ERROR : the robot ",self.color," index : ", self.index,"can't move in direction", direction)
            return
        index = self.index

        if direction == "W":
            self._get_index(aspiR,index - 1)

        if direction == "S":
            self._get_index(aspiR,index + room.n_y)

        if direction == "E":
            self._get_index(aspiR,index + 1)


        if direction == "N":
            self._get_index(aspiR,index - room.n_y)






# test

#filename = "Case_Aspi_R_3.txt"
#aspir = AspiR(filename)
#y = Robot(aspir,"Y")
#print(y.index)
#print(y.compute_move(aspir, "E"))
#print(y.index)
#y.compute_move(aspir, "S")
#r =Robot(aspir,"R")
#r.compute_move(aspir,"N")
#print(y.can_move(aspir,"W"))
#y.compute_move(aspir, "W")
#r.compute_move(aspir,'S')
#r.compute_move(aspir,"E")
#r.compute_move(aspir,"W")
#r.compute_move(aspir,"W")
#y.compute_move(aspir, "S")
#print(y.index)
#print(r.index)
