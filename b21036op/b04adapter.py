class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee


    def lighten(self, grid):
        w = len(grid[0])
        h = len(grid)
        # print(w,h)
        self.adaptee.set_dim((w, h))
        k = -1
        s0 = []
        for i, a in enumerate(grid):
            for j, b in enumerate(a):
                if b == k:
                    s0 += [(j, i)]        
        k = 1
        s1 = []
        for i, a in enumerate(grid):
            for j, b in enumerate(a):
                if b == k:
                    s1 += [(j, i)]        
        self.adaptee.generate_lights()
        self.adaptee.set_obstacles(s0)
        self.adaptee.set_lights(s1)
        print(s0, s1)
        return self.adaptee.generate_lights()


if __name__ == "__main__":

    class Light:
        def __init__(self, dim):
            self.dim = dim
            self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
            self.lights = []
            self.obstacles = []
            
        def set_dim(self, dim):
            self.dim = dim
            self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        
        def set_lights(self, lights):
            self.lights = lights
            self.generate_lights()
        
        def set_obstacles(self, obstacles):
            self.obstacles = obstacles
            self.generate_lights()
            
        def generate_lights(self):
            return self.grid.copy()


    class System:
        def __init__(self):
            self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
            self.map[5][7] = 1 # Источники света
            self.map[4][7] = 1 # Источники света
            self.map[5][2] = -1 # Стены
            self.map[6][2] = -1 # Стены
        
        def get_lightening(self, light_mapper):
            self.lightmap = light_mapper.lighten(self.map)

    system = System()
    light = Light((30, 20))
    mappingAdapter = MappingAdapter(light)

    system.get_lightening(mappingAdapter)
    # print('aaaa')
