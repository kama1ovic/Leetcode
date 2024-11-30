from collections import defaultdict, deque

class Solution:
    def validArrangement(self, pairs):
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        # 1. Grafni qurish va darajalarni hisoblash
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # 2. Boshlanish nuqtasini aniqlash
        start_node = pairs[0][0]
        for start in out_degree:
            if out_degree[start] > in_degree[start]:
                start_node = start
                break

        # 3. Natijani yig'ish
        result = []

        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
                result.append([node, next_node])

        dfs(start_node)

        # 4. Natijani teskari qaytarish
        return result[::-1]

# Misol uchun foydalanish
solution = Solution()
pairs = [[5,1],[4,5],[11,9],[9,4]]
output = solution.validArrangement(pairs)
print(output)  # Kutilgan natijani olish
