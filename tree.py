import maze
import player

class TreeNode:
    def __init__(self,player_pos):
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.c4 = None
        self.coords = player_pos
        self.is_solution = False
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
        if len(moves) >= 10: #Time comlexity proportional to value
            return
        if len(player.GetPos()) == 1:
            if player.GetPos()[0] == goal:
                root.is_solution = True
                return
        if not player.CheckPlayer(map_heads):
            return
        if root.c1 == None and player.CheckMove("left",map_heads,moves):
            player.Move("left")
            moves.append("left")
            node = TreeNode(player.GetPos())
            root.InsertC1(node)
            self.setup(root.c1,player,goal,"left",map_heads,moves)
            player.Move("right")
            moves.pop()
        if root.c2 == None and player.CheckMove("right",map_heads,moves):
            player.Move("right")
            moves.append("right")
            node = TreeNode(player.GetPos())
            root.InsertC2(node)
            self.setup(root.c2,player,goal,"right",map_heads,moves)
            player.Move("left")
            moves.pop()
        if root.c3 == None and player.CheckMove("up",map_heads,moves):
            player.Move("up")
            moves.append("up")
            node = TreeNode(player.GetPos())
            root.InsertC3(node)
            self.setup(root.c3,player,goal,"up",map_heads,moves)
            player.Move("down")
            moves.pop()
        if root.c4 == None and player.CheckMove("down",map_heads,moves):
            player.Move("down")
            moves.append("down")
            node = TreeNode(player.GetPos())
            root.InsertC4(node)
            self.setup(root.c4,player,goal,"down",map_heads,moves)
            player.Move("up")
            moves.pop()
    def SearchSolution(self,root,moves):
        if root == None:
            return
        if root.is_solution:
            print(moves)
            return
        moves.append("left")
        self.SearchSolution(root.c1,moves)
        moves.pop()
        moves.append("right")
        self.SearchSolution(root.c2,moves)
        moves.pop()
        moves.append("up")
        self.SearchSolution(root.c3,moves)
        moves.pop()
        moves.append("down")
        self.SearchSolution(root.c4,moves)
        moves.pop()



