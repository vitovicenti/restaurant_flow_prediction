class Search_problem(object):
    """A search problem consists of:
    * a start node
    * a neighbors function that gives the neighbors of a node
    * a specification of a goal
    * a (optional) heuristic function.
    The methods must be overridden to define a search problem."""

    def start_node(self):
        """returns start node"""
        raise NotImplementedError("start_node")  # abstract method

    def is_goal(self, node):
        """is True if node is a goal"""
        raise NotImplementedError("is_goal")  # abstract method

    def neighbors(self, node):
        """returns a list of the arcs for the neighbors of node"""
        raise NotImplementedError("neighbors")  # abstract method

    def heuristic(self, n):
        """Gives the heuristic value of node n.
        Returns 0 if not overridden."""
        return 0


class Arc(object):
    """An arc has a from_node and a to_node node and a (non-negative) cost"""

    def __init__(self, from_node, to_node, cost=1, action=None):
        assert cost >= 0, ("Cost cannot be negative for" +
                           str(from_node) + "->" + str(to_node) + ", cost: " + str(cost))
        self.from_node = from_node
        self.to_node = to_node
        self.action = action
        self.cost = cost

    def __repr__(self):
        """string representation of an arc"""
        if self.action:
            return str(self.from_node) + " --" + str(self.action) + "--> " + str(self.to_node)
        else:
            return str(self.from_node) + " --> " + str(self.to_node)




class Search_problem_from_explicit_graph(Search_problem):
    """A search problem consists of:
    * a list or set of nodes
    * a list or set of arcs
    * a start node
    * a list or set of goal nodes
    * a dictionary that maps each node into its heuristic value.
    * a dictionary that maps each node into its (x,y) position
    """

    def __init__(self, nodes, arcs, start=None, goals=set(), hmap={}, positions={}):
        self.neighs = {}
        self.nodes = nodes
        for node in nodes:
            self.neighs[node] = []
        self.arcs = arcs
        for arc in arcs:
            self.neighs[arc.from_node].append(arc)
        self.start = start
        self.goals = goals
        self.hmap = hmap
        self.positions = positions

    def start_node(self):
        """returns start node"""
        return self.start

    def is_goal(self, node):
        """is True if node is a goal"""
        return node in self.goals

    def neighbors(self, node):
        """returns the neighbors of node"""
        return self.neighs[node]

    def heuristic(self, node):
        """Gives the heuristic value of node n.
        Returns 0 if not overridden in the hmap."""
        if node in self.hmap:
            return self.hmap[node]
        else:
            return 0

    def __repr__(self):
        """returns a string representation of the search problem"""
        res = ""
        for arc in self.arcs:
            res += str(arc) + ".  "
        return res

    def neighbor_nodes(self, node):
        """returns an iterator over the neighbors of node"""
        return (path.to_node for path in self.neighs[node])


class Path(object):
    """A path is either a node or a path followed by an arc"""

    def __init__(self, initial, arc=None):
        """initial is either a node (in which case arc is None) or
        a path (in which case arc is an object of type Arc)"""
        self.initial = initial
        self.arc = arc
        if arc is None:
            self.cost = 0
        else:
            self.cost = initial.cost + arc.cost

    def end(self):
        """returns the node at the end of the path"""
        if self.arc is None:
            return self.initial
        else:
            return self.arc.to_node

    def nodes(self):
        """enumerates the nodes for the path.
        This starts at the end and enumerates nodes in the path backwards."""
        current = self
        while current.arc is not None:
            yield current.arc.to_node
            current = current.initial
        yield current.initial

    def initial_nodes(self):
        """enumerates the nodes for the path before the end node.
        This starts at the end and enumerates nodes in the path backwards."""
        if self.arc is not None:
            yield from self.initial.nodes()

    def __repr__(self):
        """returns a string representation of a path"""
        if self.arc is None:
            return str(self.initial)
        elif self.arc.action:
            return (str(self.initial) + "\n   --" + str(self.arc.action)
                    + "--> " + str(self.arc.to_node))
        else:
            return str(self.initial) + " --> " + str(self.arc.to_node)


    #definizione del grafo che rappresenta la mappa della città

    nod = list()
    nod.append("A")
    nod.append("B")
    nod.append("C")
    nod.append("D")
    nod.append("E")
    nod.append("F")
    nod.append("G")
    nod.append("H")
    nod.append("I")
    nod.append("R")
    nod.append("A1")
    nod.append("A2")
    nod.append("A3")
    nod.append("A4")
    nod.append("A5")

    archi = list()
    archi.append(Arc('A', 'C', 200))
    archi.append(Arc('C', 'A', 200))
    archi.append(Arc('A', 'A1', 250))
    archi.append(Arc('A1', 'A', 250))
    archi.append(Arc('C', 'A1', 300))
    archi.append(Arc('A1', 'C', 300))
    archi.append(Arc('C', 'E', 200))
    archi.append(Arc('E', 'C', 200))
    archi.append(Arc('A1', 'B', 600))
    archi.append(Arc('B', 'A1', 600))
    archi.append(Arc('E', 'B', 750))
    archi.append(Arc('B', 'E', 750))
    archi.append(Arc('E', 'R', 100))
    archi.append(Arc('R', 'E', 100))
    archi.append(Arc('D', 'B', 250))
    archi.append(Arc('B', 'D', 250))
    archi.append(Arc('A2', 'D', 70))
    archi.append(Arc('D', 'A2', 70))
    archi.append(Arc('A2', 'B', 100))
    archi.append(Arc('B', 'A2', 100))
    archi.append(Arc('D', 'F', 600))
    archi.append(Arc('F', 'D', 600))
    archi.append(Arc('F', 'R', 200))
    archi.append(Arc('R','F', 200))
    archi.append(Arc('F', 'A4', 700))
    archi.append(Arc('A4', 'F', 700))
    archi.append(Arc('A4', 'A5', 1000))
    archi.append(Arc('A5', 'A4', 1000))
    archi.append(Arc('A4', 'I', 100))
    archi.append(Arc('I', 'A4', 100))
    archi.append(Arc('I', 'A5', 800))
    archi.append(Arc('A5', 'I', 800))
    archi.append(Arc('A5', 'G', 250))
    archi.append(Arc('G', 'A5', 250))
    archi.append(Arc('G', 'A3', 200))
    archi.append(Arc('A3', 'G', 200))
    archi.append(Arc('G', 'R', 500))
    archi.append(Arc('R', 'G', 500))
    archi.append(Arc('H', 'C', 1000))
    archi.append(Arc('C', 'H', 1000))
    archi.append(Arc('H', 'A3', 300))
    archi.append(Arc('A3', 'H', 300))
    archi.append(Arc('H', 'G', 250))
    archi.append(Arc('G', 'H', 250))



    positions = {'A': (2, 3),
                 'B': (3, 13),
                 'C': (6, 3),
                 'D': (6, 17),
                 'E': (8, 8),
                 'F': (12, 13),
                 'G': (17, 6),
                 'H': (19, 1),
                 'I': (19, 17),

                 'Albergo 1': (3, 8),
                 'Albergo 2': (7, 15),
                 'Albergo 3': (15, 3),
                 'Albergo 4': (16, 19),
                 'Albergo 5': (18, 10),

                 'Ristorante': (11, 8)}



    #definizione dei problemi di ricerca

    P1 = Search_problem_from_explicit_graph(nod, archi, start='A1', goals={'R'}, positions=positions)
    P2 = Search_problem_from_explicit_graph(nod, archi, start='A2', goals={'R'}, positions=positions)
    P3 = Search_problem_from_explicit_graph(nod, archi, start='A3', goals={'R'}, positions=positions)
    P4 = Search_problem_from_explicit_graph(nod, archi, start='A4', goals={'R'}, positions=positions)
    P5 = Search_problem_from_explicit_graph(nod, archi, start='A5', goals={'R'}, positions=positions)




