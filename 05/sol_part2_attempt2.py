# itoombes, Advent of Code 2024
# Day 5 Part 2 Attempt 2


def parse_rules():
    """
    Returns a dictionary of "input -> pre-req"
    """
    f = open("input1.txt", "r")
    rules = dict()
    for rule in f.readlines():
        prereq = int(rule[0:2])
        number = int(rule[3:5])
        if number not in rules:
            rules[number] = [prereq,]
        elif prereq not in rules[number]:
            rules[number].append(prereq)
    return rules

def parse_orders():
    """
    Returns each order as a list of integers
    """
    f = open("input2.txt", "r")
    orders = list()
    for line in f:
        order = list()
        for page in line.split(","):
            order.append(int(page))
        orders.append(order)
    return orders

def ordered(order, rules):
    """
    Returns list of orders
    """
    i = 0
    nPages = len(order)
    while i < nPages:
        if order[i] in rules:
            for prereq in rules[order[i]]:
                if prereq in order[i:-1]:
                    return False
        i += 1
    return True

def reduce_ruleset(order, rules):
    ruleset = dict()
    for page in order:
        if page in rules:
            ruleset[page] = list()
            for prereq in rules[page]:
                if prereq in order:
                    ruleset[page].append(prereq)
    return ruleset

def parse_correct_order(order, rules):
    # Establish each present pre-req for each page
    newOrder = list()
    while len(order) > 0:
        rules = reduce_ruleset(order, rules)
        minimumInDegree = 10000000
        minimum = 1000000
        for page in order:
            inDegree = len(rules[page])
            if inDegree < minimumInDegree:
                minimumInDegree = inDegree
                minimum = page
        if minimumInDegree != 0:
            raise ValueError("Minimum has a prerequisite!")
        newOrder.append(minimum)
        order.remove(minimum)
    return newOrder 

def main():
    rules = parse_rules()
    printOrders = parse_orders()

    result = 0
    for order in printOrders:
        if not ordered(order, rules):
            correctOrder = parse_correct_order(order, rules)
            result += correctOrder[(len(correctOrder) - 1) // 2]

    print(result)

if __name__ == "__main__":
    main()
