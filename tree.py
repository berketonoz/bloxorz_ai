import maze
import player

class TreeNode:
    def __init__(self,player_pos):
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.c4 = None
        self.coords = player_pos
        
    def InsertC1(self,c):
        self.c1 = c
    def InsertC2(self,c):
        self.c2 = c
    def InsertC3(self,c):
        self.c3 = c
    def InsertC4(self,c):
        self.c4 = c
class Tree:
    def __init__(self,node):
        self.root = node
    def setup(self,root,player,goal,direction,map_heads,moves):
        print("Player at: ",player.GetPos())
        print("Your goal: ",goal)
        if player.GetPos()[0] == goal:
            print(moves) 
        if not player.CheckMove(direction,map_heads,moves):
            return
        if root.c1 == None and player.CheckMove("left",map_heads,moves):
            player.Move("left")
            moves.append("left")
            node = TreeNode(player.GetPos())
            root.InsertC1(node)
        self.setup(root.c1,player,goal,"left",map_heads,moves)
        if root.c2 == None and player.CheckMove("right",map_heads,moves):
            player.Move("right")
            moves.append("right")
            node = TreeNode(player.GetPos())
            root.InsertC2(node)
        self.setup(root.c2,player,goal,"right",map_heads,moves)
        if root.c3 == None and player.CheckMove("up",map_heads,moves):
            player.Move("up")
            moves.append("up")
            node = TreeNode(player.GetPos())
            root.InsertC3(node)
        self.setup(root.c3,player,goal,"up",map_heads,moves)
        if root.c4 == None and player.CheckMove("down",map_heads,moves):
            player.Move("down")
            moves.append("down")
            node = TreeNode(player.GetPos())
            root.InsertC4(node)
        self.setup(root.c4,player,goal,"down",map_heads,moves)

