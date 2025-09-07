class Hero():
    def __init__(self, position, land):
        self.canera_mode = None
        self.game_mode = True
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.set_color((119/100, 25/100, 30/100, 0.94))
        self.hero.setScale(0.3)
        self.hero.setPos(position)
        self.hero.reparentTo(render)

        self.camera_bind()
        self.accept_events()

    def camera_bind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.camera_mode = True

    def camera_up(self):
        pos = self.hero.getPos() #(3 2 1)
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] -3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.camera_mode = False

    def switch_camera(self):
        if self.camera_mode:
            self.camera_up()
        else:
            self.camera_bind()
        
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def move_to(self):
        """Обираємо як рухати гравця в залежності від режиму гри"""
        if self.game_mode == True:
            self.just_move()
        else:
            self.try_move()

    def just_move(self):
        """Рух гравця в режимі спостерігача"""
        pass

    def try_move(self):
        """Рух гравця в основному ігровому режимі"""
        pass

    def check_dir(self, angle):
       ''' повертає заокруглені зміни координат X, Y,
       відповідні переміщенню у бік кута angle.
       Координата Y зменшується, якщо персонаж дивиться на кут 0,
       та збільшується, якщо дивиться на кут 180.
       Координата X збільшується, якщо персонаж дивиться на кут 90,
       та зменшується, якщо дивиться на кут 270.
           кут 0 (від 0 до 20) -> Y - 1
           кут 45 (від 25 до 65) -> X + 1, Y - 1
           кут 90 (від 70 до 110) -> X + 1
           від 115 до 155 -> X + 1, Y + 1
           від 160 до 200 -> Y + 1
           від 205 до 245 -> X - 1, Y + 1
           від 250 до 290 -> X - 1
           від 290 до 335 -> X - 1, Y - 1
           від 340 -> Y - 1
       '''
       if 0 <= angle <= 20:
           return 0, -1
       elif angle <= 65:
           return 1, -1
       elif angle <= 110:
           return 1, 0
       elif angle <= 155:
           return 1, 1
       elif angle <= 200:
           return 0, 1
       elif angle <= 245:
           return -1, 1
       elif angle <= 290:
           return -1, 0
       elif angle <= 335:
           return -1, -1
       else:
           return 0, -1


    def accept_events(self):
        base.accept("c", self.switch_camera)
        base.accept("n", self.turn_left)
        base.accept("n" + "-repeat", self.turn_left)
        base.accept("m", self.turn_right)
        base.accept("m" + "-repeat", self.turn_right)