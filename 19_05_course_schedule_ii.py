# this is actually code for 2 problems

class Node:
    ident = None
    parents = None
    children = None
    been_visited = False
    one_time_flag_visited = False

    def __init__(self, ident):
        self.ident = ident
        self.children = list()
        self.parents = list()
        return

class Graph:
    nodes = None

    def __init__(self, n, rules_list):
        nodes = list()
        for ident in range(n):
            nodes.append(Node(ident))
        
        for rule in rules_list:
            first, second = rule
            nodes[second].children.append(nodes[first])
            nodes[first].parents.append(nodes[second])

        self.nodes = nodes
        return
    
    def _cycle_detection_helper(self, node, search_queue, rec_stack):
        if node.one_time_flag_visited == False:
            node.one_time_flag_visited = True
            search_queue.remove(node)
        
        node.been_visited = True
        newstack = rec_stack[:]
        newstack.append(node)

        for child in node.children:
            if child.been_visited == False:
                result = self._cycle_detection_helper(child, search_queue, newstack)
                if result == True:
                    return True
        
        for child in node.children:
            if child in newstack:
                return True
        
        return False

    def cycle_detect(self):
        
        search_queue = self.nodes[:]
        while len(search_queue) > 0:
            search_node = search_queue.pop()
            search_node.one_time_flag_visited = True
            rec_stack = []
            result = self._cycle_detection_helper(search_node, search_queue, rec_stack)
            
            for node in self.nodes:
                node.been_visited = False
            
            if result == True:
                return True

        return False
    
    def _topological_sort_helper(self, node, stack):
        node.been_visited = True 
        for child in node.children:
            if child.been_visited == False:
                self._topological_sort_helper(child, stack)
        
        stack.append(node.ident)

        return
    def topological_sort(self):

        stack = []
        for node in self.nodes:
            if node.been_visited == False:
                self._topological_sort_helper(node, stack)
        stack.reverse()
        return stack

    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class_graph = Graph(numCourses, prerequisites)
        if class_graph.cycle_detect():
            return []
        else:
            return class_graph.topological_sort()
        

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         class_graph = Graph(numCourses, prerequisites)
#         return not class_graph.cycle_detect()

# THIS IS WILD WTF
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        graph = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbors[pre].add(course)
        stack = [n for n in range(numCourses) if not graph[n]]
        result = []
        while stack:
            node = stack.pop()
            result.append(node)
            for n in neighbors[node]:
                graph[n].remove(node)
                if not graph[n]:
                    stack.append(n)
        return result if len(result) == numCourses else []