

class Room :
#""" Class which modelize the room"""

    def __init__(self, n_x, n_y) :
        #n_x, n_y are length and width of the grid
        self.n_x = n_x
        self.n_y = n_y


    def has_wall(self, index, direction,liste_contenu) :
        """Say if there is a wall or not"""
        # list which represent the differents walls in each coordinate
        # index = x*n_y + y (1D position of the Robot)

        L = []

        for l_x in liste_contenu[:self.n_x]:
            for i in range(self.n_y):
                L.append(l_x[i])

        if L[index] == '0' :
            if direction == "W" : return False
            if direction == "S" : return False
            if direction == "E" : return False
            if direction == "N" : return False

        if L[index] == '1' :
            if direction == "W" : return False
            if direction == "S" : return False
            if direction == "E" : return False
            if direction == "N" : return True

        if L[index] == '2' :
            if direction == "W" : return False
            if direction == "S" : return False
            if direction == "E" : return True
            if direction == "N" : return False

        if L[index] == '3' :
            if direction == "W" : return False
            if direction == "S" : return False
            if direction == "E" : return True
            if direction == "N" : return True

        if L[index] == '4':
            if direction == "W": return False
            if direction == "S": return True
            if direction == "E": return False
            if direction == "N": return False

        if L[index] == '5':
            if direction == "W": return False
            if direction == "S": return True
            if direction == "E": return False
            if direction == "N": return True

        if L[index] == '6':
            if direction == "W": return False
            if direction == "S": return True
            if direction == "E": return True
            if direction == "N": return False

        if L[index] == '7':
            if direction == "W": return False
            if direction == "S": return True
            if direction == "E": return True
            if direction == "N": return True

        if L[index] == '8':
            if direction == "W": return True
            if direction == "S": return False
            if direction == "E": return False
            if direction == "N": return False

        if L[index] == '9':
            if direction == "W": return True
            if direction == "S": return False
            if direction == "E": return False
            if direction == "N": return True


        if L[index] == 'A':
            if direction == "W": return True
            if direction == "S": return False
            if direction == "E": return True
            if direction == "N": return False

        if L[index] == 'B':
            if direction == "W": return True
            if direction == "S": return False
            if direction == "E": return True
            if direction == "N": return True

        if L[index] == 'C':
            if direction == "W": return True
            if direction == "S": return True
            if direction == "E": return False
            if direction == "N": return False

        if L[index] == 'D':
            if direction == "W": return True
            if direction == "S": return True
            if direction == "E": return False
            if direction == "N": return True

        if L[index] == 'E':
            if direction == "W": return True
            if direction == "S": return True
            if direction == "E": return True
            if direction == "N": return False




#test

#filename = "Case_Aspi_R_3.txt"


#room3 = Room(6,6,filename)
#result = room3.has_wall(24,"W")
#print(type(room3))
#print(room3.filename)
#(result)