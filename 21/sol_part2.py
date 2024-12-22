# itoombes, Advent of Code 2024
# Day 21

import heapq

#   ^ A
# < v >
ROBOT_PAD = {(0, 0) : "<",
             (1, 0) : "v",
             (2, 0) : ">",
             (1, 1) : "^",
             (2, 1) : "A"}
# 7 8 9
# 4 5 6
# 1 2 3
#   0 A
KEYPAD = {(1, 0) : "0",
          (2, 0) : "A",
          (0, 1) : "1",
          (1, 1) : "2",
          (2, 1) : "3",
          (0, 2) : "4",
          (1, 2) : "5",
          (2, 2) : "6",
          (0, 3) : "7",
          (1, 3) : "8",
          (2, 3) : "9"}

KEYPAD_INV = {}
for k, v in KEYPAD.items():
    KEYPAD_INV[v] = k

def read_sequences():
    f = open("input.txt", "r")
    sequences = list()
    for line in f.readlines():
        sequence = list()
        for c in line.replace("\n", ""):
            sequence.append(c)
        sequences.append(sequence)
    return sequences

def extract_number(sequence):
    string = ""
    for c in sequence[:3]:
        string += c
    return int(string)

def min_cost(transition_costs, init_state, target_state, valid_states):
    # (<state>, <upper arm action>)
    frontier = [(0, (init_state, "A")),]
    heapq.heapify(frontier)
    visited = {(init_state, "A") : 0}
    while len(frontier) > 0:
        cost, node = heapq.heappop(frontier)
        arm, control = node
        #print(f"{cost} : {arm}, {control}")
        # Check if state is goal
        if control == "A" and arm == target_state:
            return visited[(arm, "A")]
        # Generate successors
        # Storing in (<position>, <action>, <cost increment>)
        successors = list()
        x, y = arm
        if control == "<":
            successors.append(((x, y), "^", transition_costs["<"]["^"]))
            successors.append(((x, y), "v", transition_costs["<"]["v"]))
            successors.append(((x, y), "A", transition_costs["<"]["A"]))
            x -= 1
        elif control == ">":
            successors.append(((x, y), "^", transition_costs[">"]["^"]))
            successors.append(((x, y), "v", transition_costs[">"]["v"]))
            successors.append(((x, y), "A", transition_costs[">"]["A"]))
            x += 1
        elif control == "^":
            successors.append(((x, y), "<", transition_costs["^"]["<"]))
            successors.append(((x, y), ">", transition_costs["^"][">"]))
            successors.append(((x, y), "A", transition_costs["^"]["A"]))
            y += 1
        elif control == "v":
            successors.append(((x, y), "<", transition_costs["v"]["<"]))
            successors.append(((x, y), ">", transition_costs["v"][">"]))
            successors.append(((x, y), "A", transition_costs["v"]["A"]))
            y -= 1
        elif control == "A":
            successors.append(((x, y), "^", transition_costs["A"]["^"]))
            successors.append(((x, y), "v", transition_costs["A"]["v"]))
            successors.append(((x, y), "<", transition_costs["A"]["<"]))
            successors.append(((x, y), ">", transition_costs["A"][">"]))
        # Ensure motion is valid
        if (x, y) in valid_states.keys() and control != "A":
            successors.append(((x, y), control, 1))
        # Add unvisited or lesser path cost successors to frontier
        for nextPos, nextControl, costInc in successors:
            nextNode = (nextPos, nextControl)
            nextCost = cost + costInc
            if nextNode not in visited or nextCost < visited[nextNode]:
                visited[nextNode] = nextCost
                heapq.heappush(frontier, (nextCost, nextNode))

def process_transition_costs(depth):
    # Get the number of actions required to get to a "<action>, <action>, <BUTTON>" state
    # Start with depth 0 -- user controlled, no cost to change button
    transition_costs = {"A" : {"^" : 0, "<" : 0, ">" : 0, "v" : 0},
                        "^" : {"<" : 0, ">" : 0, "A" : 0},
                        "v" : {"<" : 0, ">" : 0, "A" : 0},
                        "<" : {"^" : 0, "v" : 0, "A" : 0},
                        ">" : {"^" : 0, "v" : 0, "A" : 0}}
    i = 1
    # Generate transition costs
    while i <= depth:
        AtU = min_cost(transition_costs, (2, 1), (1, 1), ROBOT_PAD)
        AtL = min_cost(transition_costs, (2, 1), (0, 0), ROBOT_PAD)
        AtR = min_cost(transition_costs, (2, 1), (2, 0), ROBOT_PAD)
        AtD = min_cost(transition_costs, (2, 1), (1, 0), ROBOT_PAD)

        UtL = min_cost(transition_costs, (1, 1), (0, 0), ROBOT_PAD)
        UtR = min_cost(transition_costs, (1, 1), (2, 0), ROBOT_PAD)
        UtA = min_cost(transition_costs, (1, 1), (2, 1), ROBOT_PAD)
        
        DtL = min_cost(transition_costs, (1, 0), (0, 0), ROBOT_PAD)
        DtR = min_cost(transition_costs, (1, 0), (2, 0), ROBOT_PAD)
        DtA = min_cost(transition_costs, (1, 0), (2, 1), ROBOT_PAD)

        LtU = min_cost(transition_costs, (0, 0), (1, 1), ROBOT_PAD)
        LtD = min_cost(transition_costs, (0, 0), (1, 0), ROBOT_PAD)
        LtA = min_cost(transition_costs, (0, 0), (2, 1), ROBOT_PAD)
        
        RtU = min_cost(transition_costs, (2, 0), (1, 1), ROBOT_PAD)
        RtD = min_cost(transition_costs, (2, 0), (1, 0), ROBOT_PAD)
        RtA = min_cost(transition_costs, (2, 0), (2, 1), ROBOT_PAD)

        transition_costs["A"]["^"] = AtU
        transition_costs["A"]["<"] = AtL
        transition_costs["A"][">"] = AtR
        transition_costs["A"]["v"] = AtD

        transition_costs["^"]["<"] = UtL
        transition_costs["^"][">"] = UtR
        transition_costs["^"]["A"] = UtA

        transition_costs["v"]["<"] = DtL
        transition_costs["v"][">"] = DtR
        transition_costs["v"]["A"] = DtA

        transition_costs["<"]["^"] = LtU
        transition_costs["<"]["v"] = LtD
        transition_costs["<"]["A"] = LtA

        transition_costs[">"]["^"] = RtU
        transition_costs[">"]["v"] = RtD
        transition_costs[">"]["A"] = RtA

        i += 1

    return transition_costs

def solve_sequence(sequence, transition_costs):
    cost = 0
    node = KEYPAD_INV["A"]
    for c in sequence:
        nextNode = KEYPAD_INV[c]
        # Cost is price to move + price to press button
        cost += min_cost(transition_costs, node, nextNode, KEYPAD) + 1
        node = nextNode
    return cost


def main():
    transition_costs = process_transition_costs(25)
    complexity = 0
    for sequence in read_sequences():
        cost = solve_sequence(sequence, transition_costs)
        print(f"{sequence} : {cost}")
        input()
        complexity += extract_number(sequence) * cost
    print(complexity)


if __name__ == "__main__":
    main()
