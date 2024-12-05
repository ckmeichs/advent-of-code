from collections import defaultdict, deque

class PrintQueue:
    def __init__(self, content):
        rules_section, updates_section = content.strip().split("\n\n")
        self.rules = set()
        for line in rules_section.splitlines():
            x, y = map(int, line.split('|'))
            self.rules.add((x, y))
        self.updates = []
        for line in updates_section.splitlines():
            self.updates.append(list(map(int, line.split(','))))

    def is_update_valid(self, update):
        index_map = {page: idx for idx, page in enumerate(update)}
        for x, y in self.rules:
            if x in index_map and y in index_map:  
                if index_map[x] > index_map[y]:
                    return False
        return True

    def part_one(self):
        result = 0
        for update in self.updates:
            if self.is_update_valid(update):
                middle_index = len(update) // 2
                middle_page = update[middle_index]
                result += middle_page
        print(result)

    def topological_sort(self, pages):
        graph = defaultdict(list)
        in_degree = {page: 0 for page in pages}
        for x, y in self.rules:
            if x in pages and y in pages:
                graph[x].append(y)
                in_degree[y] += 1
        queue = deque([page for page in pages if in_degree[page] == 0])
        sorted_pages = []
        while queue:
            current = queue.popleft()
            sorted_pages.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return sorted_pages
    
    def part_two(self):
        result = 0
        for update in self.updates:
            if not self.is_update_valid(update):
                fixed_update = self.topological_sort(update)
                middle_index = len(fixed_update) // 2
                middle_page = fixed_update[middle_index]
                result += middle_page
        print(result)
