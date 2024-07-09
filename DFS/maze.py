class Maze:
    def __init__(self):
        self.heads = []
    def GetTheHead(self):
        return self.heads[0]
    def GetHeads(self):
        return self.heads
    def insert(self,data):
        self.heads.append(data)
    def FindGoal(self,heads):
        temp_heads = heads
        goal = []
        for i in range(len(temp_heads)):
            goal_x = goal_y = counter = 0
            temporary = temp_heads[i]
            while temporary != None:
                if temporary.data == "2":
                    goal_x = i
                    goal_y = counter
                    goal = [i,counter]
                    print("result: ",[goal_x, goal_y])
                    return goal
                counter += 1
                temporary = temporary.next

    def setup(self,lines):
        for i in range(len(lines)):                 #O(row)
            lines[i] = lines[i].replace("\n","")
            head = Node(lines[i][0])
            remain = lines[i][1:]
            temp = head
            while remain != "":                     #O(column)
                n = Node(remain[0])
                n.insert_previous(temp)
                temp.insert_next(n)
                remain = remain[1:]
                temp = temp.next
            self.insert(head)
        count = 0
        temporary = self.heads[0]
        while temporary != None:
            for i in range(len(lines)-1):
                temp = self.heads[i]
                temp_n = self.heads[i+1]
                for k in range(count):
                    temp = temp.next
                    temp_n = temp_n.next
                temp_n.insert_up(temp)
                temp.insert_down(temp_n)
            count += 1
            temporary = temporary.next
    def print(self):
        temp = self.heads[0]
        while temp != None:
            temp_n = temp
            while temp_n != None:
                print(temp_n.data, end=" ")
                temp_n = temp_n.next
            temp = temp.down
            print()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
        self.up = None
        self.down = None
    def insert_next(self,n):
        self.next = n
    def insert_previous(self,n):
        self.previous = n
    def insert_up(self,n):
        self.up = n
    def insert_down(self,n):
        self.down = n   