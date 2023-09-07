from collections import deque

def is_valid_state(m, c):
    # Check if the state is valid (no missionaries outnumbered by cannibals)
    return m == 0 or (m >= c)

def mnc_tree_search(m, c):
    # Check if the initial state is valid
    if not is_valid_state(m, c):
        return False

    # Define possible actions (boat configurations)
    actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    # Create a queue for BFS
    queue = deque([(m, c, "L", [])])  # (m, c, boat_side, path)

    while queue:
        m_current, c_current, boat_side, path = queue.popleft()

        # Check if we have reached the goal state
        if m_current == 0 and c_current == 0 and boat_side == "R":
            return path

        for m_action, c_action in actions:
            # Determine the new state after the action
            if boat_side == "L":
                m_new = m_current - m_action
                c_new = c_current - c_action
                boat_new_side = "R"
            else:
                m_new = m_current + m_action
                c_new = c_current + c_action
                boat_new_side = "L"

            # Check if the new state is valid and within bounds
            if is_valid_state(m_new, c_new) and 0 <= m_new <= m and 0 <= c_new <= c:
                new_path = path + [(m_action, c_action)]
                queue.append((m_new, c_new, boat_new_side, new_path))

    return False  # No solution found

# Test cases
print(mnc_tree_search(2, 1))  # ((2, 0), (1, 0), (1, 1))
print(mnc_tree_search(2, 2))  # ((1, 1), (1, 0), (2, 0), (1, 0), (1, 1))
print(mnc_tree_search(3, 3))  # ((1, 1), (1, 0), (0, 2), (0, 1), (2, 0), (1, 1), (2, 0), (0, 1), (0, 2), (1, 0), (1, 1))


# Test cases for Task 1.6
# def test_16():
#     expected = ((2, 0), (1, 0), (1, 1))
#     assert(mnc_tree_search(2,1) == expected)

#     expected = ((1, 1), (1, 0), (2, 0), (1, 0), (1, 1))
#     assert(mnc_tree_search(2,2) == expected)

#     expected = ((1, 1), (1, 0), (0, 2), (0, 1), (2, 0), (1, 1), (2, 0), (0, 1), (0, 2), (1, 0), (1, 1))
#     assert(mnc_tree_search(3,3) == expected)   

#     assert(mnc_tree_search(4, 4) == False)

#test_16()

from collections import deque

def is_valid_state(m, c):
    return m == 0 or (m >= c)

def mnc_graph_search(m, c):
    if not is_valid_state(m, c):
        return False

    actions = [(m_action, c_action) for m_action in range(m + 1) for c_action in range(c + 1)]
    actions = [(m, c) for m, c in actions if 0 < m + c <= 2 and (m >= c or m == 0)]

    visited = set()
    queue = deque([(m, c, "L", [])])  # (m, c, boat_side, path)

    while queue:
        m_current, c_current, boat_side, path = queue.popleft()
        state = (m_current, c_current, boat_side)

        if state in visited:
            continue

        visited.add(state)

        if m_current == 0 and c_current == 0 and boat_side == "R":
            return path

        for m_action, c_action in actions:
            if boat_side == "L":
                m_new = m_current - m_action
                c_new = c_current - c_action
                boat_new_side = "R"
            else:
                m_new = m_current + m_action
                c_new = c_current + c_action
                boat_new_side = "L"

            if is_valid_state(m_new, c_new) and 0 <= m_new <= m and 0 <= c_new <= c:
                new_path = path + [(m_action, c_action)]
                queue.append((m_new, c_new, boat_new_side, new_path))

    return False



# Test cases for Task 1.7
def test_17():
    expected = ((2, 0), (1, 0), (1, 1))
    result = mnc_graph_search(2, 1)
    print("Expected:", expected)
    print("Result:", result)
    assert result == expected

    expected = ((1, 1), (1, 0), (2, 0), (1, 0), (1, 1))
    result = mnc_graph_search(2, 2)
    print("Expected:", expected)
    print("Result:", result)
    assert result == expected

    expected = ((1, 1), (1, 0), (0, 2), (0, 1), (2, 0), (1, 1), (2, 0), (0, 1), (0, 2), (1, 0), (1, 1))
    result = mnc_graph_search(3, 3)
    print("Expected:", expected)
    print("Result:", result)
    assert result == expected

    result = mnc_graph_search(4, 4)
    print("Expected: False")
    print("Result:", result)
    assert result == False

# Run the test cases
test_17()


    

# Task 2.3
def pitcher_search(p1,p2,p3,a):
    '''
    Solution should be the action taken from the root node (initial state) to 
    the leaf node (goal state) in the search tree.

    Parameters
    ----------    
    p1: capacity of pitcher 1
    p2: capacity of pitcher 2
    p3: capacity of pitcher 3
    a: amount of water we want to measure
    
    Returns
    ----------    
    Returns the solution to the problem as a tuple of steps. Each step is a string: "Fill Pi", "Empty Pi", "Pi=>Pj". 
    If there is no solution, return False.
    '''
    # TODO: add your solution here and remove `raise NotImplementedError`
    raise NotImplementedError

# Test cases for Task 2.3
def test_23():
    expected = ('Fill P2', 'P2=>P1')
    assert(pitcher_search(2,3,4,1) == expected)

    expected = ('Fill P3', 'P3=>P1', 'Empty P1', 'P3=>P1')
    assert(pitcher_search(1,4,9,7) == expected)

    assert(pitcher_search(2,3,7,8) == False)

#test_23()