from Room import Room




class AspiR:
    """modelize the problem"""
    def __init__(self,liste_contenu,n_x,n_y,n_r):
        n_x = int(n_x)
        n_y = int(n_y)
        n_r = int(n_r)
        self.room = Room(n_x,n_y)
        #room = aspiR.get_room()
        liste_robot = liste_contenu[n_x :]
        self.robots = [str(color) for color in liste_robot[::3]]
        L_index_robots = [int(liste_robot[i+1])*n_y + int(liste_robot[i+2]) for i in range(0,3*n_r,3)]
        self.index_robots = {}
        j = 0
        for color in self.robots:
            self.index_robots[color] = L_index_robots[j]
            j = j+1







#test


#aspir = AspiR(filename)

#room9 = aspir.room
#print(type(room9))
#result = room9.has_wall(24,"W")
#print(result)





