# search_methods.py
import heapq


def dfs(grid, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (x, y), path = stack.pop()
        print(f"Visiting: {(y, x)}, Path: {path}")
        if (x, y) == end:
            return path
        if (x, y) not in visited:
            visited.add((x, y))
            number = grid[y][x]
            for dx, dy in [(number, 0), (0, number), (-number, 0), (0, -number)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                    if grid[new_y][new_x] != 0 and (new_x, new_y) not in path:
                        stack.append(((new_x, new_y), path + [(new_x, new_y)]))
    return None


def uniform_cost_search(grid, start, end):
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        cost, (x, y), path = heapq.heappop(queue)
        print(f"Visiting: {(y, x)}, Path: {path}")  # Agregar para depuración
        if (x, y) == end:
            return path
        if (x, y) not in visited:
            visited.add((x, y))
            number = grid[y][x]
            for dx, dy in [(number, 0), (0, number), (-number, 0), (0, -number)]:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < len(grid[0])
                    and 0 <= new_y < len(grid)
                    and is_valid_move(grid, x, y, new_x, new_y)
                ):
                    new_cost = cost + 1
                    heapq.heappush(
                        queue, (new_cost, (new_x, new_y), path + [(new_x, new_y)])
                    )
    return None


# Función auxiliar para verificar si un movimiento es válido
def is_valid_move(grid, old_y, old_x, new_y, new_x):
    max_y, max_x = len(grid), len(grid[0])
    if 0 <= new_x < max_x and 0 <= new_y < max_y:
        if grid[new_y][new_x] == 0:
            return False
        if (abs(new_x - old_x) == grid[old_y][old_x] and new_y == old_y) or (
            abs(new_y - old_y) == grid[old_y][old_x] and new_x == old_x
        ):
            return True
    return False
