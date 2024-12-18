import heapq

class ReindeerMaze:
    def __init__(self, content):
        self.labyrinth = []
        self.start = ()
        self.goal = ()
        trimmend_content = content[1:-1]
        i = 0
        for y in trimmend_content:
            trimmend_y = y[1:-1]
            lx = []
            j = 0
            for x in trimmend_y:
                if x == 'S':
                    self.start = (j, i)
                    lx.append(".")
                elif x == 'E':
                    self.goal = (j, i)
                    lx.append(".")
                else:
                    lx.append(x)
                j += 1
            i += 1
            self.labyrinth.append(lx)
        self.print_labyrinth()

    def print_labyrinth(self):
        for y in self.labyrinth:
            print(y)
        print("start x, y", self.start)
        print("end x, y", self.goal)

    def heuristic(self, pos):
        """Manhattan-Distanz als Heuristik! Weißte Bescheid Schätzelein?"""
        return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])

    def shortest_path_with_turn_penalty(self, turn_cost=1000, move_cost=1):
        rows, cols = len(self.labyrinth), len(self.labyrinth[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Rechts, Unten, Links, Oben

        # Priority-Queue für A*
        priority_queue = []
        heapq.heappush(priority_queue, (0, self.start, None))  # (Kosten, Position, Richtung)
        
        visited = {}  # Speichert: Position -> minimale Kosten
        previous = {}  # Speichert: Position -> vorherige Position

        while priority_queue:
            cost, (x, y), direction = heapq.heappop(priority_queue)

            # Ziel erreicht
            if (x, y) == self.goal:
                print(f"Ziel erreicht mit {cost} Kosten")
                # Rekonstruiere den Pfad
                path = []
                current = (x, y)
                while current != self.start:
                    path.append(current)
                    current = previous[current]
                path.append(self.start)
                path.reverse()  # Pfad umdrehen, sodass er vom Start zum Ziel verläuft
                print(f"Pfad: {path}")
                return cost, path

            # Überspringe, wenn wir diesen Knoten bereits günstiger besucht haben
            if (x, y) in visited and visited[(x, y)] <= cost:
                continue
            visited[(x, y)] = cost

            # Bewegungen auswerten
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy

                # Prüfen, ob die Bewegung gültig ist
                if 0 <= nx < rows and 0 <= ny < cols and self.labyrinth[nx][ny] == ".":
                    # Kosten berechnen
                    new_direction = i
                    extra_cost = move_cost if direction == new_direction else move_cost + turn_cost

                    # Falls neue Position günstiger, füge sie zur Queue hinzu
                    if (nx, ny) not in visited or visited[(nx, ny)] > cost + extra_cost:
                        heapq.heappush(priority_queue, (cost + extra_cost + self.heuristic((nx, ny)), (nx, ny), new_direction))
                        previous[(nx, ny)] = (x, y)  # Speichere die vorherige Position

            return None, []  # Kein Weg gefunden
    
    def part_one(self):
        path, cost = self.shortest_path_with_turn_penalty()
        if cost:
            print(cost)
            for pos in path:
                x, y = pos
                self.labyrinth[x][y] = "+"
            self.print_labyrinth()
        else:
            print("Kein Weg gefunden.")
            