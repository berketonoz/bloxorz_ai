import player     
import maze
import tree


file = open("sample.txt", "r") #open map file
lines = file.readlines() #read file
map_d = maze.Maze() #construct
map_d.setup(lines) #data processing phase
map_d.print() #print maze

goal_cord = map_d.FindGoal(map_d.GetHeads())

player = player.Player()
player.PrintLoc()

tree_node = tree.TreeNode(player.GetPos())
tree = tree.Tree(tree_node)

tree.setup(tree.root,player,goal_cord,"",map_d.GetHeads(),[])

print("Have any solution been found? Lets see...")

tree.SearchSolution(tree.root,[])

print("done!")