from common.read import read_input
import re


def parse_row(row, with_counts=False):
    parent, children = row.split("contain")
    parent = " ".join(parent.split(" ")[:2])
    children = children.strip()
    children = re.findall("\d \w* \w* bag[s]?[,]?", children)
    if with_counts:
        children = [" ".join(child.split(" ")[0:3]) for child in children]
    else:
        children = [" ".join(child.split(" ")[1:3]) for child in children]

    return parent, children


def part_1():
    start = "shiny gold"
    bags = {}

    raw_data = read_input(7, 1)
    for l in raw_data:
        parent, children = parse_row(l)
        bags[parent] = children

    nodes = bags.keys()
    connected = []
    friends = []

    for k, v in bags.items():
        if k != start:
            if start in v:
                connected.append(k)
                friends.append(k)

    while connected:
        node = connected.pop()
        for k, v in bags.items():
            if k != node:
                if node in v:
                    connected.append(k)
                    friends.append(k)
    print(len(set(friends)))


def traverse(graph, start):
    sum = 0
    if graph[start]:
        for node in graph[start]:
            n_count, n_name = node.split(" ", maxsplit=1)
            n_count = int(n_count)
            sum += n_count + n_count * traverse(graph, n_name)
        return sum
    return 0


def part_2():
    start = "shiny gold"
    bags = {}

    raw_data = read_input(7, 1)
    for l in raw_data:
        parent, children = parse_row(l, with_counts=True)
        bags[parent] = children

    # children = []
    # to_visit = []
    # for child in bags[start]:
    #     count, node = child.split(" ", maxsplit=1)
    #     to_visit.append((node, int(count)))
    #     children.append((node, int(count)))

    # while to_visit:
    #     current = to_visit.pop()
    #     for child in bags[current[0]]:
    #         count, node = child.split(" ", maxsplit=1)
    #         to_visit.append((node, int(count)))
    #         children.append((node, int(count)))
    # print(children)
    total = traverse(bags, start)
    print(total)


if __name__ == "__main__":
    part_1()
    part_2()