class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data: list[int]):
        self.data = data
    
    def draw(self):
        limit_numbers: list[int] = [number for number in self.data if number >= self.LIMIT_Y[0] \
                         and number <= self.LIMIT_Y[1]]
        print(' '.join(map(str, limit_numbers)))

              
graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
