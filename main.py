import math


class Node:
    def __init__(self, nodeid, x, y, location_type):
        self.id = nodeid
        self.x = x
        self.y = y
        self.location_type = location_type
        self.edges = []  # Nodes that this node points to

    def add_edge(self, node):
        self.edges.append(node)

    def distance_to(self, node):
        return math.sqrt((node.x - self.x)**2 + (node.y - self.y)**2)

    def __repr__(self):
        return f" {self.id}: ({self.x}, {self.y}, {self.location_type})"

class Water:
    def __init__(self):
        self.nodes = {}

    def add_node(self, idnode, x, y, location_type):
        node = Node(idnode, x, y, location_type)
        self.nodes[idnode] = node
        return node

    def connect_nodes(self, id1, id2):
        if id1 in self.nodes and id2 in self.nodes:
            self.nodes[id1].add_edge(self.nodes[id2])

    def get_distance(self, id1, id2):
        if id1 in self.nodes and id2 in self.nodes:
            return self.nodes[id1].distance_to(self.nodes[id2])
        else:
            return None

    def dfs(self, start_id, visited=None):
        if visited is None:
            visited = set()

        if start_id not in visited:
            visited.add(start_id)
            print(self.nodes[start_id])

            for edge in self.nodes[start_id].edges:
                self.dfs(edge.id, visited)

        return visited

    def edge_list(self):
        for nodeid,node in self.nodes.items():
            print(f"ID: {nodeid} -> ", end="")
            for edge in node.edges:
                print(f"{edge.id} ", end="")
            print()

# Creating a River Object
river = Water()

# Adding nodes and connections
n1 = river.add_node(1, 70, -100, 'headwater')
n2 = river.add_node(2, 230, -190, 'junction')
n3 = river.add_node(3, 120, -265, 'headwater')
n4 = river.add_node(4, 120, -285, 'headwater')
n5 = river.add_node(5, 195, -320, 'headwater')
n6 = river.add_node(6, 225, -370, 'headwater')
n7 = river.add_node(7, 230, -420, 'headwater')
n8 = river.add_node(8, 260, -465, 'headwater')
n9 = river.add_node(9, 315, -460, 'headwater')
n10 = river.add_node(10, 325, -500, 'headwater')
n11 = river.add_node(11, 350, -490, 'headwater')
n12 = river.add_node(12, 355, -510, 'headwater')
n13 = river.add_node(13, 380, -570, 'headwater')
n14 = river.add_node(14, 360, -410, 'headwater')
n15 = river.add_node(15, 385, -390, 'headwater')
n16 = river.add_node(16, 245, -330, 'headwater')
n17 = river.add_node(17, 225, -290, 'headwater')
n18 = river.add_node(18, 240, -140, 'headwater')
n19 = river.add_node(19, 330, -185, 'headwater')
n20 = river.add_node(20, 330, -200, 'headwater')
n21 = river.add_node(21, 340, -210, 'headwater')
n22 = river.add_node(22, 370, -180, 'headwater')
n23 = river.add_node(23, 430, -180, 'headwater')
n24 = river.add_node(24, 460, -200, 'headwater')
n25 = river.add_node(25, 430, -230, 'headwater')
n26 = river.add_node(26, 460, -220, 'headwater')
n27 = river.add_node(27, 425, -260, 'headwater')
n28 = river.add_node(28, 410, -270, 'headwater')
n29 = river.add_node(29, 520, -275, 'headwater')
n30 = river.add_node(30, 580, -210, 'headwater')
n31 = river.add_node(31, 560, -120, 'headwater')
n32 = river.add_node(32, 580, -90, 'headwater')
n33 = river.add_node(33, 145, -185, 'junction')
n34 = river.add_node(34, 170, -210, 'junction')
n35 = river.add_node(35, 220, -185, 'junction')
n36 = river.add_node(36, 275, -250, 'junction')
n37 = river.add_node(37, 290, -270, 'junction')
n38 = river.add_node(38, 325, -330, 'junction')
n39 = river.add_node(39, 320, -290, 'junction')
n40 = river.add_node(40, 265, -360, 'junction')
n41 = river.add_node(41, 295, -360, 'junction')
n42 = river.add_node(42, 100, -130, 'junction')
n43 = river.add_node(43, 305, -390, 'junction')
n44 = river.add_node(44, 400, -450, 'junction')
n45 = river.add_node(45, 450, -380, 'junction')
n46 = river.add_node(46, 380, -340, 'junction')
n47 = river.add_node(47, 415, -445, 'junction')
n48 = river.add_node(48, 355, -360, 'junction')
n49 = river.add_node(49, 350, -345, 'junction')
n50 = river.add_node(50, 425, -290, 'junction')
n51 = river.add_node(51, 430, -280, 'junction')
n52 = river.add_node(52, 450, -270, 'junction')
n53 = river.add_node(53, 500, -250, 'junction')
n54 = river.add_node(54, 540, -170, 'junction')
n55 = river.add_node(55, 360, -260, 'junction')
n56 = river.add_node(56, 370, -230, 'junction')
n57 = river.add_node(57, 370, -220, 'junction')
n58 = river.add_node(58, 380, -220, 'junction')
n59 = river.add_node(59, 190, -205, 'junction')

river.connect_nodes(1, 42)
river.connect_nodes(42, 33)
river.connect_nodes(42, 3)
river.connect_nodes(3, 4)
river.connect_nodes(4, 33)
river.connect_nodes(33, 34)
river.connect_nodes(34, 5)
river.connect_nodes(34, 59)
river.connect_nodes(59, 35)
river.connect_nodes(59, 17)
river.connect_nodes(35, 18)
river.connect_nodes(35, 2)
river.connect_nodes(2, 36)
river.connect_nodes(36, 37)
river.connect_nodes(2, 19)
river.connect_nodes(36, 20)
river.connect_nodes(37, 39)
river.connect_nodes(37, 16)
river.connect_nodes(39, 38)
river.connect_nodes(39, 55)
river.connect_nodes(38, 41)
river.connect_nodes(38, 49)
river.connect_nodes(41, 40)
river.connect_nodes(40, 6)
river.connect_nodes(40, 7)
river.connect_nodes(41, 43)
river.connect_nodes(43, 8)
river.connect_nodes(43, 9)
river.connect_nodes(39, 55)
river.connect_nodes(55, 56)
river.connect_nodes(56, 57)
river.connect_nodes(56, 58)
river.connect_nodes(57, 21)
river.connect_nodes(57, 22)
river.connect_nodes(58, 23)
river.connect_nodes(58, 24)
river.connect_nodes(55, 25)
river.connect_nodes(49, 48)
river.connect_nodes(48, 14)
river.connect_nodes(48, 15)
river.connect_nodes(49, 46)
river.connect_nodes(46, 45)
river.connect_nodes(45, 29)
river.connect_nodes(45, 47)
river.connect_nodes(47, 44)
river.connect_nodes(44, 10)
river.connect_nodes(44, 11)
river.connect_nodes(44, 12)
river.connect_nodes(47, 13)
river.connect_nodes(46, 50)
river.connect_nodes(50, 51)
river.connect_nodes(51, 28)
river.connect_nodes(51, 27)
river.connect_nodes(51, 52)
river.connect_nodes(52, 26)
river.connect_nodes(53, 53)
river.connect_nodes(53, 30)
river.connect_nodes(53, 54)
river.connect_nodes(54, 31)
river.connect_nodes(54, 32)


# try to calculate the distance
print("Distance between Node 1 and Node 2:", river.get_distance(1, 2))
print("DFS Traversal:")

# travel the nodes
river.dfs(1)
# a method for travel all nodes
### some expain for dfs(1)
#Suppose  3 nodes connected as `1 -> 2 -> 3`.
#1. `dfs(1)`.
#2. Node 1 is not in the `visited` set. Add it, print its details.
#3. Check Node 1's edges. We find Node 2. do`dfs(2)`.
#4. Node 2 is not in the `visited` set. Add it, print its details.
#5. Check Node 2's edges. We find Node 3. do `dfs(3)`.
#6. Node 3 is not in the `visited` set. Add it, print its details.
#7. Node 3 has no unvisited edgess. Return from `dfs(3)`.
#8. Return from `dfs(2)`.
#9. Return from `dfs(1)`.
#The output will display the details of the nodes in the order they were visited: Node 1, Node 2, and then Node 3.

# check the edge
print(river.edge_list())
