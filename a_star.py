import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan Distance

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            break
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            next_node = (current[0]+dx, current[1]+dy)
            if 0 <= next_node[0] < rows and 0 <= next_node[1] < cols and grid[next_node[0]][next_node[1]] == 0:
                new_cost = cost_so_far[current] + 1
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(goal, next_node)
                    heapq.heappush(open_set, (priority, next_node))
                    came_from[next_node] = current
    # Rekonstruksi jalur
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()
    return path

# Contoh penggunaan
grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]
start = (0, 0)
goal = (0, 3)
print("Jalur terpendek:", a_star_search(grid, start, goal))
