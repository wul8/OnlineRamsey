import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
from networkx.algorithms import isomorphism as iso
import copy

class state:

    def __init__(self,graph,colors,step):
        """
        initialize state object
        :param graph: networkx object represents the graph
        :param colors: color list that will be allowed to use in painting the edge
        """
        self.graph = graph
        self.colors = colors
        self.successorStates = []
        self.step = step
        self.maxLength = 0
        self.colorsMappings = self.generate_colors_mapping()
        self.minStep = 0


    def __deepcopy__(self, memodict={}):
        """
        rewrite deepcopy function in copy package. Faster.
        """
        copy_object = state(self.graph.copy(),self.colors,self.step)
        copy_object.colorsMappings = self.colorsMappings
        copy_object.maxLength = self.maxLength
        return copy_object

    def updateSuccessorMin(self,minStep):
        """Update the min successor step to reach targeted chronomatic graph"""
        if self.minStep == 0:
            self.minStep = minStep
        else:
            self.minStep = min(self.minStep,minStep)

    def generate_colors_mapping(self):
        """Generate possible color mapping for checking isomorphic graph"""
        colorsMappings = []
        for perm in list(permutations(self.colors)):
            colorsMappings.append(dict(zip(self.colors,list(perm))))
        return colorsMappings

    def len(self):
        """
        get the number of nodes in graph
        :return: number of nodes
        """
        return len(self.graph)

    def colorList(self):
        """
        :return: return all the possible colorList
        """
        return self.colors


    def connect_node(self,indexA,indexB,colorName):
        """
        connect existing ndoes of indexA and indexB and coloring the edge with the colorName
        :param indexA: first node to connect
        :param indexB: second node to connect
        :param colorName: the name of the color to be painted on the new edge
        :return: True if connecting operation works; False if the nodes are already connected or the
                 one of the nodes does not exist
        """
        if self.graph.has_edge(indexA,indexB): return False
        self.step = self.step + 1
        self.graph.add_edge(indexA,indexB, color = colorName)
        return True

    def has_edge(self,indexA,indexB):
        return self.graph.has_edge(indexA,indexB)

    def add_node(self,indexA,colorName):
        """
        add extra node and connect it with one existing node
        :param indexA: the index of existing node to be connected
        :param colorName: the name of the color to be painted on the new edge
        :return: None
        """
        self.step = self.step + 1
        self.graph.add_edge(self.len(),indexA,color = colorName)

    def add_twoNodes(self,colorName):
        """
        add extra two nodes and connect them
        :param colorName: the name of the color to be painted on the new edge
        :return: None
        """
        self.step = self.step + 1
        self.graph.add_edge(self.len(),self.len()+1,color = colorName)

    def plot(self,index):
        """
        plot the state graph in the file image/Graph
        :param index: file name index
        :return: None
        """
        colors = nx.get_edge_attributes(self.graph,'color').values()
        fig = plt.figure()
        nx.draw(self.graph,with_labels = True,edge_color = colors)
        file_name = "image/Graph" + str(index) + "png"
        plt.savefig(file_name)
        plt.close(fig)

    def isConnected(self,indexI,indexJ):
        """
        check if to nodes are connected
        :param indexI: the first node
        :param indexJ: the second node
        :return: True if the nodes are connected; O/W false
        """
        return self.graph.has_edge(indexI,indexJ)


    def isIsomorphicGraph(graphA,graphB,colorsMappings):
        """
        check if two graphs are isomorphic regarding with
        :param graphB:
        :param colorsMappings:
        :return:
        """
        tempGraphB = copy.deepcopy(graphB)
        edgeColor = nx.get_edge_attributes(tempGraphB, "color")
        attr = {}
        for edge in nx.edges(tempGraphB):
            attr[edge]={"color":colorsMappings[edgeColor[edge]]}
        nx.set_edge_attributes(tempGraphB,attr)
        em = iso.categorical_edge_match('color', "red")
        if nx.is_isomorphic(graphA,tempGraphB,edge_match = em): return True
        return False

    def isIsomorphicTo(self,stateB):
        """
        check if stateA graph and stateB graph are isomorphic
        :param stateA: the first state
        :param stateB: the second state
        :return: True if stateA graph and stateB graph are isomorphic; O/W false
        """
        graphA = self.graph
        graphB = stateB.graph
        for Mapping in self.colorsMappings:
            if  state.isIsomorphicGraph(graphA,graphB,Mapping):
                return True
        return False


    def hasIsomorphic(self,lst):
        """
        check if the self state is isomorphic to the previous state that has been visited
        :param lst: lst of state that has already been visited
        :param step: how many steps required to reach self state. This parameter is used to reduce complexity
        :return: True if there exists a state that is isomorphic to the self state
        """

        for preState in lst:
            if preState.step == self.step and preState.len() == self.len() and \
                    self.isIsomorphicTo(preState):
                return preState
        return None

    def add_successor_states(self,nextState):
        """add one step further successor state of self state."""
        self.successorStates.append(nextState)

    def get_online_ramsey_number(self,limit):
        """
        return the online ramsey number given by the limited length of
        targeted choronomatic path. The function is used when all the
        states have already been generated.
        :param limit: the length of targeted choronomatic path
        :return: Online Ramsey Number
        """
        if self.maxLength >= limit:
            return self.step
        minNumber = float("inf")
        for category in self.successorStates:
            maxNumber = float("-inf")
            for nextState in category:
                nextRamseyNumber = nextState.get_online_ramsey_number(limit)
                maxNumber = max(nextRamseyNumber,maxNumber)
            if maxNumber != float("-inf"):
                minNumber = min(maxNumber,minNumber)
        return minNumber

    def update_max_path(self):
        """
        The longest chronomatic path in the current state graph
        """
        def dfs(currentNode,nodeList,color):
            nodeList.append(currentNode)
            maxLen = 1
            for node in self.graph.neighbors(currentNode):
                if node not in nodeList and self.graph[currentNode][node]["color"] == color:
                    maxLen = max(maxLen,dfs(node,nodeList,color)+1)
            return maxLen

        maxLen = 1
        for nodeI in self.graph.nodes():
            for nodeJ in self.graph.neighbors(nodeI):
                color = self.graph[nodeI][nodeJ]["color"]
                maxLen = max(maxLen,dfs(nodeJ,[nodeI,nodeJ],color))
        self.maxLength = maxLen

