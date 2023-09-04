class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            return True
        return False


if __name__ == '__main__':
        n, m = map(int, input().split())
        count = 0
        mx = 0
        dsu = DSU(n)
        travels = []
        for _ in range(m):
            v, u, w = map(int, input().split())
            travels.append((v-1, u-1, w))
        travels = sorted(travels, key=lambda x: x[2], reverse=True)
        answer = travels[0][2]
        for v, u, w in travels:
            if dsu.union(v, u):
                answer = w - 1

        print(answer)
