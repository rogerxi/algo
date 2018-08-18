"""Algorithm.

Big O:
    http://bigocheatsheet.com/

BFS & DFS:
    Stack is used together with DFS, and queue with BFS.
    When to use BFS, DFS, or either one of them?


Sort:
    Heap Sort

    Merge Sort

Tree:
    B Tree

    AVL Tree

    Read-Black Tree

Dynamic Programming

"""

from collections import defaultdict
import heapq
import unittest


def meeting_room_ii(intervals):
    """.

    Given an array of meeting time intervals consisting of start and end times
    [[s1,e1],[s2,e2],...], find the minimum number of rooms required.

    Reference:
        http://www.cnblogs.com/grandyang/p/5244720.html
    """
    # Solution 1:
    def solution1():
        min_rooms = 0
        rooms = 0
        heap = []
        intervals.sort(key=lambda x: x[0])
        for s1, e1 in intervals:
            rooms += 1
            heapq.heappush(heap, e1)
            while heap and heapq.nsmallest(1, heap)[0] <= s1:
                heapq.heappop(heap)
                rooms -= 1

            min_rooms = max(min_rooms, rooms)

        return min_rooms

    # Solution 2:
    def solution2():
        min_rooms = 0
        rooms = 0
        start_times = [s1 for s1, _ in intervals]
        start_times.sort()
        end_times = [e1 for _, e1 in intervals]
        end_times.sort()
        i, j = 0, 0
        while i < len(start_times):
            if start_times[i] < end_times[j]:
                rooms += 1
                min_rooms = max(min_rooms, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1

        return min_rooms

    solution2()
    return solution1()


def find_top_followees(matrix):
    """.

    Given a matrix of followings of followers and followees,
    find the top followees which have links to all other followers.
    For example, a matrix for 4 members (a, b, c, d):

    [[0 1 0 0]      # b follows a.
     [0 0 0 0]
     [0 0 0 1]
     [0 0 1 0]]

    The answer is [a, c] or [a, d].
    """
    top_followees = []

    # Union find.

    # BFS.
    # unions = list()
    # for row in matrix:
    #     for cell in row:
    #         for union in unions:

    # DFS.
    def dfs(matrix):
        top_followees = []
        nodes_accessed = set()
        nodes_to_access = set(range(len(matrix)))
        while nodes_to_access:
            node = nodes_to_access.pop()
            nodes_accessed.add(node)
            # followers = []
            followees = [node]
            while followees:
                followee = followees.pop()
                for index, following in enumerate(matrix[followee]):
                    if following:
                        followees.append(index)

        return top_followees

    return top_followees


def dijkstra():
    """."""
    pass


def find_min_height_trees(n, edges):
    """.

    https://leetcode.com/problems/minimum-height-trees/description/

    Example:
        Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
        Output: [3, 4]
    """
    # TODO: improve performance.
    if not edges:
        return [0]

    # Construct a mapping from node to a set of linked nodes.
    edges_dict = defaultdict(set)
    for node1, node2 in edges:
        edges_dict[node1].add(node2)
        edges_dict[node2].add(node1)

    while len(edges_dict) > 2:
        # Remove the leaf nodes.
        leaf_nodes = dict()
        for node1, linked_nodes in edges_dict.items():
            if len(linked_nodes) == 1:
                leaf_nodes[node1] = linked_nodes.pop()
                edges_dict.pop(node1)

        # Remove the links between leaf nodes and other nodes.
        for leaf_node in leaf_nodes:
            edges_dict[leaf_nodes[leaf_node]].remove(leaf_node)

    return edges_dict.keys()


class TestCaseAlgo(unittest.TestCase):
    """Test case for alogorithms."""

    def assert_equal(self, func, data):
        """Equal assertion.

        Args:
            func: object, function to be tested.
            data: list, list of input arguments and expected output.
        """
        for args, output in data:
            self.assertEqual(func(args), output)

    def test_meeting_room_ii(self):
        """."""
        self.assert_equal(meeting_room_ii, (
            ([[1, 4], [2, 3], [3, 8], [4, 7], [5, 9], [6, 7]], 4),
            ([[0, 30], [5, 10], [15, 20]], 2),
            ([[0, 30], [15, 40], [10, 35], [40, 45]], 3),
        ))


if __name__ == '__main__':
    unittest.main()
