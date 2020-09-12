import maze

class Player:
    def __init__(self):
        self.coords = [[2,2]]
        self.state = "ver"
        self.goal = []
    def Clear(self):
        self.coords.clear()
    def GetState(self):
        return self.state
    def PrintLoc(self):
        print("Player at position: (" + str(self.coords) + ")")
    def GetPos(self):
        return self.coords
    def CheckPlayer(self,temp_heads):
        for coord in self.coords:
            temporary = temp_heads[coord[0]]
            for i in range(coord[1]):
                temporary = temporary.next
            if temporary.data == "0":
                return False
        return True

    def CheckMove(self,dir,map_heads,moves): #Modifiye edilmeli
        if len(moves) >= 1:
            if moves[-1] == "right" and dir == "left":
                return False
            if moves[-1] == "left" and dir == "right":
                return False
            if moves[-1] == "up" and dir == "down":
                return False
            if moves[-1] == "down" and dir == "up":
                return False
        if dir == "":
            return True #For init purposes
        
        temp_heads = map_heads
        coord = new_coord = []
        if dir == "left":
            coord = min(self.coords, key=lambda x: x[1])
            new_coord.append([coord[0],coord[1]-1])
            if len(self.coords) == 1:
                new_coord.append([coord[0],coord[1]-2])
        if dir == "right":
            coord = max(self.coords, key=lambda x: x[1])
            new_coord.append([coord[0],coord[1]+1])
            if len(self.coords) == 1:
                new_coord.append([coord[0],coord[1]+2])
        if dir == "up":
            coord = min(self.coords, key=lambda x: x[0])
            new_coord.append([coord[0]-1,coord[1]])
            if len(self.coords) == 1:
                new_coord.append([coord[0]-2,coord[1]])
        if dir == "down":
            coord = max(self.coords, key=lambda x: x[0])
            new_coord.append([coord[0]+1,coord[1]])
            if len(self.coords) == 1:
                new_coord.append([coord[0]+2,coord[1]])

        for c in new_coord: #General check if on edge
            for a in c:
                if a <= 0:
                    return False
            temporary = temp_heads[c[0]]
            for i in range(c[1]):
                temporary = temporary.next
            if temporary != None:
                if temporary.data == "0":
                    return False
            else:
                return False
        return True

    def Move(self,dir): #head => Maze head
        coord_cand = []
        if self.state == "ver":
            y_pos,x_pos = self.coords[0][0],self.coords[0][1]
            if dir == "left" :
                coord_cand = [[y_pos,x_pos-1],[y_pos,x_pos-2]]
            elif dir == "right":
                coord_cand = [[y_pos,x_pos+1],[y_pos,x_pos+2]]
            elif dir == "up":
                coord_cand = [[y_pos-1,x_pos],[y_pos-2,x_pos]]
            elif dir == "down":
                coord_cand = [[y_pos+1,x_pos],[y_pos+2,x_pos]]
            self.state = "hor"
        elif self.state == "hor":
            y_pos,x_pos = [self.coords[0][0],self.coords[1][0]],[self.coords[0][1],self.coords[1][1]]
            if x_pos[0] == x_pos[1]:
                if dir == "left":
                    coord_cand = [[y_pos[0],x_pos[0]-1],[y_pos[1],x_pos[1]-1]]
                elif dir == "right":
                    coord_cand = [[y_pos[0],x_pos[0]+1],[y_pos[1],x_pos[1]+1]]
                elif dir == "up":
                    coord_cand = [[min(y_pos)-1,x_pos[0]]]
                    self.state = "ver"
                elif dir == "down":
                    coord_cand = [[max(y_pos)+1,x_pos[0]]]
                    self.state = "ver"
            elif  y_pos[0] == y_pos[1]:
                if dir == "left":
                    coord_cand = [[y_pos[0],min(x_pos)-1]]
                    self.state = "ver"
                elif dir == "right":
                    coord_cand = [[y_pos[0],max(x_pos)+1]]
                    self.state = "ver"
                elif dir == "up":
                    coord_cand = [[y_pos[0]-1,x_pos[0]],[y_pos[0]-1,x_pos[1]]]
                elif dir == "down":
                    coord_cand = [[y_pos[0]+1,x_pos[0]],[y_pos[0]+1,x_pos[1]]]
        self.coords = coord_cand
        #print(self.coords)
        if coord_cand == []:
            print("A problem has occured along the way !")
