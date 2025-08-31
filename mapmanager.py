class MapManager:
    def __init__(self):
        self.model = "models/block.egg"
        self.texture = "textures/block.png"
        self.colors = [
            (245, 39, 39, 0.8),
            (39, 245, 50, 0.86),
            (245, 204, 39, 0.86),
            (11, 5, 124, 0.8)
        ]
        self.add_lend_node()
        self.add_block((1, 1, 1))

    def add_lend_node(self):
        self.land = render.attachNewNode("Land")

    def clear_land_node(self):
        self.land.removeNode()
        self.add_lend_node()

    def add_block(self, position: tuple): #  (1, 2, 3)
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setColor(self.colors[0])
        self.block.setPos(position)
        self.block.reparentTo(self.land)
