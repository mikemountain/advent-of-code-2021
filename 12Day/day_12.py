from pprint import pprint

def find_all_paths(graph, start, end, revisited = False, small_cave = '', path = []):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node.isupper():
            newpaths = find_all_paths(graph, node, end, revisited, small_cave, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif node in ['start', 'end'] and node not in path:
            newpaths = find_all_paths(graph, node, end, revisited, small_cave, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif node in path and not revisited and node not in ['start', 'end']:
            newpaths = find_all_paths(graph, node, end, True, small_cave, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif node not in path:
            small_cave = node
            newpaths = find_all_paths(graph, node, end, revisited, small_cave, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

with open('input.txt') as f:
    dag = {}
    lines = [line.strip() for line in f]
    for l in lines:
        cave_1, cave_2 = l.split('-')
        if cave_1 not in dag:
            dag[cave_1] = [cave_2]
        else:
            dag[cave_1].append(cave_2)

        if cave_2 not in dag:
            dag[cave_2] = [cave_1]
        else:
            dag[cave_2].append(cave_1)
    
    all_paths = find_all_paths(dag, 'start', 'end')
    print(len(all_paths))