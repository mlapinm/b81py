class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee


    def lighten(self, grid):
        wh = (len(grid), len(grid[0]))
        # print(wh)
        self.adaptee.set_dim(wh)
        k = -1
        s0 = [(e.index(k), i) for i, e in enumerate(grid) if k in e]
        # s0 = [(i, e.index(k)) for i, e in enumerate(grid) if k in e]
        k = 1
        s1 = [(e.index(k),i) for i, e in enumerate(grid) if k in e]
        # s1 = [(i, e.index(k)) for i, e in enumerate(grid) if k in e]
        self.adaptee.set_lights(s1)
        self.adaptee.set_obstacles(s0)
        # print(s0, s1)
        grid2 = self.adaptee.generate_lights()
        w = len(grid)
        h = len(grid[0])
        grid3 = [[0 for e in range(h)] for _ in range(w)]
        for i, e in enumerate(grid2):
            for j, n in enumerate(e):
                grid3[j][i] = n
        return grid3

